"""Provides utility functions
"""
import sys
import pathlib
import json
import re
import logging
from datetime import datetime

from . import DEFAULTS, LANG_CODE


logger = logging.getLogger(__name__)


def _has_lang_code(snapshot_paths):
    lang_suffix = f"/{DEFAULTS.docs_dir}/{LANG_CODE}"

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


def batch(iterable, n):
    """Yield successive n-sized batches from iterable.
    """
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]


def get_excluded_filepaths(src_prefix):
    """Returns a list of file paths, relative to src_prefix, read from
    __file__/../../exclude.txt.
    """
    module_path = pathlib.Path(__file__).parent
    excludes_path = module_path.parent / DEFAULTS.excludes_filename

    try:
        with excludes_path.open(mode="rt", encoding="utf-8") as excludes:
            paths = [line.strip()
                    for line
                    in excludes.readlines()
                    if not line.startswith("#")]

        return [pathlib.Path(src_prefix) / filepath
                for filepath
                in paths
                if filepath]
    except FileNotFoundError as e:
        logger.warning("Can't read list of excluded files: %s", str(e))

    return []


def read_commit_sha():
    """Returns the first tag that is a SHA-1 hash, i.e. a hexadecimal string 40
    characters in length, read from $CWD/snapshots.json produced by
    'restic snapshots' command.
    """
    json_file = pathlib.Path.cwd() / "snapshots.json"
    commit_sha = None

    try:
        with json_file.open(mode="rt", encoding="utf-8") as snapshot_json:
            commit_sha = _find_commit_sha(json.load(snapshot_json))

            assert commit_sha is not None, f"No SHA-1 found in {json_file}"
    except FileNotFoundError as e:
        logger.error("Can't read snapshots: %s", str(e))
        sys.exit(1)
    except AssertionError as e:
        logger.error("Can't find commit SHA: '%s'", str(e))
        sys.exit(1)

    return commit_sha


def _get_attrs(obj, attr_names):
    """Returns a dict of attributes listed in attr_names for obj.
    """
    return {attr: getattr(obj, attr)
            for attr
            in dir(obj)
            if attr in attr_names}


def md_filter(diff_obj):
    """Return True if diff_obj describes a Markdown file.
    """
    diff_attrs = _get_attrs(diff_obj, ("a_path", "b_path", "rename_to",))

    return any(d_path.lower().endswith(".md")
               for d_path
               in _get_attrs(diff_obj, diff_attrs).values()
               if isinstance(d_path, str))


def write_head_sha(head_sha, output_path: str):
    """Writes the head_sha into a file at output_path.
    """
    output_file = pathlib.Path(output_path)

    try:
        output_file.write_text(head_sha, encoding="utf-8")
        logger.info("HEAD commit SHA written into '%s'",
                    output_path)
    except FileNotFoundError as e:
        logger.error("Can't write HEAD commit SHA: %s", str(e))
        sys.exit(1)


def mkparents(path: pathlib.Path):
    """Creates parent directories for path.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
