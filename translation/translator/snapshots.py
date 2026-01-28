"""Provides functions for handling restic snapshot metadata.
"""
import os
import re
import pathlib
import json
import logging
from datetime import datetime

from .constants import DEFAULTS
from .utils import check_environment


logger = logging.getLogger(__name__)


try:
    check_environment("LANG_CODE")
except:
    logger.error("Failed to initialize '%s'.", __name__)
    raise


def _has_lang_code(snapshot_paths):
    lang_suffix = f"/{DEFAULTS.docs_dir}/{os.getenv('LANG_CODE')}"

    for path in snapshot_paths:
        if path.endswith(lang_suffix):
            return True

    return False


def _snapshot_path_filter(snapshot):
    return _has_lang_code(snapshot.get("paths", []))


def _is_sha1_hash(tag):
    return re.match("^[0-9a-f]{40}$", tag, re.IGNORECASE) is not None


def _snapshot_datetime(snapshot):
    isotime = snapshot.get("time", datetime.min.isoformat())
    return datetime.fromisoformat(isotime)


def _find_commit_sha(snapshots):
    lang_snapshots = filter(_snapshot_path_filter, snapshots)
    for snapshot in sorted(lang_snapshots, key=_snapshot_datetime):
        for tag in snapshot.get("tags", []):
            if _is_sha1_hash(tag):
                return tag

    return None


def read_commit_sha():
    """Returns the first tag that is a SHA-1 hash, i.e. a hexadecimal string 40
    characters in length, read from $CWD/snapshots.json produced by
    'restic snapshots' command.
    """
    json_file = pathlib.Path.cwd() / DEFAULTS.snapshots_filename
    commit_sha = None

    try:
        with json_file.open(mode="rt", encoding="utf-8") as snapshot_json:
            commit_sha = _find_commit_sha(json.load(snapshot_json))

            assert commit_sha is not None, f"No SHA-1 found in {json_file}"
    except FileNotFoundError:
        logger.error("Can't read snapshots.")
        raise
    except AssertionError:
        logger.error("Can't find commit SHA.")
        raise

    return commit_sha


def write_head_sha(head_sha, output_path: str):
    """Writes the head_sha into a file at output_path.
    """
    output_file = pathlib.Path(output_path)

    try:
        output_file.write_text(head_sha, encoding="utf-8")
        logger.info("HEAD commit SHA written into '%s'", output_path)
    except:
        logger.error("Can't write HEAD commit SHA.")
        raise
