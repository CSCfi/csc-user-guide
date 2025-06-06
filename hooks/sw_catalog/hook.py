from pathlib import Path

from mkdocs.plugins import get_plugin_logger, CombinedEvent, event_priority
from mkdocs.structure.files import File as MkDocsFile, InclusionLevel

from classes import DocsHook
from .config import get_config
from .catalog import Catalog
from .appendix import Appendix
from .apps import App, DocsApp, AppendixApp
from .export import JSONExport, DocsExport


class SWCatalogHook(DocsHook):
    def __init__(self, hook_name):
        self.__name = hook_name
        self.__logger = self.init_logger(hook_name)

    def on_config(self, config):
        catalog_config = get_config(config.docs_dir)
        catalog_config.load_dict(
            self.get_config_dict(self.__name)
        )
        failed, warnings = catalog_config.validate()

        for _, error in failed:
            self.__logger.error(error)
        for _, warning in warnings:
            self.__logger.warning(warning)

        self.__catalog = Catalog(catalog_config.listing_order)
        self.__appendix = Appendix(catalog_config.appendix)
        self.__json_export = JSONExport(self.__catalog,
                                        ("name",
                                         "description",
                                         "license_type",
                                         "disciplines",
                                         "available_on",
                                         "url")
                                        )
        self.__export_subpath = catalog_config.export_subpath
        self.__docs_export = DocsExport(self.__catalog)

        for app_meta in self.__appendix.external_apps:
            self.__catalog.collect_app(AppendixApp(app_meta))

        return None

    # Lower priority to avoid warning from mkdocs-redirects plugin
    @event_priority(50)
    def on_files(self, files, config):
        for filename in ("index.md", "by_discipline.md", "by_system.md"):
            src_uri = Path(self.__export_subpath) / filename
            stub = self.__docs_export[filename]
            file_obj = MkDocsFile.generated(config,
                                            src_uri,
                                            content=stub,
                                            inclusion=InclusionLevel.INCLUDED)
            files.append(file_obj)

        return files

    @event_priority(100)
    def _on_page_markdown_sooner(self, markdown, page, config, files):
        if (catalog_meta := page.meta.get("catalog")) is not None:
            app = DocsApp(catalog_meta, page)

            for message in app.warnings:
                self.__logger.warning(message)
            if app.name.lower() == "materialsstudio": self.__logger.error(app)
            self.__catalog.collect_app(app)
        elif (app_src := \
                  self.__appendix.internal_apps.get(page.file.src_uri)) is not None:
            app = AppendixApp(app_src, page.canonical_url)
            self.__catalog.collect_app(app)

        return None

    @event_priority(-100)
    def _on_page_markdown_later(self, markdown, page, config, files):
        def page_matches(filename):
            return Path(page.file.src_uri) == Path(self.__export_subpath) / filename

        if page_matches("index.md"):
            return self.__docs_export.append_alphabetical(markdown)
        elif page_matches("by_discipline.md"):
            return self.__docs_export.append_by_discipline(markdown)
        elif page_matches("by_system.md"):
            return self.__docs_export.append_by_system(markdown)
        else:
            return None

    on_page_markdown = CombinedEvent(_on_page_markdown_sooner,
                                     _on_page_markdown_later)

    # Not used for now.
    #
    # def on_page_context(self, context, page, config, nav):
    #     return (context | {"catalog": self.__catalog.asdict()}
    #             if page.meta.get("template") == "sw-catalog/apps-index.html"
    #             else None)

    def on_post_build(self, config):
        export_basepath = Path(config.site_dir)
        export_filepath = export_basepath / self.__export_subpath / "catalog.json"

        with open(export_filepath, "wt") as export_file:
            export_file.write(self.__json_export.content)

        return None

    def on_serve(self, *args, **kwargs):
        len_unchecked = len(self.__catalog.unchecked)
        n_unchecked = f" ({len_unchecked} unchecked)" if len_unchecked > 0 else ""

        self.__logger.info(
            f"{len(self.__catalog)} apps in Software catalog{n_unchecked}"
        )
