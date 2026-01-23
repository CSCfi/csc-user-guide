"""Module for handling pages according to Git diff.
"""
import re
import pathlib
import shutil
import string
import logging

from .classes import TranslationCache, FileWas, FileIs, FileNeeds, DiffPath
from .utils import get_excluded_filepaths, mkparents


logger = logging.getLogger(__name__)


class PageTranslation:
    """Represents a documentation page to be translated, symlinked, deleted
    or moved.
    """
    def __init__(self,
                 diff_path: DiffPath,
                 operation: FileNeeds,
                 cache: TranslationCache):
        self.__docs_src = diff_path.docs_src
        self.__src_prefix = diff_path.src_prefix
        self.__docs_dest = diff_path.docs_dest
        self.__dest_prefix = diff_path.dest_prefix
        self.__op = (operation.value
                     if operation.value is None
                     else getattr(self, operation.value))
        self.__cache = cache

    @property
    def path(self) -> str:
        """Path of the page.
        """
        return self.__docs_src

    @property
    def src(self) -> pathlib.Path:
        """Concrete filesystem path where source is read from.
        """
        return self.__src_prefix / self.__docs_src

    @property
    def dest(self) -> pathlib.Path:
        """Concrete filesystem path where translation is written to.
        """
        return self.__dest_prefix / self.__docs_dest

    @property
    def original(self) -> str:
        """The content of the source file.
        """
        return self.src.read_text(encoding="utf-8")

    @property
    def pending_operation(self):
        """The callable operation to be performed for this instance.

        One of self.retrieve, self.move, self.delete, self.symlink or
        None, in which case the file is set to be translated.
        """
        return self.__op

    def write_translation(self, translated_content: str):
        """Writes translation result to destination file.
        """
        try:
            mkparents(self.dest)
            self.dest.write_text(translated_content, encoding="utf-8")
            logger.info("Translation result written to '%s'.", self.__docs_dest)
            self.__cache.store(self.__docs_src, self.dest)
        except TypeError:
            logger.warning(
                "Attempted to write '%s' to undefined destination.",
                self.__docs_src
            )

    def retrieve(self):
        """Retrieves cached translation and places it to destination.
        """
        try:
            self.__cache.retrieve(self.__docs_src, self.dest)
        except TypeError:
            logger.warning(
                "Attempted to retrieve '%s' with no destination.",
                self.__docs_src
            )

    def move(self):
        """Moves previously translated file with unchanged content.
        """
        try:
            mkparents(self.dest)
            self.src.move(self.dest)
            logger.info("Moved '%s' to '%s'.",
                        self.__docs_src,
                        self.__docs_dest)
        except TypeError:
            logger.warning(
                "Attempted to move '%s' to undefined destination.",
                self.__docs_src
            )

    def delete(self):
        """Deletes a previously translated file or a symlink.
        """
        self.src.unlink(missing_ok=True)
        logger.info("Deleted '%s'.", self.__docs_src)

    def symlink(self):
        """Copies a symlink from source to destination. If destination is
        symlink, i.e. it was modified, removes the existing symlink first.
        """
        try:
            if self.dest.is_symlink():
                self.dest.unlink()

            mkparents(self.dest)
            shutil.copy(self.src, self.dest, follow_symlinks=False)
            logger.info("Symlinked '%s'.", self.__docs_src)
        except TypeError:
            logger.warning(
                "Attempted to handle symlink '%s' with no destination.",
                self.__docs_src
            )


class Translations:
    """Processes Diff objects in need of translation.
    """
    def __init__(self,
                 src_prefix: pathlib.Path,
                 dest_prefix: pathlib.Path,
                 cache: TranslationCache):
        self.__src_prefix = src_prefix
        self.__dest_prefix = dest_prefix
        self.__translations: list[PageTranslation] = []
        self.__excluded_files = get_excluded_filepaths(self.__src_prefix)
        self.__cache = cache

        n_cached_files = self.__cache.count
        if n_cached_files > 0:
            logger.info("Found %i cached translations.", n_cached_files)

    def __iter__(self):
        yield from self.__pending_translation

    def __getitem__(self, key):
        return list(self.__pending_translation)[key]

    def __len__(self):
        return len(list(self.__pending_translation))

    @property
    def pending(self):
        """Filtered objects with pending operations other than translation.
        """
        return filter(lambda page: callable(page.pending_operation),
                      self.__translations)

    @property
    def __pending_translation(self):
        return filter(lambda page: not callable(page.pending_operation),
                      self.__translations)

    def __is_excluded(self, docs_src):
        return any((self.__src_prefix / docs_src).samefile(excluded)
                   for excluded in self.__excluded_files)

    def __new_diff_path(self, docs_src):
        return DiffPath(
            docs_src=docs_src,
            src_prefix=self.__src_prefix,
            docs_dest=docs_src,
            dest_prefix=self.__dest_prefix
        )

    def __handle_changed(self, diff_obj):
        if self.__is_excluded(diff_obj.b_path):
            logger.info("Ignored excluded file '%s'.", diff_obj.b_path)
            return

        if (self.__src_prefix / diff_obj.b_path).is_symlink():
            logger.info("Found new symlink '%s'.", diff_obj.b_path)
            self.__translations.append(
                PageTranslation(
                    self.__new_diff_path(diff_obj.b_path),
                    FileNeeds.LINKING,
                    self.__cache
                )
            )
            return

        operation = FileNeeds.TRANSLATION
        status = self.__cache.query(diff_obj.b_path)
        if status == FileIs.FRESH:
            operation = FileNeeds.RETRIEVAL
        elif status == FileIs.STALE:
            logger.info("Found stale cache entry for '%s'.", diff_obj.b_path)

        self.__translations.append(
            PageTranslation(
                self.__new_diff_path(diff_obj.b_path),
                operation,
                self.__cache
            )
        )

    def append(self, diff_obj):
        """Appends a diff_obj for processing.
        """
        match diff_obj.change_type:
            case FileWas.ADDED | FileWas.MODIFIED:
                self.__handle_changed(diff_obj)

            case FileWas.MOVED:
                moved_path = DiffPath(
                    docs_src=diff_obj.rename_from,
                    src_prefix=self.__dest_prefix,
                    docs_dest=diff_obj.rename_to,
                    dest_prefix=self.__dest_prefix
                )
                page = PageTranslation(moved_path,
                                       FileNeeds.RELOCATION,
                                       self.__cache)
                self.__translations.append(page)

            case FileWas.DELETED:
                deleted_path = DiffPath(
                    docs_src=diff_obj.a_path,
                    src_prefix=self.__dest_prefix
                )
                page = PageTranslation(deleted_path,
                                       FileNeeds.DELETION,
                                       self.__cache)
                self.__translations.append(page)

            case _:
                return

    def complete(self):
        """Signals for completion of the translation.
        """
        self.__cache.clear()


class PageContentWrapper:
    """Wraps and unwraps a batch of DiffPath objects and their contents.
    """
    _wrapper_template = string.Template(
        "\n\n<!-- START:$file_key -->\n$content\n<!-- END:$file_key -->\n"
    )
    _extractor_pattern = r"<!-- START:(.*?) -->(.*?)<!-- END:\1 -->"

    def __init__(self, pages: Translations):
        self.__page_map = {}
        self.__combined_content = ""
        self.__translated_combined = ""

        for page in pages:
            self.__combined_content += self._wrapper_template.substitute(
                file_key=page.path,
                content=page.original
            )

            self.__page_map[page.path] = page

    def __len__(self):
        return len(self.__page_map)

    def __str__(self):
        return self.__combined_content

    def __iter__(self):
        matches = re.findall(self._extractor_pattern,
                             self.__translated_combined,
                             re.DOTALL)

        for key, content in matches:
            yield (self.__page_map.get(key), content.lstrip(),)

    def is_empty(self):
        """Predicate for empty wrapper.
        """
        return not self.__combined_content.strip()

    @property
    def translation(self):
        """The raw combined translation result. Empty if not set.
        """
        return self.__translated_combined

    @translation.setter
    def translation(self, result):
        self.__translated_combined = result
