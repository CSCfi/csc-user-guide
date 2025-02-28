from pathlib import Path
from types import SimpleNamespace

from mkdocs.config.defaults import MkDocsConfig

from .constants import *


class SWCatalogConfig:
    def __new__(self, config: MkDocsConfig):
        return SimpleNamespace(
            export_filepath=(Path(config.site_dir) / CATALOG_DIRNAME / "catalog.json").resolve(),
            appendix_srcpath=(Path.cwd() / CATALOG_DIRNAME / "appendix.yml").resolve(),
            hook_name=MKDOCS_HOOK_NAME,
            index_template=str(Path(CATALOG_DIRNAME) / "apps-index.html"),
            meta_key="software_catalog",
            licenses=LICENSE_TYPES,
            disciplines=DISCIPLINES,
            systems=SYSTEMS,
            exported_props=EXPORTED_PROPERTIES
        )
