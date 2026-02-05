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


class FileNeeds(enum.Enum):
    """Types of pending operations for translations.
    """
    RETRIEVAL = "retrieve"
    RELOCATION = "move"
    DELETION = "delete"
    LINKING = "symlink"
    TRANSLATION = None


class FileIs(enum.Enum):
    """Status of cache query.
    """
    FRESH = "fresh"
    STALE = "stale"
    MISSING = False


class DiffPath(typing.NamedTuple):
    """Stores the filenames and paths for files found in Git diff.
    """
    docs_src: str
    src_prefix: pathlib.Path
    docs_dest: str = None
    dest_prefix: pathlib.Path = None


class CachePath(typing.NamedTuple):
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
    def store(self, docs_src: str, from_path: pathlib.Path):
        """Store a file at 'from_path' in the cache so that it can be retrieved
        later by referring to 'docs_src'.
        """

    @abstractmethod
    def retrieve(self, docs_src: str, to_path: pathlib.Path):
        """Retrieve the cached entry for 'docs_src' by placing the file to
        'to_path'.
        """

    @abstractmethod
    def clear(self):
        """Clear the cache for the currently processed language.
        """
