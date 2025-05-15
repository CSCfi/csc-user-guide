import yaml
from pathlib import Path
from types import SimpleNamespace

from mkdocs.plugins import get_plugin_logger

from .config import SWCatalogConfig
from .hook import SWCatalogHook


def read_config_file():
    config_filepath = Path.cwd() / "hooks" / __name__ / "config.yml"

    with open(config_filepath, "r") as config_file:
        return yaml.safe_load(config_file)

def get_config():
    config_dict = read_config_file()
    config = SWCatalogConfig()
    config.load_dict(config_dict)

    return config

logger = get_plugin_logger(f"{__name__}-hook")
config = get_config()

failed, warnings = config.validate()

for failure in failed:
    logger.error(failure)

for warning in warnings:
    logger.warning(warning)

hook = SWCatalogHook(SimpleNamespace(**config), logger)

on_page_markdown = hook.on_page_markdown
on_page_context = hook.on_page_context
on_post_build = hook.on_post_build
on_serve = hook.on_serve

__all__ = [name for name in locals().keys() if name.startswith("on_")]
