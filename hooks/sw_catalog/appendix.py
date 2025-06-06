class Appendix:
    def __init__(self, appendix: list):
        self.__appendix = appendix
        self.__internal_apps = {app["src"]: app
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
