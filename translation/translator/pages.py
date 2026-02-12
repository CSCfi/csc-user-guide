"""Module for handling pages according to Git diff.
"""
import re
import pathlib
import shutil
import string
import logging
from types import SimpleNamespace

from git import Diff

from .classes import PageTranslation, TranslationCache, FileWas, FileIs
from .utils import get_excluded_filepaths, mkparents


logger = logging.getLogger(__name__)


class NewTranslation(PageTranslation):
    """Subclass for pages in need of translation.
    """
    @classmethod
    def for_path(cls,
                 path: pathlib.Path,
                 src_prefix: pathlib.Path,
                 dest_prefix: pathlib.Path,
                 cache: TranslationCache):
        """Returns an instance of NewTranslation for 'path'.
        """
        return cls(SimpleNamespace(b_path=str(path)),
                                   src_prefix,
                                   dest_prefix,
                                   cache)

    def __init__(self,
                 diff_obj,
                 src_prefix,
                 dest_prefix,
                 cache):
        self.__path = diff_obj.b_path
        self.__src_path = src_prefix / diff_obj.b_path
        self.__dest_path = dest_prefix / diff_obj.b_path
        self.__cache = cache

    def __handle_cached(self):
        self.__cache.retrieve(self.path, self.__dest_path)

    @property
    def path(self) -> str:
        return self.__path

    @property
    def original(self) -> str:
        """The content of the source page.
        """
        return self.__src_path.read_text(encoding="utf-8")

    @property
    def pending_operation(self):
        return (self.__handle_cached
                if self.__cache.query(self.path) == FileIs.FRESH
                else None)

    def write_translation(self, translated_content: str):
        """Writes translation result to destination file.
        """
        mkparents(self.__dest_path)
        self.__dest_path.write_text(translated_content, encoding="utf-8")
        logger.info("Translation result written to '%s'.", self.path)
        self.__cache.store(self.path, self.__dest_path)


class MovedTranslation(PageTranslation):
    """Subclass for moved pages.
    """
    def __init__(self, diff_obj, prefix):
        self.__docs_src = diff_obj.rename_from
        self.__docs_dest = diff_obj.rename_to
        self.__src_path = prefix / diff_obj.rename_from
        self.__dest_path = prefix / diff_obj.rename_to
        self.__content = self.__src_path.read_text(encoding="utf-8")

    @property
    def path(self) -> str:
        return self.__docs_src

    def __handle_move(self):
        mkparents(self.__dest_path)
        self.__src_path.unlink(missing_ok=True, follow_symlinks=False)
        self.__dest_path.write_text(self.__content, encoding="utf-8")
        logger.info("Moved '%s' to '%s'.",
                    self.__docs_src,
                    self.__docs_dest)

    @property
    def pending_operation(self):
        return self.__handle_move


class DeletedTranslation(PageTranslation):
    """Subclass for deleted pages.
    """
    def __init__(self, diff_obj, prefix):
        self.__docs_src = diff_obj.a_path
        self.__dest_path = prefix / diff_obj.a_path

    @property
    def path(self) -> str:
        return self.__docs_src

    def __handle_delete(self):
        self.__dest_path.unlink(missing_ok=True)
        logger.info("Deleted '%s'.", self.path)

    @property
    def pending_operation(self):
        return self.__handle_delete


class SymlinkedTranslation(PageTranslation):
    """Subclass for symlinked pages.
    """
    def __init__(self, diff_obj, src_prefix, dest_prefix):
        self.__docs_src = diff_obj.b_path
        self.__src_path = src_prefix / diff_obj.b_path
        self.__dest_path = dest_prefix / diff_obj.b_path

    @property
    def path(self) -> str:
        return self.__docs_src

    def __handle_symlink(self):
        if self.__dest_path.is_symlink():
            self.__dest_path.unlink()

        mkparents(self.__dest_path)
        shutil.copy(self.__src_path, self.__dest_path, follow_symlinks=False)
        logger.info("Symlinked '%s'.", self.path)

    @property
    def pending_operation(self):
        return self.__handle_symlink


class Translations:
    """Processes Diff objects in need of translation.
    """
    def __init__(self,
                 src_prefix: pathlib.Path,
                 dest_prefix: pathlib.Path,
                 cache: TranslationCache):
        self.__src_prefix = src_prefix
        self.__dest_prefix = dest_prefix
        self.__translations: set[PageTranslation] = set()
        self.__excluded_files = get_excluded_filepaths(self.__src_prefix)
        self.__cache = cache

    def __iter__(self):
        yield from self.__pending_translation

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

    def __is_excluded(self, page_path):
        try:
            if any((self.__src_prefix / page_path).samefile(excluded)
                    for excluded in self.__excluded_files):
                logger.info("Ignored excluded file '%s'.", page_path)
                return True
            return False
        except FileNotFoundError:
            return False

    def __is_symlink(self, page_path):
        result = (self.__src_prefix / page_path).is_symlink()

        if result:
            logger.info("Found new symlink '%s'.", page_path)

        return result

    def __add_page(self, page, replace=False):
        if not self.__is_excluded(page.path):
            if replace:
                self.__translations.discard(page)
            self.__translations.add(page)

    def include(self, *sources: [Diff | pathlib.Path]) -> None:
        """Adds source pages for processing. Diff takes precedence over
        pathlib.Path if source describes the same page.
        """
        for src in sources:
            page = None

            if isinstance(src, Diff):
                diff_obj = src
                match diff_obj.change_type:
                    case FileWas.ADDED | FileWas.MODIFIED:
                        page = (SymlinkedTranslation(diff_obj,
                                                    self.__src_prefix,
                                                    self.__dest_prefix)
                                if self.__is_symlink(diff_obj.b_path)
                                else NewTranslation(diff_obj,
                                                    self.__src_prefix,
                                                    self.__dest_prefix,
                                                    self.__cache))

                    case FileWas.MOVED:
                        page = MovedTranslation(diff_obj, self.__dest_prefix)

                    case FileWas.DELETED:
                        page = DeletedTranslation(diff_obj, self.__dest_prefix)

                    case _:
                        continue

            elif isinstance(src, pathlib.Path):
                path_obj = src
                src_path = self.__src_prefix / path_obj

                if any((src_path.is_symlink(),
                        not src_path.is_file(),
                        not path_obj.name.endswith(".md"))):
                    continue

                page = NewTranslation.for_path(path_obj,
                                               self.__src_prefix,
                                               self.__dest_prefix,
                                               self.__cache)

            if page is not None:
                self.__add_page(page, replace=isinstance(src, Diff))

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
