#! /usr/bin/env python3
"""Refresh stale translation.
"""
import os
import sys
import logging
import pathlib
from itertools import chain

from git import Repo

from translator.constants import DEFAULTS
from translator.repo import sparse_checkout, copy_git_dir
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
    check_environment("LANG_CODE")
    lang_code = os.getenv("LANG_CODE")
    lang_name = get_language(lang_code)
except:
    logger.error("Failed to initialize translator.")
    raise


def _main(dest_dir: str, head_sha_output_path: str):
    repo_path = sparse_checkout()
    repo = Repo(repo_path)

    head_commit_sha = repo.head.commit.hexsha
    head_tree = repo.head.commit.tree[DEFAULTS.docs_dir]
    latest_commit_sha = read_commit_sha()
    latest_tree = repo.commit(latest_commit_sha).tree[DEFAULTS.docs_dir]

    logger.info("Handling diff %s...%s.",
                latest_commit_sha,
                head_commit_sha)

    translations = Translations(repo_path / DEFAULTS.docs_dir,
                                pathlib.Path(dest_dir),
                                TranslationCache(repo_path))

    forced = get_forced_filepaths(latest_commit_sha, lang_code)
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

    copy_git_dir(dest_dir)
    write_head_sha(head_commit_sha, head_sha_output_path)
    translations.complete()


if __name__ == "__main__":
    try:
        _main(sys.argv[1], sys.argv[2])
    except IndexError as e:
        logger.error("Error reading command-line arguments: %s", str(e))

        raise
