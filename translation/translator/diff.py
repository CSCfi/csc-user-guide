"""Handle diff change types.
"""
import logging

from .classes import FileWas, DiffPath
from .utils import get_excluded_filepaths


logger = logging.getLogger(__name__)


def handle_diff(git_diff, src_prefix, dest_prefix):
    """Iterate on diff objects and determine whether to translate, move or
    delete files.

    Returns an iterable of DiffPath objects for files that need translation.
    """

    excluded_files = get_excluded_filepaths(src_prefix)
    files_to_translate = []

    for diff_obj in git_diff:
        match diff_obj.change_type:
            case FileWas.ADDED|FileWas.MODIFIED:
                # In these cases, DiffPath source and destination look
                # identical without prefix...
                outdated_path = DiffPath(
                    diff_obj.b_path,
                    src_prefix / diff_obj.b_path,
                    diff_obj.b_path,
                    dest_prefix / diff_obj.b_path
                )

                if any(outdated_path.src.samefile(excluded) for excluded in excluded_files):
                    logger.info("Ignored excluded file '%s'", outdated_path.docs_src)
                    continue

                if outdated_path.src.is_symlink():
                    outdated_path.symlink()
                else:
                    files_to_translate.append(outdated_path)

            case FileWas.MOVED:
                # ...while, in this case, DiffPath the source and destination
                # prefixes are identical...
                moved_path = DiffPath(
                    diff_obj.rename_from,
                    dest_prefix / diff_obj.rename_from,
                    diff_obj.rename_to,
                    dest_prefix / diff_obj.rename_to
                )

                moved_path.move()

            case FileWas.DELETED:
                # ...and, in this case, there is no destination.
                deleted_path = DiffPath(
                    diff_obj.a_path,
                    dest_prefix / diff_obj.a_path
                )

                deleted_path.delete()

            case _:
                continue

    return files_to_translate
