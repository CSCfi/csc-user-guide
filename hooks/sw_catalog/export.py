import json

import humps

from .catalog import Catalog


class JSONExport:
    def __init__(self, catalog: Catalog, props):
        self.__catalog = catalog
        self.__props = props

    @property
    def content(self):
        data = self.__catalog.export(self.__props)
        return json.dumps(humps.camelize(data))


class DocsExport:
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
    @staticmethod
    def app_link(app):
        description = app.get("description", "")
        app_description =  f" &mdash; {description}" if description else ""
        app_name, app_url =  ((app["name"], app["page"].file.src_uri.removeprefix("apps/"))
                              if "page" in app
                              else (f"{app['name']} :material-open-in-new:", app["url"]))

        return f"- [{app_name}]({app_url}){app_description}\n"

    @staticmethod
    def alpha_toc_item(char):
        return f"- [{char.upper()}](#{char.lower()})\n"

    @classmethod
    def alpha_toc(cls, app_group: dict) -> str:
        return f"""## Applications in alphabetical order

<div class="alpha-toc" markdown>

{"".join(cls.alpha_toc_item(char) for char in app_group.keys())}
</div>
"""

    @classmethod
    def app_section(cls, heading, apps: list[dict]):
        links = "\n".join(map(cls.app_link, apps))
        return (
            f"### {heading.upper() if len(heading) == 1 else heading}"
            f"\n{links}"
        )

    @classmethod
    def sections(cls, app_group: dict):
        return "\n\n".join(cls.app_section(heading, apps) for heading,apps in app_group.items())

    def __init__(self, catalog: Catalog):
        self.__catalog = catalog

    def __getitem__(self, key):
        return self._markdown_stubs[key]

    def append_alphabetical(self, markdown):
        toc = self.alpha_toc(self.__catalog.alphabetical)
        sections = self.sections(self.__catalog.alphabetical)

        return "\n\n".join((markdown, toc, sections))

    def append_by_discipline(self, markdown):
        sections = self.sections(self.__catalog.by_discipline)

        return "\n\n".join((markdown, sections))

    def append_by_system(self, markdown):
        sections = self.sections(self.__catalog.by_availability)
        web_uis = {f"{system} web interface": apps for system,apps in self.__catalog.by_web_availability.items()}
        web_sections = self.sections(web_uis)

        return "\n\n".join((markdown, sections, web_sections))

    # 'def export_by_license(self)' not needed.
