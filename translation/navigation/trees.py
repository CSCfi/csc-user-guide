import pathlib
import itertools

import yaml

from .classes import NavPage, NavSection, IndexSection, NavItem


def _nav_constructor(loader, node):
    mapping = loader.construct_mapping(node)

    match list(mapping.items()):
        case _ if "nav" in mapping and node.start_mark.column < 1:
            return NavSection(loader.name, mapping["nav"])

        case [(str(title), (str(page), *children))]:
            return IndexSection(title, page, tuple(children))

        case [(str(title), tuple(children))]:
            return NavSection(title, children)

        case [(str(title), page)]:
            return NavPage(title, page)

        case _:
            return None


def _tuple_constructor(loader, node):
    return tuple(loader.construct_sequence(node))


# Construct custom objects
for tag, constructor in {
    "map": _nav_constructor,
    "seq": _tuple_constructor
}.items():
    yaml.add_constructor(f"tag:yaml.org,2002:{tag}",
                         constructor, Loader=yaml.SafeLoader)

# Ignore Python tags in YAML
for tag in (
    "!",
    "tag:yaml.org,2002:python/",
):
    yaml.add_multi_constructor(tag, lambda *_: None, Loader=yaml.SafeLoader)

# Dont' emit YAML tags
yaml.emitter.Emitter.prepare_tag = lambda *_: ""


def _read_nav_from(path_obj: pathlib.Path) -> NavItem:
    with path_obj.open(mode="rt", encoding="utf-8") as fp:
        return yaml.load(fp, Loader=yaml.SafeLoader)


def get_nav_trees(config_filename: str) -> tuple[NavItem]:
    original_config = pathlib.Path(config_filename)
    config_glob = f"{original_config.stem}_*{original_config.suffix}"
    config_filepaths = \
        itertools.chain((original_config,),
                        original_config.parent.glob(config_glob))

    return tuple(map(_read_nav_from, config_filepaths))
