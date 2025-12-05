"""Provides utility functions
"""
import sys
import pathlib
import json
import re
import logging


logger = logging.getLogger(__name__)


def batch(iterable, n):
    """Yield successive n-sized batches from iterable.
    """
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]


def get_excluded_filepaths(src_prefix):
    """Returns a list of file paths, relative to src_prefix, read from
    __file__/../exclude.txt.
    """
    excludes_path = pathlib.Path(__file__).parent.parent / "exclude.txt"

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
        logger.error("Can't read list of excluded files: %s", str(e))
        sys.exit(1)


def read_commit_sha():
    """Returns the first tag that is a SHA-1 hash, i.e. a hexadecimal string 40
    characters in length, read from $CWD/snapshots.json produced by
    'restic snapshots' command.
    """
    json_file = pathlib.Path.cwd() / "snapshots.json"
    commit_sha = None

    try:
        with json_file.open(mode="rt", encoding="utf-8") as snapshot_json:
            for snapshot in json.load(snapshot_json):
                for tag in snapshot.get("tags", []):
                    if re.match(r"[0-9a-f]{40}", tag) is not None:
                        commit_sha = tag
                        break
    except FileNotFoundError as e:
        logger.error("Can't read snapshots: %s", str(e))
        sys.exit(1)

    return commit_sha


def get_attrs(obj, attr_names):
    """Returns a dict of attributes listed in attr_names for obj.
    """
    return {attr: getattr(obj, attr)
            for attr
            in dir(obj)
            if attr in attr_names}


def md_filter(diff_obj):
    """Returns true if diff_obj looks like it is for a Markdown file.
    """
    diff_attrs = get_attrs(diff_obj, ("a_path", "b_path", "rename_to",))

    return any(d_path.lower().endswith(".md")
               for d_path
               in get_attrs(diff_obj, diff_attrs).values()
               if isinstance(d_path, str))


def write_head_sha(git_repo, output_path: str):
    """Writes the HEAD commit hash for git_repo into the file at
    output_path.
    """
    output_file = pathlib.Path(output_path)

    try:
        output_file.write_text(git_repo.head.commit.hexsha, encoding="utf-8")
        logger.info("HEAD commit SHA written into '%s'",
                    output_path)
    except FileNotFoundError as e:
        logger.error("Can't write HEAD commit SHA: %s", str(e))
        sys.exit(1)


def get_diff(git_repo, docs_dir: str, commit_sha: str):
    """Returns a git diff in git_repo between commit_sha and HEAD,
    with only files under docs_dir considered.
    """
    latest_translation = git_repo.commit(commit_sha).tree[docs_dir]
    current_state = git_repo.head.commit.tree[docs_dir]

    return latest_translation.diff(current_state)
