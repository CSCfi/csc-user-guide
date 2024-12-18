from math import inf
from string import Template

from mkdocs.exceptions import PluginError
from mkdocs.plugins import get_plugin_logger


class Order:
    def __init__(self, values):
        self.__ranks = {value.lower(): rank
                           for rank, value
                           in enumerate(values)}

    def __rank(self, value):
        return self.__ranks.get(str(value).lower(), inf)

    def less_than(self, this, that):
        return self.__rank(this) < self.__rank(that)


class OrderedValue:
    def __init__(self, value, order):
        self.__value = value
        self.__order = order

    def __lt__(self, other):
        return self.__order.less_than(self, other)

    def __str__(self):
        return self.__value


class App:
    def __init__(self, meta, page):
        app_meta = {key: value for key,
                    value in meta.items() if value is not None}
        self.name = app_meta.get("name", "")
        self.description = app_meta.get("description", "")
        self.license_type = app_meta.get("license_type", "")
        self.disciplines = app_meta.get("disciplines", [])
        self.available_on = app_meta.get("available_on", [])
        self.page = page

    def __iter__(self):
        for field in vars(self).items():
            yield field


class Catalog:
    LICENSE_TYPES = (
        "Free",
        "Academic",
        "Non-commercial",
    )
    LICENSE_ORDER = Order(LICENSE_TYPES)

    DISCIPLINES = (
        "Biosciences",
        "Chemistry",
        "Computational Engineering",
        "Data Analytics and Machine Learning",
        "Geosciences",
        "Language Research and Other Digital Humanities and Social Sciences",
        "Mathematics and Statistics",
        "Physics",
        "Quantum",
    )
    DISCIPLINE_ORDER = Order(DISCIPLINES)

    SYSTEMS = (
        "Puhti",
        "Mahti",
        "LUMI",
    )
    SYSTEM_ORDER = Order(SYSTEMS)

    def __init__(self):
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

    def check_app(self, app):
        def check_prop(prop, note):
            warning_template = \
                Template("Doc file '$src' is for an application, "
                         "but the YAML front matter does not include $missing.")
            src = app.page.file.src_uri
            assert len(prop) > 0, warning_template.substitute(
                src=src, missing=note)

        props = ((app.name, "the name of the app"),
                 (app.description, "a description for the app"),
                 (app.license_type, "a license type for the app"),
                 (app.disciplines, "disciplines for the app"),
                 (app.available_on, "availability information"))

        for prop, note in props:
            check_prop(prop, note)

    def collect_app(self, app: App):
        self.__apps.append(app)
        self.__disciplines |= set(app.disciplines)
        self.__licenses |= set([app.license_type])
        self.__systems |= set(filter(lambda elem: isinstance(elem, str),
                                     app.available_on))
        self.__web_interfaces |= set(next(iter(filter(lambda elem: isinstance(elem, dict),
                                                      app.available_on)), {})
                                     .get("web_interfaces", []))

    @property
    def apps(self):
        return [dict(app) for app in self.__sorted_apps]

    @property
    def disciplines(self):
        return sorted(self.__disciplines,
                      key=lambda discipline: OrderedValue(discipline, self.DISCIPLINE_ORDER))

    @property
    def licenses(self):
        return sorted(self.__licenses,
                      key=lambda license_type: OrderedValue(license_type, self.LICENSE_ORDER))

    @property
    def systems(self):
        return sorted(self.__systems,
                      key=lambda system: OrderedValue(system, self.SYSTEM_ORDER))

    @property
    def web_interfaces(self):
        return sorted(self.__web_interfaces,
                      key=lambda web_ui: OrderedValue(web_ui, self.SYSTEM_ORDER))

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


class SoftwareCatalogHook:
    MKDOCS_HOOK_NAME = "software-catalog-hook"

    def __init__(self):
        self.__logger = logger = get_plugin_logger(self.MKDOCS_HOOK_NAME)
        self.__catalog = Catalog()

    def on_config(self, config):
        try:
            sw_catalog_config = config.extra["sw_catalog"]
            self.__SW_CATALOG_INDEX_TEMPLATE = \
                f"{sw_catalog_config['templates_dir']}/apps-index.html"
            self.__SW_CATALOG_PAGE_META_KEY = \
                sw_catalog_config["page_meta_key"]
        except KeyError as error:
            raise PluginError(f"Software catalog misconfiguration: '{error}'")

    def on_page_markdown(self, markdown, page, config, files):
        entry = page.meta.get(self.__SW_CATALOG_PAGE_META_KEY)

        if entry is not None:
            app = App(entry, page)
            self.__catalog.collect_app(app)
            try:
                self.__catalog.check_app(app)
            except AssertionError as error:
                self.__logger.warning(error)
        return None

    def on_page_context(self, context, page, config, nav):
        template = page.meta.get("template")
        return (context | {"catalog": dict(self.__catalog)}
                if template == self.__SW_CATALOG_INDEX_TEMPLATE
                else None)

    def on_serve(self, *args, **kwargs):
        n_apps = len(self.__catalog)
        self.__logger.info(f"{n_apps} apps in Software catalog")


hook = SoftwareCatalogHook()
on_config = hook.on_config
on_page_markdown = hook.on_page_markdown
on_page_context = hook.on_page_context
on_serve = hook.on_serve
