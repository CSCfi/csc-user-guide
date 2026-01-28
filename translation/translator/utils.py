"""Provides utility functions.
"""
import os
import pathlib
import logging

import yaml

from .constants import DEFAULTS, LANG_CODE_MAP


logger = logging.getLogger(__name__)


def _get_config_filepath(filename: str) -> pathlib.Path:
    module_path = pathlib.Path(__file__).parent

    return module_path.parent / filename


def _get_attrs(obj, attr_names):
    """Returns a dict of attributes listed in attr_names for obj.
    """
    return {attr: getattr(obj, attr)
            for attr
            in dir(obj)
            if attr in attr_names}


def _check_language(lang_code):
    """Asserts that 'lang_code' has a corresponding language name.
    """
    assert lang_code in LANG_CODE_MAP, f"Language '{lang_code}' not found."


def get_language(lang_code):
    """Returns the name of the language corresponding to 'lang_code'.

    Raises AssertionError.
    """
    _check_language(lang_code)

    return LANG_CODE_MAP[lang_code]


def check_environment(env_var_names):
    """Asserts that every variable in 'env_var_names' is defined in the
    environment.
    """
    for var_name in env_var_names:
        assert var_name in os.environ, f"{var_name} not found in environment"


def md_filter(diff_obj):
    """Return True if diff_obj describes a Markdown file.
    """
    diff_attrs = _get_attrs(diff_obj, ("a_path", "b_path", "rename_to",))

    return any(d_path.lower().endswith(".md")
               for d_path
               in _get_attrs(diff_obj, diff_attrs).values()
               if isinstance(d_path, str))


def batch(iterable, n):
    """Yield successive n-sized batches from iterable.
    """
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]


def get_excluded_filepaths(src_prefix):
    """Returns a list of file paths, relative to src_prefix, to exclude from
    translation.
    """
    excludes_path = _get_config_filepath(DEFAULTS.excludes_filename)

    try:
        with excludes_path.open(mode="rt", encoding="utf-8") as excludes:
            paths = [line.strip()
                    for line
                    in excludes.readlines()
                    if not line.startswith("#")]

        return [pathlib.Path(src_prefix) / filepath
                for filepath
                in paths
                if filepath]
    except FileNotFoundError as e:
        logger.warning("Can't read list of excluded files: %s", str(e))

        return []


def get_dictionary(lang_code):
    """Returns a dict of translation instructions for 'lang_code'.
    """
    dictionary_path = _get_config_filepath(DEFAULTS.dictionary_filename)
    src = DEFAULTS.source_lang_code
    tgt = lang_code
    try:
        with dictionary_path.open(mode="rt", encoding="utf-8") as dictionary:
            entries = yaml.safe_load(dictionary)
            return {entry[src]: entry[tgt]
                    for entry
                    in entries
                    if all(key in entry for key in (src, tgt,))}
    except FileNotFoundError as e:
        logger.warning("Can't read translation dictionary: '%s'", str(e))

        return {}


def mkparents(path: pathlib.Path):
    """Creates parent directories for path.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
