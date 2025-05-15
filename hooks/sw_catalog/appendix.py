class Appendix:
    def __init__(self, appendix):
        self.__appendix = appendix
        self.__internal_apps = {app["src"]: app
                                for app
                                in self.__appendix
                                if "src" in app}

    @property
    def internal_apps(self):
        return self.__internal_apps

    @property
    def external_apps(self):
        for app in self.__appendix:
            if "src" not in app:
                yield app
