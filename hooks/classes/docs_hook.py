import yaml
from pathlib import Path

from mkdocs.plugins import get_plugin_logger
from mkdocs.exceptions import PluginError


class DocsHook:
    HOOKS_DIR = "hooks"
    CONFIG_FILENAME = "config.yml"

    def __init__(self,
                 *args,
                 name=None,
                 **kwargs):
        try:
            assert name is not None
        except AssertionError:
            raise PluginError("Hook must have a name")

        self._name = name
        self._logger = get_plugin_logger(f"{self._name}-hook")
        self._config_dict = self._get_config_dict(self._name)

    @property
    def plugin_events(self):
        return {attr_name: getattr(self, attr_name)
                for attr_name in dir(self)
                if self._is_mkdocs_plugin_event(attr_name)}

    def _is_mkdocs_plugin_event(self, attr_name):
        return (attr_name.startswith("on_")
                and callable(getattr(self, attr_name)))

    @classmethod
    def _get_config_dict(cls, name):
        config_filepath = Path.cwd() / cls.HOOKS_DIR / name / cls.CONFIG_FILENAME

        try:
            with open(config_filepath, "r") as config_file:
                return yaml.safe_load(config_file)
        except FileNotFoundError:
            return None
