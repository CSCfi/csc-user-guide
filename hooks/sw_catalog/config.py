from mkdocs.config import base, config_options as c
from mkdocs.config.defaults import MkDocsConfig


class _AppendixItem(base.Config):
    name = c.Type(str)
    description = c.Type(str)
    disciplines = c.ListOfItems(c.Type(str))
    src = c.Optional(c.File(exists=True))
    url = c.Optional(c.URL())


class SWCatalogConfig(base.Config):
    export_subpath = c.Type(str)
    license_type_order = c.ListOfItems(c.Type(str))
    discipline_order = c.ListOfItems(c.Type(str))
    system_order = c.ListOfItems(c.Type(str))
    appendix = c.Optional(c.ListOfItems(c.SubConfig(_AppendixItem)))
