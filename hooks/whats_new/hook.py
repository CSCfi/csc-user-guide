"""Generate links to What's new entries for
  - docs/index.md
  - docs/support/whats-new.md
"""
import pathlib
import functools

from markdown import Markdown

from classes import DocsHook
from .parser import WhatsNewParser


class WhatsNewHook(DocsHook):
    """Generate What's new entries.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__docs_path = None
        self.__wn_sections = {}

    def __get_reducer(self, source, level=2, cutoff=None):
        def wn_reducer(sections, item, level=level):
            target, html = item
            parser = WhatsNewParser(target.relative_to(source.parent),
                                    level=level)
            parser.feed(html)
            return sections + "".join(parser[:cutoff])

        return wn_reducer

    def on_config(self, config): # pylint: disable=missing-function-docstring
        self.__docs_path = pathlib.Path(config.docs_dir).resolve()
        wn_path = self.__docs_path / "support/wn/"
        wn_glob = wn_path.glob("*-new.md")

        md = Markdown(extensions=config.markdown_extensions)
        for wn_page in wn_glob:
            self.__wn_sections[wn_page] = md.convert(
                wn_page.read_text(encoding="utf-8")
            )
            self._logger.info("What's new entries read from '%s'.",
                              wn_page.relative_to(self.__docs_path))

    def on_page_markdown(self, markdown, page, **_): # pylint: disable=missing-function-docstring
        if page.file.src_uri in ("index.md", "support/whats-new.md"):
            level, cutoff = ((3, 6)
                            if page.file.src_uri == "index.md"
                            else (2, None))
            reducer = self.__get_reducer(
                self.__docs_path / page.file.src_uri,
                level=level,
                cutoff=cutoff
            )

            self._logger.info("Appending What's new entries to '%s'.",
                              page.file.src_uri)
            return markdown \
                + functools.reduce(reducer,
                                   self.__wn_sections.items(),
                                   "")

        return None
