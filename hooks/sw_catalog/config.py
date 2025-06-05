import os

from mkdocs.config import base, config_options as c


class _DocFile(c.File):
    name = "documentation file"

    def __init__(self, docs_dir="", **kwargs):
        super().__init__(**kwargs)
        self.docs_dir = docs_dir

    def run_validation(self, value):
        return super().run_validation(os.path.join(self.docs_dir, value))


class _ListingOrder(base.Config):
    license_types = c.ListOfItems(c.Type(str))
    disciplines = c.ListOfItems(c.Type(str))
    systems = c.ListOfItems(c.Type(str))


def get_config(docs_dir):
    class _AppendixItem(base.Config):
        name = c.Type(str)
        description = c.Type(str)
        disciplines = c.ListOfItems(c.Type(str))
        url = c.Optional(c.URL())
        src = c.Optional(_DocFile(exists=True, docs_dir=docs_dir))


    class _CatalogConfig(base.Config):
        export_subpath = c.Type(str)
        listing_order = c.SubConfig(_ListingOrder)
        appendix = c.ListOfItems(c.SubConfig(_AppendixItem))

    return _CatalogConfig()
