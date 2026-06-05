"""Refresh stale translation.
"""
import os
import sys
import logging
import pathlib
from itertools import chain

from git import Repo

from translator.utils import (get_forced_filepaths,
                              check_environment,
                              get_language,
                              md_filter)
from translator.snapshots import read_commit_sha, write_head_sha
from translator.persistence import SwiftCache as TranslationCache
from translator.pages import Translations
from translator.api import translate_markdown


logger = logging.getLogger(__name__)

try:
    check_environment("LANG_CODE",
                      "CLONE_PATH",
                      "DOCS_DIR")

    DOCS_DIR = os.getenv("DOCS_DIR")
    LANG_CODE = os.getenv("LANG_CODE")
    lang_name = get_language(LANG_CODE)
    repo_path = pathlib.Path(os.getenv("CLONE_PATH"))
except:
    logger.error("Failed to initialize translator.")
    raise


def _main(dest_dir: str,
          head_sha_output_path: str,
          cache_dump_path: str):
    repo = Repo(repo_path)

    head_commit_sha = repo.head.commit.hexsha
    head_tree = repo.head.commit.tree[DOCS_DIR]
    latest_commit_sha, k = read_commit_sha()
    latest_tree = repo.commit(latest_commit_sha).tree[DOCS_DIR]

    logger.info("Handling diff %s...%s.",
                latest_commit_sha,
                head_commit_sha)

    translations = Translations(repo_path / DOCS_DIR,
                                pathlib.Path(dest_dir),
                                TranslationCache(repo_path))

    forced = get_forced_filepaths(latest_commit_sha, k, LANG_CODE)
    diff_index = filter(md_filter, latest_tree.diff(head_tree))

    translations.include(*chain(forced, diff_index))

    for page in translations.pending:
        page.pending_operation()

    n_pages = len(translations)
    logger.info("%s pages to translate.",
                "No" if n_pages < 1 else str(n_pages))

    for page in translations:
        logger.info("Translating '%s' to '%s'...", page.path, lang_name)
        result = translate_markdown(page.original)
        page.write_translation(result)

    if not translations.is_empty:
        write_head_sha(head_commit_sha, head_sha_output_path)

    translations.complete(cache_dump_path)


if __name__ == "__main__":
    try:
        _main(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError as e:
        logger.error("Error reading command-line arguments: %s", str(e))

        raise
