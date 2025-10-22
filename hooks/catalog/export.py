import json
from pathlib import Path
from typing import Union

import humps
from markdown.extensions.toc import slugify, unique as unique_slug

from .catalog import Catalog
from .config import CatalogConfig


class JSONExport:
    def __init__(self, catalog: Catalog, config: CatalogConfig):
        self.__catalog = catalog
        self.__props = config.export_props
        self.__filepath = config.export_filepath

    @property
    def __content(self):
        data = self.__catalog.export(self.__props)
        return json.dumps(humps.camelize(data))

    def write(self) -> None:
        with open(self.__filepath, "wt") as export_file:
            export_file.write(self.__content)


class DocsExport:
    """Class used for generating Markdown
    sources for the application index pages,
    i.e. 'docs/apps/{index,by_discipline,by_system}.md'
    ('by_license.md' still exists in the filesystem).

    When 'MKDOCS_ENV' is set to 'test', the sources
    are also written to disk for the test scripts
    to examine (see 'CatalogHook.on_post_build()' in
    'hooks/catalog/hook.py').
    """

    _markdown_stubs = {
        "by_system.md": """---
hide:
  - toc
---

# Applications by availability

Applications available on

- [Mahti](#mahti), CSC supercomputer for massively parallel jobs
- [Puhti](#puhti), CSC supercomputer for small and medium jobs
- [LUMI](#lumi), EuroHPC supercomputer for CPU and especially GPU jobs

Interactive web applications available on

- [Mahti web interface](#mahti-web-interface)
- [Puhti web interface](#puhti-web-interface)
- [LUMI web interface](#lumi-web-interface)


"""
    }

    def __init__(self, catalog: Catalog, config: CatalogConfig, lang_code="en"):
        self.__catalog = catalog
        self.__config = config
        self.__lang = lang_code
        self.__pages: dict[Path, str] = {}

    def __get_anchor_id(self, heading: str, ids: set) -> str:
        slug = unique_slug(slugify(heading, "-"), ids)
        ids.add(slug)

        return slug

    def __get_translation(self, group: str, key: tuple[str, str]) -> str:
        item_key, value = key

        group_en = self.__config.listing_order.get(group)
        for item in group_en:
            if item.get(item_key, "") == value:
                return item.get(f"{item_key}_{self.__lang}", "")

        return ""

    def __get_system_description(self, name: str):
        for system in self.__config.listing_order.systems:
            if system.get("name", "") == name:
                return (system.get("description", "")
                        if self.__lang == "en"
                        else system.get(f"description_{self.__lang}"))

    def __get_discipline_context(self) -> dict:
        ids = set()

        return [{"name": (discipline
                          if self.__lang == "en"
                          else self.__get_translation("disciplines", ("name", discipline))),
                 "id": self.__get_anchor_id(discipline, ids),
                 "apps": apps}
                for discipline, apps
                in self.__catalog.by_discipline.items()]

    def __get_systems_context(self) -> dict:
        pass

    def get_page_context(self, page) -> dict:
        contexts = {
            "index": dict(alphabetical=self.__catalog.alphabetical),
            "by_discipline": dict(by_discipline=self.__get_discipline_context()),
            "by_availability": dict(by_availability=self.__get_systems_context())
        }

        return contexts.get(Path(page.file.src_uri).stem, {})



    def __internal_link(self, app):
        uri_prefix = f"{Path(self.__config.export_filepath).parent.name}/"
        src_uri = app["page"].file.src_uri
        link_href = (f"./{src_uri.removeprefix(uri_prefix)}"
                     if src_uri.startswith(uri_prefix)
                     else f"/{src_uri}")
        link_name = (f"{app['name']} :material-arrow-right:"
                     if not link_href.startswith("./")
                     else app["name"])

        return f"[{link_name}]({link_href})"

    def __external_link(self, app):
        link_href = app["url"]
        link_name = f"{app['name']} :material-open-in-new:"
        return f"[{link_name}]({link_href}){{ target=_blank }}"

    def __app_link(self, app):
        description = app.get("description", "")
        app_description =  f" &mdash; {description}" if description else ""

        app_link = (self.__internal_link(app)
                    if app.get("page") is not None
                    else self.__external_link(app))

        return f"- {app_link}{app_description}\n"

    def __app_section(self, heading, apps: list[dict]):
        links = "\n".join(map(self.__app_link, apps))
        return (
            f"### {heading.upper() if len(heading) == 1 else heading}"
            f"\n{links}"
        )

    def __sections(self, app_group: dict):
        return "\n\n".join(self.__app_section(heading, apps) for heading,apps in app_group.items())

    def get_stub(self, filename: str) -> str:
        return self._markdown_stubs[filename]

    def add_page(self, filepath: Path, content: str):
        self.__pages[filepath] = content

    def append_by_system(self, markdown):
        sections = self.__sections(self.__catalog.by_availability)
        web_uis = {f"{system} web interface": apps for system,apps in self.__catalog.by_web_availability.items()}
        web_sections = self.__sections(web_uis)

        return "\n\n".join((markdown, sections, web_sections))

    # 'def export_by_license(self)' not needed.

    def append_content(self, filepath: Path, markdown) -> Union[str, None]:
        attr_name = f"append_{filepath.stem}"

        if hasattr(self, attr_name):
            method = getattr(self, attr_name)
            return method(markdown) if callable(method) else None


    def write_sources(self):
        for page_src, content in self.__pages.items():
            with open(page_src, "w") as src_file:
                src_file.write(content)
