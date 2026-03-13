"""Defines some constants.
"""
from types import SimpleNamespace


LANG_CODE_MAP = {
    "fi": "Finnish"
}
DEFAULTS = SimpleNamespace(
    docs_dir="docs",
    snapshots_filename="snapshots.json",
    excludes_filename="exclude.txt",
    dictionary_filename="dictionary.yml",
    force_filename="force.yml",
    batch_size=4,
    source_lang_code="en",
    source_language="English",
    openai=SimpleNamespace(
        model="gpt-5",
        max_tokens=128000, # https://platform.openai.com/docs/models/gpt-5
        max_tokens_multiplier=1.1,
        timeout=10.0,
        retries=5
    ),
)
