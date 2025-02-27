from mkdocs.plugins import get_plugin_logger

from .catalog import Catalog
from .appendix import Appendix
from .config import SWCatalogConfig
from .apps import App, DocsApp, AppendixApp
from .exports import JSONExport


class SoftwareCatalogHook:
    def on_config(self, config):
        self.__config = SWCatalogConfig(config)
        self.__catalog = Catalog(self.__config.disciplines,
                                 self.__config.licenses,
                                 self.__config.systems)
        self.__appendix = Appendix(self.__config.appendix_srcpath)
        self.__export = JSONExport(self.__catalog,
                                   self.__config.exported_props)
        self.__logger = get_plugin_logger(self.__config.hook_name)

        for app in self.__appendix.external_apps:
            self.__catalog.collect_app(AppendixApp(app))

        return None

    def on_page_markdown(self, markdown, page, config, files):
        meta = page.meta.get(self.__config.meta_key)
        if meta is not None:
            try:
                app = DocsApp(meta, page)
                self.__catalog.collect_app(app)
            except AssertionError as warning:
                self.__logger.warning(warning)

        app = self.__appendix.internal_apps.get(page.file.src_uri)
        if app is not None:
            self.__catalog.collect_app(AppendixApp(app, page.canonical_url))

        return None

    def on_page_context(self, context, page, config, nav):
        return (context | {"catalog": dict(self.__catalog)}
                if page.meta.get("template") == self.__config.index_template
                else None)

    def on_post_build(self, config):
        with open(self.__config.export_filepath, "wt") as export_file:
            export_file.write(self.__export.content)
        return None

    def on_serve(self, *args, **kwargs):
        self.__logger.info(
            f"{len(self.__catalog)} apps in Software catalog"
        )
