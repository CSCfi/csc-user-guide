"""Base classes.
"""
from pathlib import Path

import yaml

from mkdocs.plugins import get_plugin_logger
from mkdocs.exceptions import PluginError


class DocsHook: # pylint: disable=too-few-public-methods
    """Base class for hooks.
    """
    HOOKS_DIR = "hooks"
    CONFIG_FILENAME = "config.yml"

    def __init__(self, *_, name=None, **__):
        try:
            assert name is not None, "Hook must have a name"
        except AssertionError as e:
            raise PluginError(str(e)) from e

        self._name = name
        self._logger = get_plugin_logger(f"{self._name}-hook")
        self._config_dict = self._get_config_dict(self._name)

    @property
    def plugin_events(self):
        """Returns a dict of MkDocs plugin events defined
        in (a subclass of) this hook.
        """
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
            with open(config_filepath, "rt", encoding="utf-8") as config_file:
                return yaml.safe_load(config_file)
        except FileNotFoundError:
            return None
