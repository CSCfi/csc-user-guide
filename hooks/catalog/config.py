import os

from mkdocs.config import base, config_options as c, defaults as d
from mkdocs.exceptions import PluginError

from .apps import App, DocsApp, AppendixApp


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


class _File(c.File):
    def __init__(self, name="", base_dir="", absolute: bool=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.base_dir = base_dir
        self.absolute = absolute

    def run_validation(self, value):
        absolute_path = super().run_validation(os.path.join(self.base_dir, value))

        return absolute_path if self.absolute else value


class _DocSrc(c.BaseConfigOption):
    name = "source document"

    def __init__(self, base_dir="", **kwargs):
        super().__init__(**kwargs)
        self.base_dir = base_dir

    def run_validation(self, value):
        error = False
        url_option = c.URL()
        file_option  = _File(exists=True,
                             name=self.name,
                             base_dir=self.base_dir)

        try:
            url = url_option.run_validation(value)
            return {"url": url}
        except (base.ValidationError, TypeError):
            error = True

        try:
            src = file_option.run_validation(value)
            return {"src": src}
        except (base.ValidationError, TypeError):
            error = True

        if error:
            message = f"'{value}' is neither a valid URL nor a {file_option.name}."
            raise base.ValidationError(message)


class CatalogConfig:
    APP_PROPS = tuple(prop
                      for prop, obj
                      in (vars(App)
                          | vars(DocsApp)
                          | vars(AppendixApp)
                         ).items()
                       if isinstance(obj, property))

    def __new__(cls, mkdocs_config: d.MkDocsConfig, config_dict: dict):
        class _AppendixItem(base.Config):
            name = c.Type(str)
            description = c.Type(str)
            disciplines = c.ListOfItems(c.Type(str))
            doc = _DocSrc(base_dir=mkdocs_config.docs_dir)


        class _CatalogConfig(base.Config):
            index_template = _File(exists=True,
                                   name="index template",
                                   base_dir=mkdocs_config.theme.custom_dir)
            export_filepath = _File(exists=False,
                                    name="export file",
                                    base_dir=mkdocs_config.site_dir,
                                    absolute=True)
            export_props = c.ListOfItems(c.Choice(cls.APP_PROPS))
            listing_order = c.SubConfig(_ListingOrder)
            appendix = c.ListOfItems(c.SubConfig(_AppendixItem))

            def validate(self):
                failed, warnings = super().validate()

                for key, error in failed:
                    raise PluginError(f"{key}: {error}")

                return warnings

        config = _CatalogConfig()
        config.load_dict(config_dict)

        return config



