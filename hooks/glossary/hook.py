"""Generate a page with all the glossary entries.
"""
import pathlib
import re

from classes import DocsHook


class GlossaryHook(DocsHook):
    """Generate glossary page 'support/glossary.md'.
    """
    entry_pattern = r"^[\*-]\[([^\]]+)\]: (.+)$"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__entries = {}

    def __entries_from(self, path):
        with path.open("rt", encoding="utf-8") as fp:
            for line in fp.readlines():
                try:
                    m = re.fullmatch(self.entry_pattern, line.strip())
                    term = m.group(1)
                    definition = m.group(2)
                    entry = f"- `{term}`: {definition}\n"
                    try:
                        self.__entries[term[0].lower()].append(entry)
                    except KeyError:
                        self.__entries[term[0].lower()] = [entry]
                except AttributeError:
                    pass

    def on_config(self, config): # pylint: disable=missing-function-docstring
        try:
            snippets_config = config.mdx_configs["pymdownx.snippets"]
            base_path = snippets_config["base_path"]
            glossaries = snippets_config["auto_append"]
        except (AttributeError, KeyError):
            pass
        else:
            for glossary in glossaries:
                self.__entries_from(pathlib.Path(base_path) / glossary)
                self._logger.info("Glossary entries read from '%s'.", glossary)

    def on_page_markdown(self, markdown, page, **_): # pylint: disable=missing-function-docstring
        if page.file.src_uri == "support/glossary.md":
            sections = {alpha.upper(): "\n".join(sorted(entries,
                                                 key=lambda e: e.lower()))
                        for alpha, entries
                        in sorted(self.__entries.items())}

            self._logger.info("Writing glossary to '%s'.", page.file.src_uri)
            return markdown + "\n".join(f"## {heading}\n\n{lines}"
                                        for heading, lines
                                        in sections.items())

        return None
