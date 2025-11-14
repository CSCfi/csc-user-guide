from typing import Optional, Callable

from .ordering import OrderedValue
from .apps import App, DocsApp, AppendixApp
from .config import CatalogConfig


class Catalog:
    @staticmethod
    def is_exportable(app):
        attrs = ("unchecked", "warnings",)

        return not any(hasattr(app, attr) and bool(getattr(app, attr))
                       for attr in attrs)

    def __init__(self, config: CatalogConfig):
        self.__ordered = {key: (values
                                if all(type(value) is str for value in values)
                                else [value.get("name", "")
                                      for value
                                      in values
                                      if not value.get("fallback")])
                          for key, values
                          in config.listing_order.items()}
        self.__apps: list[App] = []
        self.__disciplines = set()
        self.__licenses = set()
        self.__systems = set()
        self.__web_interfaces = set()

    def __len__(self):
        return len(self.__apps)

    def asdict(self):
        props = ("apps",
                 "disciplines",
                 "licenses",
                 "systems",
                 "web_interfaces",
                 "alphabetical",
                 "by_discipline",
                 "by_license_type",
                 "by_availability",
                 "by_web_availability")

        return {attr_name: getattr(self, attr_name)
                for attr_name in dir(self)
                if attr_name in props}

    @property
    def __sorted_apps(self):
        return sorted(self.__apps, key=lambda app: app.name)

    def __collect_systems(self, availability):
        for item in availability:
            if isinstance(item, str):
                self.__systems.add(item)
            if isinstance(item, dict):
                self.__web_interfaces |= set(item.get("web_interfaces", []))

    def collect_app(self, app: App):
        self.__apps.append(app)
        self.__disciplines |= set(app.disciplines)
        self.__licenses |= set([app.license_type])
        self.__collect_systems(app.available_on)

    def export(self, props):
        return {"applications": [
            {prop: app[prop]
             for prop in props
             if prop in app and app[prop]}
            for app in [app_obj.asdict()
                        for app_obj
                        in self.__sorted_apps
                        if self.is_exportable(app_obj)]]}

    def __get_sort_key(self, order_by: list[str]) -> Callable[[str], OrderedValue]:
        return lambda value: OrderedValue(value, order_by)

    def __get_grouped_apps(self,
                           groups: list[str],
                           attr: str,
                           callback: Optional[Callable[[App, str], bool]]=None) -> dict:
        callback_fn = (callback if callback is not None
                       else lambda app, attr, value: (value in getattr(app, attr)
                                                      if hasattr(app, attr)
                                                      else False))

        return {item: [app.asdict()
                       for app
                       in self.__sorted_apps
                       if callback_fn(app, attr, item)]
                for item
                in groups}

    @property
    def unchecked(self) -> list[dict]:
        return [app.asdict() for app in self.__apps if app.unchecked]

    @property
    def appended(self) -> list[dict]:
        return [app.asdict() for app in self.__apps if isinstance(app, AppendixApp)]

    @property
    def disciplines(self) -> list[str]:
        return sorted(self.__disciplines,
                      key=self.__get_sort_key(self.__ordered["disciplines"]))

    @property
    def licenses(self) -> list[str]:
        return sorted(self.__licenses,
                      key=self.__get_sort_key(self.__ordered["license_types"]))

    @property
    def systems(self) -> list[str]:
        return sorted(self.__systems,
                      key=self.__get_sort_key(self.__ordered["systems"]))

    @property
    def web_interfaces(self) -> list[str]:
        return sorted(self.__web_interfaces,
                      key=self.__get_sort_key(self.__ordered["systems"]))

    @property
    def alphabetical(self) -> dict[str, list[dict]]:
        characters = set([app.name[0].lower() for app in self.__apps])
        startswith = lambda app, attr, value: (getattr(app, attr).lower().startswith(value))

        return self.__get_grouped_apps(sorted(characters),
                                       "name",
                                       callback=startswith)

    @property
    def by_discipline(self) -> dict[str, list[dict]]:
        return self.__get_grouped_apps(self.disciplines, "disciplines")

    @property
    def by_license_type(self) -> dict[str, list[dict]]:
        identity = lambda app, attr, value: (value == getattr(app, attr))

        return self.__get_grouped_apps(self.licenses,
                                       "license_type",
                                       callback=identity)

    @property
    def by_availability(self) -> dict[str, list[dict]]:
        return self.__get_grouped_apps(self.systems, "available_on")

    @property
    def by_web_availability(self) -> dict[str, list[dict]]:
        return self.__get_grouped_apps(self.web_interfaces, "available_on_web")
