import yaml
from pathlib import Path

from mkdocs.plugins import get_plugin_logger


class DocsHook:
    @property
    def plugin_events(self):
        return {attr_name: getattr(self, attr_name)
                for attr_name in dir(self)
                if self._is_mkdocs_plugin_event(attr_name)}

    def _is_mkdocs_plugin_event(self, attr_name):
        return (attr_name.startswith("on_")
                and callable(getattr(self, attr_name)))

    @staticmethod
    def get_config_dict(hook_name):
        config_filepath = Path.cwd() / "hooks" / hook_name / "config.yml"

        with open(config_filepath, "r") as config_file:
            return yaml.safe_load(config_file)

    @staticmethod
    def init_logger(hook_name):
        return get_plugin_logger(f"{hook_name}-hook")
