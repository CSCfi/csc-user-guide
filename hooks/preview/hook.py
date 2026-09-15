import pathlib
import collections

import git

from classes import DocsHook


class PreviewHook(DocsHook):
    PageStatus = collections.namedtuple("PageStatus", "head, status")

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        self.__cwd = pathlib.Path.cwd()

        repo = git.Repo(self.__cwd)
        self.__headsha = repo.head.commit.hexsha
        self.__untracked = [(self.__cwd / u) for u in repo.untracked_files]
        self.__modified = [(self.__cwd / d.a_path) for d in repo.index.diff(None)]

    def __get_page_status(self, page_src_path):
        try:
            if any(page_src_path.samefile(untracked_path)
                   for untracked_path in self.__untracked):
                return "untracked"
            if any(page_src_path.samefile(modified_path)
                   for modified_path in self.__modified):
                return "modified"
        except FileNotFoundError:
            pass

        return None

    def on_pre_build(self, **_): # pylint: disable=missing-function-docstring
        self._logger.info("preview build%s, commit %s",
                          " (dirty)" if self._dirty else "",
                          self.__headsha)

    def on_config(self, config): # pylint: disable=missing-function-docstring
        setattr(config, "exclude_docs", None)

        return config

    def on_page_context(self, context, page, config, **_): # pylint: disable=missing-function-docstring
        if "page" in context:
            page_src_path = pathlib.Path(config.docs_dir) / page.file.src_uri

            setattr(context["page"],
                    "git",
                    self.PageStatus(head=self.__headsha,
                                    status=(self.__get_page_status(page_src_path)
                                            if self._startup_command == "serve"
                                            else None)))

            return context

        return None
