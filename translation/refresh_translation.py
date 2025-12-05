#! /usr/bin/env python3
"""Refresh stale translation.
"""
import os
import sys
import pathlib
import logging

from git import Repo

from translator.api import translate_batch
from translator.diff import handle_diff
from translator.utils import (read_commit_sha,
                              md_filter,
                              get_diff,
                              write_head_sha,
                              batch)

logger = logging.getLogger(__name__)

# Get language code from environment
try:
    # Map language codes to language names
    languages = {
        "fi": "Finnish"
    }

    lang_code = os.environ["LANG_CODE"]
    LANGUAGE = languages[lang_code]
except KeyError:
    logger.error("Missing or invalid LANG_CODE in environment.")
    sys.exit(1)


def main(repo_dir: str, dest_dir: str, head_sha_output_path: str,
         docs_dir="docs", batch_size=8):
    """(Re-)translates Markdown files under repo_dir/docs_dir/, to language
    correspondig to lang_code, if they have been changed between the commit
    read from $CWD/snapshot.json and the HEAD of git repository in repo_dir.

    Translated Markdown files are placed in dest_dir, following the directory
    structure in repo_dir. The commit hash of repo_dir HEAD is written to
    head_sha_output_path.
    """
    git_repo = Repo(repo_dir)
    commit_sha = read_commit_sha()
    filtered_diff = filter(md_filter,
                           get_diff(git_repo, docs_dir, commit_sha))

    logger.info("Handling diff %s...%s",
                commit_sha,
                git_repo.head.commit.hexsha)

    files_to_translate = handle_diff(filtered_diff,
                                     pathlib.Path(repo_dir) / docs_dir,
                                     pathlib.Path(dest_dir))

    logger.info("%i files to translate", len(files_to_translate))

    for file_batch in batch(files_to_translate, n=batch_size):
        translate_batch(file_batch, LANGUAGE)

    write_head_sha(git_repo, head_sha_output_path)


if __name__ == "__main__":
    main(*sys.argv[1:])
