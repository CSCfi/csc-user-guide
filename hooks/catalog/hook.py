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

        self.__index_filenames = \
            ("by_system.md",)

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

    # Lower priority to avoid warning from mkdocs-redirects plugin
    @event_priority(50)
    def on_files(self, files, config):
        for filename in self.__index_filenames:
            base_uri = Path(self.__catalog_config.export_filepath).parent
            src_uri = base_uri.relative_to(config.site_dir) / filename
            stub = self.__docs_export.get_stub(filename)

            file_obj = MkDocsFile.generated(config,
                                            src_uri,
                                            content=stub,
                                            inclusion=InclusionLevel.INCLUDED)

            if files.get_file_from_path(src_uri) is not None:
                files.remove(file_obj)

            files.append(file_obj)

        return files

    @event_priority(100)
    def _on_page_markdown_sooner(self, markdown, page, config, files):
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

    @event_priority(-100)
    def _on_page_markdown_later(self, markdown, page, config, files):
        src_uri = page.file.src_uri
        filepath = Path(src_uri)
        dirname, *segments = filepath.parts

        if (dirname == "apps"
            and len(segments) == 1
            and segments[0] in self.__index_filenames):

            # For now, set 'edit_url' to point to the Python module
            # responsible for generating the apps index pages:
            page.edit_url = urljoin(config.repo_url, "edit/master/hooks/catalog/export.py")

            content = self.__docs_export.append_content(filepath, markdown)
            self.__docs_export.add_page(Path(config.docs_dir) / dirname / filepath.name, content)

            return content

        else:
            return None

    on_page_markdown = CombinedEvent(_on_page_markdown_sooner,
                                     _on_page_markdown_later)

    def on_page_context(self, context, page, config, nav):
        return (context | dict(catalog=self.__docs_export.get_page_context(page))
                if page.meta.get("template") == "apps-index.html"
                else None)

    def on_post_build(self, config):
        self.__json_export.write()

        if config.extra.get("environment") == "test":
            self.__docs_export.write_sources()

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
