#! /usr/bin/env python3
"""Clone and checkout git repository.
"""
import os
import logging
import pathlib
import shutil
import tempfile
from types import SimpleNamespace

from git import Git

from .constants import DEFAULTS
from .utils import check_environment


logger = logging.getLogger(__name__)

try:
    check_environment("REPO_ORG", "REPO_NAME", "REPO_BRANCH")

    GIT = SimpleNamespace(
        work_path=pathlib.Path(tempfile.mkdtemp()),
        service="github.com",
        repo=SimpleNamespace(
            org=os.getenv("REPO_ORG"),
            name=os.getenv("REPO_NAME"),
            branch=os.getenv("REPO_BRANCH")
        )
    )
except:
    logger.error("Failed to initialize '%s'.", __name__)
    raise


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
