import json
from pathlib import Path

import humps

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
        "index.md": """---
hide:
  - toc
---

# Applications

!!! default "Cannot find the application you are looking for?"
    * [See here for ways to install software yourself](../computing/installing.md).
    * You may also [contact CSC Service Desk](../support/contact.md) with your software
      installation request. Given enough requests, we may consider pre-installing a particular
      application, or purchasing a license for it if the software in question is proprietary.
    * Although we cannot promise to pre-install all requested applications, CSC Service Desk
      is happy to support you in installing software yourself.

- [By discipline](by_discipline.md)
- [By availability](by_system.md)
- [By license](by_license.md)


""",
        "by_discipline.md": """---
hide:
  - toc
---

# Applications by discipline

!!! default "Note"
    In addition to technical support, CSC also provides expert consulting in
    questions related to sciences and methods. For more details, see our
    [science-specific support pages at research.csc.fi](https://research.csc.fi/sciences)
    or directly [contact our Service Desk](../support/contact.md).

[TOC]


""",
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

    def __init__(self, catalog: Catalog, config: CatalogConfig):
        self.__catalog = catalog
        self.__config = config
        self.__pages: dict[Path, str] = {}

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

    def __alpha_toc_item(self, char):
        return f"- [{char.upper()}](#{char.lower()})\n"

    def __alpha_toc(self, app_group: dict) -> str:
        return f"""## Applications in alphabetical order

<div class="alpha-toc" markdown>

{"".join(self.__alpha_toc_item(char) for char in app_group.keys())}
</div>
"""

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

    def append_index(self, markdown):
        toc = self.__alpha_toc(self.__catalog.alphabetical)
        sections = self.__sections(self.__catalog.alphabetical)

        return "\n\n".join((markdown, toc, sections))

    def append_by_discipline(self, markdown):
        sections = self.__sections(self.__catalog.by_discipline)

        return "\n\n".join((markdown, sections))

    def append_by_system(self, markdown):
        sections = self.__sections(self.__catalog.by_availability)
        web_uis = {f"{system} web interface": apps for system,apps in self.__catalog.by_web_availability.items()}
        web_sections = self.__sections(web_uis)

        return "\n\n".join((markdown, sections, web_sections))

    # 'def export_by_license(self)' not needed.

    def append_content(self, filepath: Path, markdown) -> str | None:
        attr_name = f"append_{filepath.stem}"

        if hasattr(self, attr_name):
            method = getattr(self, attr_name)
            return method(markdown) if callable(method) else None


    def write_sources(self):
        for page_src, content in self.__pages.items():
            with open(page_src, "w") as src_file:
                src_file.write(content)
