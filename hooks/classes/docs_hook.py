"""Base classes.
"""
import pathlib

import yaml

from properdocs.plugins import get_plugin_logger
from properdocs.exceptions import PluginError


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

        self._work_dir = pathlib.Path.cwd()
        self._startup_command = None
        self._dirty = None
        self.__modified = {}

    def _skip_if_clean(self, filepath, callback):
        mtime = filepath.stat().st_mtime_ns

        if not self._dirty or mtime > self.__modified.get(filepath, 0):
            callback()

            self.__modified[filepath] = mtime

    @property
    def plugin_events(self):
        """Returns a dict of ProperDocs plugin events defined
        in (a subclass of) this hook.
        """
        return {attr_name: getattr(self, attr_name)
                for attr_name in dir(self)
                if self._is_properdocs_plugin_event(attr_name)}

    def _is_properdocs_plugin_event(self, attr_name):
        return (attr_name.startswith("on_")
                and callable(getattr(self, attr_name)))

    @classmethod
    def _get_config_dict(cls, name):
        config_filepath = pathlib.Path.cwd() / cls.HOOKS_DIR / name / cls.CONFIG_FILENAME

        try:
            with open(config_filepath, "rt", encoding="utf-8") as config_file:
                return yaml.safe_load(config_file)
        except FileNotFoundError:
            return None

    def on_startup(self, command, dirty): # pylint: disable=missing-function-docstring
        self._startup_command = command

        if command == "serve":
            self._dirty = dirty
