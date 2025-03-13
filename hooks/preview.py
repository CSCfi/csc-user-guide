from pathlib import Path

from git import Repo
from mkdocs.plugins import get_plugin_logger


class PreviewHook:
    MKDOCS_HOOK_NAME = "preview-hook"
    ENVIRONMENT_KEY = "environment"
    PREVIEW_ENVIRONMENT = "preview"

    def __init__(self):
      self.environment = None
      self.startup_command = None
      self.logger = get_plugin_logger(self.MKDOCS_HOOK_NAME)
      self.head_sha = Repo(Path.cwd()).head.commit.hexsha

    @property
    def is_preview_build(self):
        return self.environment == self.PREVIEW_ENVIRONMENT and \
               self.startup_command == "build"

    def on_startup(self, command, dirty):
      self.startup_command = command
      return None

    def on_config(self, config):
        self.environment = config.extra[self.ENVIRONMENT_KEY]
        if self.is_preview_build:
            self.logger.info(f"preview build, commit {self.head_sha}")
        return None

    def on_page_markdown(self, markdown, page, config, files):
      if self.is_preview_build:
          page.meta["head_sha"] = self.head_sha
      return None


hook = PreviewHook()
on_startup = hook.on_startup
on_config = hook.on_config
on_page_markdown = hook.on_page_markdown
