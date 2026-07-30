"""Clear translation cache.
"""
import os
import sys
import logging

from translator.persistence import SwiftCache as TranslationCache
from translator.utils import check_environment


logger = logging.getLogger(__name__)

try:
    check_environment("LANG_CODE")

    LANG_CODE = os.getenv("LANG_CODE")
except:
    logger.error("Failed to initialize post-translation.")
    raise


def _main(cached_objs_path: str):
    try:
        failed = list(TranslationCache.clear_from_file(cached_objs_path))
    except AssertionError as e:
        logger.warning("Failed to clear cache: '%s'", str(e))

    if len(failed) > 0:
        for f in failed:
            logger.warning("Could not delete cached page '%s'.", f)


if __name__ == "__main__":
    try:
        _main(sys.argv[1])
    except IndexError as e:
        logger.error("Error reading command-line arguments: %s", str(e))

        raise
