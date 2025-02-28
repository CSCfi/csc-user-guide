import yaml


class Appendix:
    def __init__(self, filepath: str):
        self.__appendix = \
            self.__get_appendix(filepath)["applications"]
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

    @staticmethod
    def __get_appendix(filepath):
        with open(filepath, "r") as appendix_file:
            appendix = yaml.safe_load(appendix_file)
            return appendix
