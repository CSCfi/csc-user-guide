import re
from string import Template
from functools import reduce

from mkdocs.structure.pages import Page
from mkdocs.exceptions import PluginError


class App:
    def __init__(self, meta):
        self.unchecked = meta.get("unchecked", False)
        self.name = meta.get("name")
        self.description = meta.get("description", "")
        self.license_type = meta.get("license_type", "")
        self.disciplines = meta.get("disciplines", [])
        self.available_on = meta.get("available_on", [])

    def __attr_name(self, attr):
        pattern = re.compile(r"^_([A-Z][a-zA-Z]+)__(\w+)$")

        try:
            base, name = pattern.match(attr).group(1, 2)
            if base in ([b.__name__ for b in self.__class__.__bases__]
                        + [self.__class__.__name__]):
                return name
        except AttributeError:
            return attr

    def asdict(self):
        def excluded(attr):
            for name in ("unchecked", "warnings"):
                if attr.endswith(name):
                    return True
            return False

        return {self.__attr_name(attr): getattr(self, attr)
                for attr
                in vars(self)
                if not excluded(attr)}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise PluginError(
                "Every application in the Software Catalog must have a name"
            )
        self.__name = name


class DocsApp(App):
    WARNING_TEMPLATE = \
        Template("Doc file '$src' is for an application, "
                 "but the YAML front matter does not include $missing.")
    WARNING_NOTES = {
        "description": "a description for the app",
        "license_type": "a license type for the app",
        "disciplines": "disciplines for the app",
        "available_on": "availability information"
    }

    def __init__(self, meta: dict, page: Page):
        self.__warnings = []
        self.page = page
        self.url = page.canonical_url
        super().__init__(meta)

    def __check_property(self, prop_name, value):
        value_missing = value is None or len(value) < 1

        if value_missing and not self.unchecked:
            message = self.WARNING_TEMPLATE.substitute(
                src=self.page.file.src_uri,
                missing=self.WARNING_NOTES[prop_name]
            )

            self.__warnings.append(message)

    @property
    def warnings(self):
        return tuple(self.__warnings)

    @property
    def description(self):
        return self.__description

    @property
    def license_type(self):
        return self.__license_type

    @property
    def disciplines(self):
        return self.__disciplines

    @property
    def available_on(self):
        return self.__available_on

    @property
    def available_on_web(self):
        def reducer(systems, item):
            return ([*systems, *item.get("web_interfaces", [])]
                    if type(item) is dict
                    else systems)

        return reduce(reducer, self.__available_on, [])

    @description.setter
    def description(self, description):
        self.__check_property("description", description)
        self.__description = description if description is not None else ""

    @license_type.setter
    def license_type(self, license_type):
        self.__check_property("license_type", license_type)
        self.__license_type = license_type if license_type is not None else ""

    @disciplines.setter
    def disciplines(self, disciplines):
        self.__check_property("disciplines", disciplines)
        self.__disciplines = disciplines if disciplines is not None else []

    @available_on.setter
    def available_on(self, available_on):
        self.__check_property("available_on", available_on)
        self.__available_on = available_on if available_on is not None else []


class AppendixApp(App):
    def __init__(self, meta, url=None):
        super().__init__(meta)
        self.url = url if url is not None else meta.get("url")
