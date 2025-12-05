"""Various classes
"""
import typing
import enum
import re
import pathlib
import string
import logging


logger = logging.getLogger(__name__)


class FileWas(enum.StrEnum):
    """Enum class for git diff change types.
    """
    ADDED = "A"
    MODIFIED = "M"
    MOVED = "R"
    DELETED = "D"


class DiffPath(typing.NamedTuple):
    """Path to a file that has been added, changed, moved or deleted since
    previous translation. String fields with names prefixed with 'docs_'
    are assumed to refer to paths under some docs_dir, while pathlib.Path
    fields should be assigned concrete paths. Provides methods for handling
    above cases and access to source file content as property.
    """
    docs_src: str
    src: pathlib.Path
    docs_dest: str = None
    dest: pathlib.Path = None

    @property
    def __has_destination(self):
        return all(
            (isinstance(self.dest, pathlib.Path),
             isinstance(self.docs_dest, str),)
        )

    def __mkparents(self):
        self.dest.parent.mkdir(parents=True, exist_ok=True)

    @property
    def original(self):
        """The content of the source file.
        """
        return self.src.read_text(encoding="utf-8")

    def write_translation(self, translated_content: str):
        """Write translation result to destination file or log a warning if
        destination path is not defined.
        """
        if self.__has_destination:
            self.__mkparents()

            self.dest.write_text(translated_content, encoding="utf-8")
            logger.info("Translation result written to '%s'", self.docs_dest)
        else:
            logger.warning("Attempted to write '%s' to undefined destination",
                           self.docs_src)

    def move(self):
        """Move previously translated file with unchanged content.
        """
        if self.__has_destination:
            self.__mkparents()

            self.src.move(self.dest)
            logger.info("Moved '%s' to '%s'", self.docs_src, self.docs_dest)
        else:
            logger.warning("Attempted to move '%s' to undefined destination",
                           self.docs_src)

    def delete(self):
        """Delete a previously translated file or a symlink.
        """
        self.src.unlink(missing_ok=True)
        logger.info("Deleted '%s'", self.docs_src)

    def symlink(self):
        """Copy a symlink from source to destination. If destination is
        symlink, i.e. it was modified, remove the existing symlink first.
        """
        if not self.src.is_symlink():
            logger.warning("Attempted to handle non-symlink '%s'")
            return

        if self.__has_destination:
            if self.dest.is_symlink():
                self.dest.unlink()

            self.__mkparents()
            self.src.copy(self.dest, follow_symlinks=False,
                                     preserve_metadata=True)
            logger.info("Copied symlink '%s'", self.docs_src)
        else:
            logger.warning(
                "Attempted to handle symlink '%s' with no destination",
                self.docs_src
            )


class ContentWrapper:
    """Wraps and unwraps a batch of DiffPath objects and their contents.
    """
    _wrapper_template = string.Template(
        "\n\n<!-- START:$file_key -->\n$content\n<!-- END:$file_key -->\n"
    )
    _extractor_pattern = r"<!-- START:(.*?) -->(.*?)<!-- END:\1 -->"

    def __init__(self, diff_paths):
        self.__diff_path_map = {}
        self.__combined_content = ""
        self.__translated_combined = ""

        for diff_path_obj in diff_paths:
            key = diff_path_obj.docs_src

            self.__combined_content += self._wrapper_template.substitute(
                file_key=key,
                content=diff_path_obj.original
            )

            self.__diff_path_map[key] = diff_path_obj

    def __len__(self):
        return len(self.__diff_path_map)

    def __str__(self):
        return self.__combined_content

    def __iter__(self):
        matches = re.findall(self._extractor_pattern,
                             self.__translated_combined,
                             re.DOTALL)

        for key, content in matches:
            yield (self.__diff_path_map.get(key), content,)

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
