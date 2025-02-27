from .ordering import OrderedValue
from .apps import App, DocsApp


class Catalog:
    def __init__(self, disciplines, licenses, systems):
        self.__ordered = dict(disciplines=disciplines,
                              licenses=licenses,
                              systems=systems)
        self.__apps: [App] = []
        self.__disciplines = set()
        self.__licenses = set()
        self.__systems = set()
        self.__web_interfaces = set()

    def __iter__(self):
        for prop in ("apps",
                     "disciplines",
                     "licenses",
                     "systems",
                     "web_interfaces",
                     "alphabetical",
                     "by_discipline",
                     "by_license",
                     "by_availability"):
            yield (prop, getattr(self, prop))

    def __len__(self):
        return len(self.__apps)

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
            for app in [dict(app_obj)
                        for app_obj
                        in self.__sorted_apps]]}

    def __get_sort_key(self, order_by):
        return lambda value: OrderedValue(value, order_by)

    @property
    def apps(self):
        return [dict(app) for app in self.__sorted_apps if isinstance(app, DocsApp)]

    @property
    def disciplines(self):
        return sorted(self.__disciplines,
                      key=self.__get_sort_key(self.__ordered["disciplines"]))

    @property
    def licenses(self):
        return sorted(self.__licenses,
                      key=self.__get_sort_key(self.__ordered["licenses"]))

    @property
    def systems(self):
        return sorted(self.__systems,
                      key=self.__get_sort_key(self.__ordered["systems"]))

    @property
    def web_interfaces(self):
        return sorted(self.__web_interfaces,
                      key=self.__get_sort_key(self.__ordered["systems"]))

    @property
    def alphabetical(self):
        characters = set([app.name[0].lower() for app in self.__apps])
        return {char: [dict(app)
                       for app
                       in self.__sorted_apps
                       if app.name.lower().startswith(char)]
                for char
                in sorted(characters)}

    @property
    def by_discipline(self):
        return {discipline: [dict(app)
                             for app
                             in self.__sorted_apps
                             if discipline in app.disciplines]
                for discipline
                in self.disciplines}

    @property
    def by_license(self):
        return {license_type: [dict(app)
                               for app
                               in self.__sorted_apps
                               if license_type == app.license_type]
                for license_type
                in self.licenses}

    @property
    def by_availability(self):
        return {system: [dict(app)
                         for app
                         in self.__sorted_apps
                         if system in app.available_on]
                for system
                in self.systems}

    @property
    def by_web_availability(self):
        return {web_ui: [dict(app)
                         for app
                         in self.__sorted_apps
                         if web_ui in app.available_on.get("web_interfaces", [])]}
