import os

from mkdocs.config import base, config_options as c, defaults as d

from .apps import App, DocsApp, AppendixApp


class CatalogConfig:
    APP_PROPS = tuple(prop
                    for prop, obj
                    in (vars(App)
                        | vars(DocsApp)
                        | vars(AppendixApp)
                        ).items()
                    if isinstance(obj, property))


    class _DocFile(c.File):
        name = "documentation file"

        def __init__(self, docs_dir="", **kwargs):
            super().__init__(**kwargs)
            self.docs_dir = docs_dir

        def run_validation(self, value):
            return super().run_validation(os.path.join(self.docs_dir, value))

    class _ExportFile(c.File):
        name = "export file"

        def __init__(self, site_dir="", **kwargs):
            super().__init__(**kwargs)
            self.site_dir = site_dir

        def run_validation(self, value):
            return super().run_validation(os.path.join(self.site_dir, value))


    def __new__(cls, mkdocs_config: d.MkDocsConfig, config_dict: dict):
        class _DisciplinesItem(base.Config):
            name = c.Type(str)
            name_fi = c.Type(str)
            fallback = c.Optional(c.Type(bool))

        class _SystemsItem(base.Config):
            name = c.Type(str)
            description = c.Type(str)
            description_fi = c.Type(str)

        class _ListingOrder(base.Config):
            license_types = c.ListOfItems(c.Type(str))
            disciplines = c.ListOfItems(c.SubConfig(_DisciplinesItem))
            systems = c.ListOfItems(c.SubConfig(_SystemsItem))

        class _AppendixItem(base.Config):
            name = c.Type(str)
            description = c.Type(str)
            disciplines = c.ListOfItems(c.Type(str))
            url = c.Optional(c.URL())
            src = c.Optional(cls._DocFile(exists=True, docs_dir=mkdocs_config.docs_dir))

        class _CatalogConfig(base.Config):
            export_filepath = cls._ExportFile(exists=False, site_dir=mkdocs_config.site_dir)
            export_props = c.ListOfItems(c.Choice(cls.APP_PROPS))
            listing_order = c.SubConfig(_ListingOrder)
            appendix = c.ListOfItems(c.SubConfig(_AppendixItem))

        config = _CatalogConfig()
        config.load_dict(config_dict)

        return config
