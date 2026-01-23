"""Translator for Markdown content.
"""
import os
import tempfile
import pathlib
import logging
from types import SimpleNamespace as ns


LANG_CODE_MAP = {
    "fi": "Finnish"
}
DEFAULTS = ns(
    docs_dir="docs",
    excludes_filename="exclude.txt",
    batch_size=4,
    source_language="English",
    openai=ns(
        model="gpt-5",
        max_tokens=128000, # https://platform.openai.com/docs/models/gpt-5
        max_tokens_multiplier=1.1,
        timeout=10.0,
        retries=5
    ),
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def _restic_collision(swift_ns):
    restic_repo = os.getenv("RESTIC_REPOSITORY")
    if restic_repo is not None:
        collision = f":{swift_ns.cache_container}:/{swift_ns.cache_prefix}"
        return restic_repo.endswith(collision)
    return False


try:
    for var_name in ("LANG_CODE",
                     "CACHE_CONTAINER",
                     "CACHE_PREFIX",
                     "REPO_ORG",
                     "REPO_NAME",
                     "REPO_BRANCH",):
        assert var_name in os.environ, f"{var_name} not found in environment"

    LANG_CODE = os.getenv("LANG_CODE")
    TARGET_LANGUAGE = LANG_CODE_MAP[LANG_CODE]
    GIT = ns(
        work_path=pathlib.Path(tempfile.mkdtemp()),
        service="github.com",
        repo=ns(
            org=os.getenv("REPO_ORG"),
            name=os.getenv("REPO_NAME"),
            branch=os.getenv("REPO_BRANCH")
        )
    )
    SWIFT = ns(
        cache_container=os.getenv("CACHE_CONTAINER"),
        cache_prefix=os.getenv("CACHE_PREFIX"),
        service_opts={
            "auth_version": "3",
            "os_auth_type": "v3applicationcredential"
        },
        operation_opts={
            "prefix": f"{os.getenv('CACHE_PREFIX')}/{LANG_CODE}"
        }
    )

    assert not _restic_collision(SWIFT), "Cache path collides with restic"
except:
    logger.error("Failed to initialize translator.")
    raise
