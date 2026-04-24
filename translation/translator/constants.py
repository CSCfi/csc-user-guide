"""Defines some constants.
"""
from types import SimpleNamespace


LANG_CODE_MAP = {
    "fi": "Finnish"
}
DEFAULTS = SimpleNamespace(
    snapshots_filename="snapshots.json",
    excludes_filename="exclude.txt",
    dictionary_filename="dictionary.yml",
    force_filename="force.yml",
    batch_size=4, # not used, batching has issues
    source_lang_code="en",
    source_language="English",
    openai=SimpleNamespace(
        model="gpt-5.4",
        timeout=10.0,
        retries=5,
        temperature=0, # default is 1
    ),
)
