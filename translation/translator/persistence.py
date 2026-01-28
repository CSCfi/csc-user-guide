"""Keep track of cached translations.
"""
import os
import logging
import pathlib
import tempfile
import shutil
from functools import reduce
from itertools import chain, takewhile
from collections.abc import Iterable, Callable
from types import SimpleNamespace

from git import Repo
from swiftclient.service import SwiftService, SwiftError, SwiftUploadObject

from .constants import DEFAULTS
from .utils import check_environment, mkparents
from .classes import TranslationCache, CachePath, FileWas, FileIs


logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("swiftclient").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


def _restic_collision(swift_ns):
    restic_repo = os.getenv("RESTIC_REPOSITORY")
    if restic_repo is not None:
        collision = f":{swift_ns.cache_container}:/{swift_ns.cache_prefix}"
        return restic_repo.endswith(collision)
    return False


try:
    check_environment("LANG_CODE",
                      "OS_AUTH_URL",
                      "OS_APPLICATION_CREDENTIAL_ID",
                      "OS_APPLICATION_CREDENTIAL_SECRET",
                      "CACHE_CONTAINER",
                      "CACHE_PREFIX")

    SWIFT = SimpleNamespace(
        cache_container=os.getenv("CACHE_CONTAINER"),
        cache_prefix=os.getenv("CACHE_PREFIX"),
        service_opts={
            "auth_version": "3",
            "os_auth_type": "v3applicationcredential"
        },
        operation_opts={
            "prefix": f"{os.getenv('CACHE_PREFIX')}/{os.getenv('LANG_CODE')}"
        }
    )

    assert not _restic_collision(SWIFT), "Cache path collides with restic."
except:
    logger.error("Failed to initialize '%s'.", __name__)
    raise


class SwiftCache(TranslationCache):
    """Implements TranslationCache using python-swiftclient.
    """
    @staticmethod
    def __remove_prefix(path: str) -> str:
        return path.removeprefix(f"{SWIFT.operation_opts['prefix']}/")

    @staticmethod
    def __item_mapper(item: dict) -> str:
        return item.get("name", "")

    @staticmethod
    def __item_filter(item: dict) -> bool:
        return item.get("content_type") == "text/markdown"

    @classmethod
    def __upload_mapper(cls, upload: dict) -> str:
        return cls.__remove_prefix(upload.get("object", ""))

    @classmethod
    def __page_reducer(cls, listing: Iterable, page: dict) -> Iterable:
        if page.get("success"):
            return chain(listing,
                         filter(cls.__item_filter,
                                page.get("listing", [{}])))
        return listing

    @classmethod
    def __download_reducer(cls, downloads: Iterable, dl_obj: dict) -> Iterable:
        if dl_obj.get("success"):
            return chain(downloads, (dl_obj,))
        return downloads

    @classmethod
    def __upload_reducer(cls, uploads: Iterable, ul_obj: dict) -> Iterable:
        if ul_obj.get("success") and ul_obj.get("action") == "upload_object":
            return chain(uploads, (ul_obj,))
        return uploads

    @classmethod
    def __deletion_reducer(cls,
                           deletions: Iterable,
                           del_obj: dict) -> Iterable:
        if all((del_obj.get("success") is False,
                del_obj.get("action") == "delete_object",
                not del_obj.get("object", "").endswith("/"),)):
            return chain(deletions, (del_obj,))
        return deletions

    @classmethod
    def __to_reduced(cls,
                     result: Iterable,
                     reducer: Callable,
                     mapper: Callable|None=__item_mapper) -> map:
        return map(mapper,
                   reduce(reducer, result, iter(())))

    @staticmethod
    def __service() -> SwiftService:
        return SwiftService(options=SWIFT.service_opts)

    @staticmethod
    def __operation(method: Callable,
                    options: dict|None=None,
                    **kwargs) -> Iterable[dict]:
        container = SWIFT.cache_container
        options = SWIFT.operation_opts | (options or {})

        return method(container=container, options=options, **kwargs)

    @staticmethod
    def __new_upload(src_path: pathlib.Path,
                     name: str,
                     commit_sha: str|None=None) -> SwiftUploadObject:
        prefix = SWIFT.operation_opts["prefix"]
        name = (f"{prefix}/{commit_sha}/{name}"
                if commit_sha is not None
                else f"{prefix}/{name}")

        return SwiftUploadObject(str(src_path),
                                 object_name=name)

    def __init__(self, repo_path: pathlib.Path):
        self.__repo = Repo(repo_path)
        self.__head_sha = self.__repo.head.commit.hexsha
        self.__head_tree = self.__repo.head.commit.tree[DEFAULTS.docs_dir]
        self.__local_path = pathlib.Path(tempfile.mkdtemp())
        self.__cached_paths = tuple(self.__download_cache(self.__local_path))
        self.__added_paths = []

    def __del__(self):
        temp_path = pathlib.Path(tempfile.gettempdir())
        if self.__local_path.is_relative_to(temp_path):
            shutil.rmtree(self.__local_path)

    def __download_mapper(self, download: dict) -> CachePath:
        remote_path = download.get("object")
        commit_path = self.__remove_prefix(remote_path)
        commit_sha = "".join(takewhile(lambda c: c != "/", commit_path))

        return CachePath(
            remote=remote_path,
            local=pathlib.Path(download.get("path")),
            docs_src=commit_path.removeprefix(f"{commit_sha}/"),
            commit=self.__repo.commit(commit_sha)
        )

    def __download_cache(self,
                         output_path: pathlib.Path) -> Iterable[CachePath]:
        with self.__service() as swift:
            try:
                objects = self.__to_reduced(
                    self.__operation(swift.list),
                    self.__page_reducer
                )
                downloads = self.__to_reduced(
                    self.__operation(swift.download,
                                    options={"out_directory": output_path,
                                             "remove_prefix": True},
                                    objects=list(objects)),
                    self.__download_reducer,
                    mapper=self.__download_mapper
                )
                return downloads
            except SwiftError as e:
                logger.warning(
                    "Failed to download cached translations: %s",
                    str(e)
                )
                return iter(())

    def __put_file(self, docs_src: str, src_path: pathlib.Path) -> Iterable:
        with self.__service() as swift:
            try:
                file_upload = self.__new_upload(src_path,
                                                docs_src,
                                                commit_sha=self.__head_sha)
                uploads = self.__to_reduced(
                    self.__operation(swift.upload,
                                     objects=[file_upload]),
                    self.__upload_reducer,
                    mapper=self.__upload_mapper
                )

                self.__added_paths.append(file_upload.object_name)
                return uploads

            except SwiftError as e:
                logger.warning("Failed to cache '%s': %s", docs_src, str(e))
                return iter(())

    def __get_latest(self, docs_src: str) -> CachePath|None:
        paths = filter(lambda p: p.docs_src == docs_src, self.__cached_paths)

        return max(paths, key=lambda p: p.commit.committed_date, default=None)

    def __has_changed(self, path: CachePath) -> bool:
        diff_index = path.commit.tree[DEFAULTS.docs_dir].diff(self.__head_tree)

        for diff_obj in diff_index.iter_change_type(FileWas.MODIFIED):
            if diff_obj.b_path == path.docs_src:
                return True

        return False

    def __clear_cache(self) -> Iterable:
        with self.__service() as swift:
            try:
                objects = chain(
                    map(lambda path: path.remote, self.__cached_paths),
                    self.__added_paths
                )

                return self.__to_reduced(
                    self.__operation(swift.delete,
                                     objects=list(objects)),
                    self.__deletion_reducer
                )
            except SwiftError as e:
                logger.warning("Failed to clear cache: '%s'", str(e))
                return iter(())

    @property
    def count(self) -> int:
        return len(self.__cached_paths)

    def query(self, docs_src: str) -> FileIs:
        latest = self.__get_latest(docs_src)

        return (FileIs.MISSING
                if latest is None
                else (FileIs.STALE
                      if self.__has_changed(latest)
                      else FileIs.FRESH))

    def store(self, docs_src: str, from_path: pathlib.Path):
        for upload in self.__put_file(docs_src, from_path):
            path = self.__remove_prefix(upload)
            logger.info("Created cache entry '%s'.", path)

    def retrieve(self, docs_src: str, to_path: pathlib.Path):
        latest = self.__get_latest(docs_src)
        try:
            local_path = latest.local

            mkparents(to_path)
            shutil.copy(local_path, to_path)
            logger.info("Retrieved '%s' from cache.", docs_src)
        except AttributeError:
            logger.warning("No cache entry for '%s' found.", docs_src)
        except shutil.SameFileError:
            logger.warning("Retrieved file already '%s' exists.", docs_src)

    def clear(self):
        failed = list(self.__clear_cache())
        if len(failed) > 0:
            for f in failed:
                logger.warning("Failed to delete cached '%s'.", f)
        else:
            logger.info("Cache cleared for %s.", SWIFT.operation_opts.prefix)
