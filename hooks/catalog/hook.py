from classes import DocsHook
from .config import CatalogConfig
from .catalog import Catalog
from .apps import DocsApp, AppendixApp
from .export import JSONExport, DocsExport


class CatalogHook(DocsHook):

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.__catalog = \
            self.__context = \
                self.__export = \
                    self.__lang_code = None
        self.__appendix_lookup = {}
        self.__template_filename = ""

    def __init_catalog(self, config: CatalogConfig, lang_code="en") -> None:
        self.__catalog = Catalog(config)
        self.__lang_code = lang_code
        self.__context = DocsExport(self.__catalog, config, lang_code=lang_code)
        self.__export = JSONExport(self.__catalog, config)

        # Collect appendix apps that don't have a page in Docs
        for item in config.appendix:
            if item.doc.get("url") is not None:
                app = AppendixApp(item)
                self.__catalog.collect_app(app)

        # Set up a lookup table for collecting appendix apps
        self.__appendix_lookup = {item.doc["src"]: item
                                  for item
                                  in config.appendix
                                  if item.doc.get("src") is not None}

    def __handle_app_page(self, page) -> None:
        app = DocsApp(page, lang_code=self.__lang_code)

        for message in app.warnings:
            self._logger.warning(message)
        self.__catalog.collect_app(app)

    def __handle_appendix_page(self, meta, page) -> None:
        app = AppendixApp(meta, page=page)

        self.__catalog.collect_app(app)

    def __handle_index_page(self, page, ids: set) -> None:
        page.present_anchor_ids |= ids

    def __validate(self, config: CatalogConfig) -> None:
        warnings = config.validate()

        for key, warning in warnings:
            self._logger.warning(f"{key}: {warning}")

    def __handle_config(self, mkdocs_config) -> None:
        catalog_config = CatalogConfig(mkdocs_config, self._config_dict)
        language = mkdocs_config.theme.get("language", "en")

        self.__validate(catalog_config)
        self.__init_catalog(catalog_config, lang_code=language)
        self.__template_filename = catalog_config.index_template

    def __report_statistics(self) -> None:
        def report_number_of(name: str, apps: list):
            n_apps = len(apps)
            return f"{n_apps} {name}" if n_apps > 0 else None

        reports = [report_number_of(*collection)
                   for collection
                   in (("appended", self.__catalog.appended),
                       ("unchecked", self.__catalog.unchecked))]
        report_output = (f" ({', '.join(r for r in reports if r is not None)})"
                         if len(reports) > 0
                         else "")

        self._logger.info(
            f"{len(self.__catalog)} apps in Software catalog{report_output}"
        )

    def on_config(self, config):
        self.__handle_config(config)

        return None

    def on_page_markdown(self, markdown, page, config, files):
        if "catalog" in page.meta:
            self.__handle_app_page(page)
        elif (meta := self.__appendix_lookup.get(page.file.src_uri)) is not None:
            self.__handle_appendix_page(meta, page)

        return None

    def on_page_context(self, context, page, config, nav):
        if page.meta.get("template") == self.__template_filename:
            page_context, anchor_ids = self.__context.get_page_context(page)

            self.__handle_index_page(page, anchor_ids)
            return context | page_context
        else:
            return None

    def on_post_build(self, config):
        self.__export.write()

        return None

    def on_serve(self, *args, **kwargs):
        self.__report_statistics()
