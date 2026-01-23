#! /usr/bin/env python3
"""Clone and checkout git repository.
"""
import logging
import pathlib
import shutil

from git import Git

from . import DEFAULTS, GIT


logger = logging.getLogger(__name__)


def _get_clone_path():
    url = f"https://{GIT.service}/{GIT.repo.org}/{GIT.repo.name}.git"

    logger.info("Cloning %s", url)

    Git(working_dir=GIT.work_path).clone(
        "--filter=blob:none",
        "--no-checkout",
        url
    )

    return GIT.work_path / GIT.repo.name


def sparse_checkout():
    """Sparse checkout files for translation. Returns path to the clone.
    """
    clone_path = _get_clone_path()
    glob = f"/{DEFAULTS.docs_dir}/**/*.md"

    logger.info("Branch '%s', sparse checkout: '%s'.", GIT.repo.branch, glob)

    g = Git(working_dir=clone_path)
    g.sparse_checkout("init", "--no-cone")
    g.sparse_checkout("set", glob)
    g.checkout(GIT.repo.branch)

    return clone_path


def copy_git_dir(destination: str):
    """Copy the cloned .git directory to parent of destination.
    """
    src = (GIT.work_path / GIT.repo.name) / ".git"
    dest = pathlib.Path(destination).parent / ".git"
    shutil.copytree(src, dest, symlinks=False)
