import json
from pathlib import Path

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
    def __init__(self, catalog: Catalog, config: CatalogConfig):
        self.__catalog = catalog
        self.__config = config

    def __get_anchor_id(self, heading: str, ids: set) -> str:
        slug = unique_slug(slugify(heading, "-"), ids)
        ids.add(slug)

        return slug

    def __get_system_description(self, name: str) -> str:
        for system in self.__config.listing_order.systems:
            if system.get("name", "") == name:
                return system.get("description", "")

    def __get_alphabetical_context(self) -> tuple[list, set[str]]:
        ids = set()

        return ([{"name": letter,
                 "id": self.__get_anchor_id(letter, ids),
                 "apps": apps}
                for letter, apps
                in self.__catalog.alphabetical.items()],
                ids,)

    def __get_disciplines_context(self) -> tuple[list, set[str]]:
        ids = set()

        return ([{"name": discipline,
                 "id": self.__get_anchor_id(discipline, ids),
                 "apps": apps}
                for discipline, apps
                in self.__catalog.by_discipline.items()],
                ids,)

    def __get_systems_context(self) -> tuple[dict, set[str]]:
        ids = set()

        return (dict(on_systems=[{"name": system,
                                 "id": self.__get_anchor_id(system, ids),
                                 "description": self.__get_system_description(system),
                                 "apps": apps}
                                for system, apps
                                in self.__catalog.by_availability.items()],
                    on_web=[{"name": system,
                             "id": self.__get_anchor_id(f"{system} web interface", ids),
                             "apps": apps}
                            for system, apps
                            in self.__catalog.by_web_availability.items()]),
                ids,)

    def get_page_context(self, page) -> tuple[dict, set]:
        page_key = Path(page.file.src_uri).stem

        func_lookup = {
            "index": self.__get_alphabetical_context,
            "by_discipline": self.__get_disciplines_context,
            "by_availability": self.__get_systems_context
        }
        context, ids = func_lookup.get(page_key, lambda *_: ({},set()))()

        return (dict(catalog={page_key: context}),
                ids,)
