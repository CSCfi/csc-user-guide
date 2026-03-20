"""Class definitions for the translator.
"""
import enum
import pathlib
from abc import ABC, abstractmethod
from typing import overload, NamedTuple, Callable

from git import Commit, Diff


class FileWas(enum.StrEnum):
    """Git diff change types.
    """
    ADDED = "A"
    COPIED = "C"
    DELETED = "D"
    MODIFIED = "M"
    MOVED = "R"
    RETYPED = "T"


class FileIs(enum.Enum):
    """Status of cache query.
    """
    FRESH = "fresh"
    STALE = "stale"
    MISSING = False


class CachePath(NamedTuple):
    """Stores the remote, local and docs_dir-related filepaths along with the
    Git commit object.
    """
    remote: str
    local: pathlib.Path
    docs_src: str
    commit: Commit


class TranslationCache(ABC):
    """Store and retrieve translations from a cache.
    """
    @property
    @abstractmethod
    def count(self) -> int:
        """Returns the number of cache records.
        
        Does not necessarily reflect the state of the cache after changes.
        """

    @abstractmethod
    def query(self, docs_src: str) -> FileIs:
        """Check if 'docs_src' is fresh, stale or does not exist in cache.

        Does not necessarily reflect the state of the cache after changes.
        """

    @abstractmethod
    def store(self, docs_src: str, from_path: pathlib.Path) -> None:
        """Store a file at 'from_path' in the cache so that it can be retrieved
        later by referring to 'docs_src'.
        """

    @abstractmethod
    def retrieve(self, docs_src: str, to_path: pathlib.Path) -> None:
        """Retrieve the cached entry for 'docs_src' by placing the file to
        'to_path'.
        """

    @abstractmethod
    def clear(self) -> None:
        """Clear the cache for the currently processed language.
        """


class PageTranslation(ABC):
    """Represents a documentation page to be translated, retrieved from cache,
    symlinked, deleted or moved. Two PageTranslation objects compare equal if
    they have the same path.
    """
    @overload
    @abstractmethod
    def __init__(self,
                 diff_obj: Diff,
                 src_prefix: pathlib.Path,
                 dest_prefix: pathlib.Path,
                 cache: TranslationCache):
        ...

    @overload
    @abstractmethod
    def __init__(self,
                 diff_obj: Diff,
                 src_prefix: pathlib.Path,
                 dest_prefix: pathlib.Path):
        ...

    @overload
    @abstractmethod
    def __init__(self,
                 diff_obj: Diff,
                 prefix: pathlib.Path):
        ...

    def __eq__(self, other) -> bool:
        return (self.path == other.path
                if issubclass(type(other), PageTranslation)
                else NotImplemented)

    def __hash__(self):
        return hash(self.path)

    @property
    @abstractmethod
    def path(self) -> str:
        """Path of the page."""

    @property
    @abstractmethod
    def pending_operation(self) -> Callable | None:
        """The callable operation to be performed for this instance. If None,
        the page is to be translated.
        """
