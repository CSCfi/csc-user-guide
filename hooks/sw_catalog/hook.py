from pathlib import Path

from .catalog import Catalog
from .appendix import Appendix
from .apps import App, DocsApp, AppendixApp
from .export import JSONExport


class SWCatalogHook:
    def __init__(self, sw_catalog_config, mkdocs_logger):
        self.__logger = mkdocs_logger
        self.__catalog = Catalog(sw_catalog_config.discipline_order,
                                 sw_catalog_config.license_type_order,
                                 sw_catalog_config.system_order)
        self.__appendix = Appendix(sw_catalog_config.appendix)
        self.__export = JSONExport(self.__catalog,
                                   ("name",
                                    "description",
                                    "license_type",
                                    "disciplines",
                                    "available_on",
                                    "url"))
        self.__export_subpath = sw_catalog_config.export_subpath

        for app in self.__appendix.external_apps:
            self.__catalog.collect_app(AppendixApp(app))

    def on_page_markdown(self, markdown, page, config, files):
        catalog_meta = page.meta.get("software_catalog")
        if catalog_meta is not None:
            try:
                app = DocsApp(catalog_meta, page)
                self.__catalog.collect_app(app)
            except AssertionError as warning:
                self.__logger.warning(warning)

        app = self.__appendix.internal_apps.get(page.file.src_uri)
        if app is not None:
            self.__catalog.collect_app(AppendixApp(app, page.canonical_url))

        return None

    def on_page_context(self, context, page, config, nav):
        return (context | {"catalog": dict(self.__catalog)}
                if page.meta.get("template") == "sw-catalog/apps-index.html"
                else None)

    def on_post_build(self, config):
        export_basepath = Path(config.site_dir)
        export_filepath = export_basepath / self.__export_subpath / "catalog.json"

        with open(export_filepath, "wt") as export_file:
            export_file.write(self.__export.content)

        return None

    def on_serve(self, *args, **kwargs):
        self.__logger.info(
            f"{len(self.__catalog)} apps in Software catalog"
        )
