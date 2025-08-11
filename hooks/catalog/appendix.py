from pathlib import Path

from .config import CatalogConfig


class Appendix:
    def __init__(self, config: CatalogConfig):
        self.__appendix = config.appendix
        self.__internal_apps = {Path(app["src"]): app
                                for app
                                in self.__appendix
                                if app.get("src") is not None}

    @property
    def internal_apps(self):
        return self.__internal_apps

    @property
    def external_apps(self):
        for app in self.__appendix:
            if not app.get("src"):
                yield app
