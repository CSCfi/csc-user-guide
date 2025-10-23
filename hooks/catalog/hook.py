from pathlib import Path
from urllib.parse import urljoin

from mkdocs.plugins import get_plugin_logger, CombinedEvent, event_priority
from mkdocs.structure.files import File as MkDocsFile, InclusionLevel

from classes import DocsHook
from .config import CatalogConfig
from .catalog import Catalog
from .appendix import Appendix
from .apps import App, DocsApp, AppendixApp
from .export import JSONExport, DocsExport


class CatalogHook(DocsHook):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def on_config(self, config):
        self.__catalog_config = \
            CatalogConfig(config, self._config_dict)

        failed, warnings = self.__catalog_config.validate()

        for _, error in failed:
            self._logger.error(error)
        for _, warning in warnings:
            self._logger.warning(warning)

        self.__lang = config.theme.get("language", "en")
        self.__catalog = Catalog(self.__catalog_config)
        self.__appendix = Appendix(self.__catalog_config)
        self.__json_export = JSONExport(self.__catalog,
                                        self.__catalog_config)
        self.__docs_export = DocsExport(self.__catalog,
                                        self.__catalog_config, lang_code=self.__lang)

        for app_meta in self.__appendix.external_apps:
            self.__catalog.collect_app(AppendixApp(app_meta))

        return None

    def on_page_markdown(self, markdown, page, config, files):
        if (catalog_meta := page.meta.get("catalog")) is not None:
            app = DocsApp(catalog_meta, page, lang_code=self.__lang)

            for message in app.warnings:
                self._logger.warning(message)

            self.__catalog.collect_app(app)
        elif (app_meta := \
                  self.__appendix.internal_apps.get(
                        Path(config.docs_dir) / page.file.src_uri)
                    ) is not None:
            app_meta["page"] = page
            app = AppendixApp(app_meta, url=page.canonical_url)
            self.__catalog.collect_app(app)

        return None

    def on_page_context(self, context, page, config, nav):
        return (context | dict(catalog=self.__docs_export.get_page_context(page))
                if page.meta.get("template") == "apps-index.html"
                else None)

    def on_post_build(self, config):
        self.__json_export.write()

        return None

    def on_serve(self, *args, **kwargs):
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
