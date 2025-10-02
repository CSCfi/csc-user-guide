from pathlib import Path
from collections import namedtuple

from git import Repo

from classes import DocsHook


PageStatus = namedtuple("PageStatus", "head, status")

class PreviewHook(DocsHook):
    MKDOCS_HOOK_NAME = "preview-hook"
    ENVIRONMENT_KEY = "environment"
    PREVIEW_ENVIRONMENT = "preview"

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        self.environment = None
        self.startup_command = None
        self.docs_dir = None
        self.cwd = Path.cwd()
        self.repo = Repo(self.cwd)

    def __get_status(self, page):
        untracked = [(self.cwd / u) for u in self.repo.untracked_files]
        modified = [(self.cwd / d.a_path) for d in self.repo.index.diff(None)]
        page_src_path = self.docs_dir / page.file.src_uri

        try:
            if any([page_src_path.samefile(untracked_path) for untracked_path in untracked]):
                return "untracked"
            elif any([page_src_path.samefile(modified_path) for modified_path in modified]):
                return "modified"
        except FileNotFoundError:
            pass

        return None

    @property
    def is_preview_build(self):
        return self.environment == self.PREVIEW_ENVIRONMENT and \
               self.startup_command in ("build", "serve")

    def on_startup(self, command, dirty):
        self.startup_command = command
        return None

    def on_config(self, config):
        self.environment = config.extra[self.ENVIRONMENT_KEY]
        self.docs_dir = Path(config.docs_dir)
        if self.is_preview_build:
            self._logger.info(f"preview build, commit {self.repo.head.commit.hexsha}")
        return None

    def on_page_context(self, context, page, config, nav):
        if self.is_preview_build and "page" in context:
            setattr(context["page"],
                    "git",
                    PageStatus(head=self.repo.head.commit.hexsha,
                               status=self.__get_status(page)))
            return context
        else:
            return None
