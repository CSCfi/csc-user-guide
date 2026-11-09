"""Generate links to What's new entries.
"""
import pathlib
import functools

from markdown import Markdown

from classes import DocsHook
from .parser import WhatsNewParser


class WhatsNewHook(DocsHook):
    """List What's new entries on
        - docs/index.md (cutoff)
        - docs/support/whats-new.md
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__md = None
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
        def handle_wn(wn_file):
            self.__wn_sections[wn_file] = self.__md.convert(
                wn_file.read_text(encoding="utf-8")
            )
            self._logger.info("What's new entries read from '%s'.",
                wn_file.relative_to(pathlib.Path(config.docs_dir))
            )

        self.__md = Markdown(extensions=config.markdown_extensions)

        wn_path = pathlib.Path(config.docs_dir) / "support/wn/"
        wn_glob = wn_path.glob("*-new.md")

        for wn_file in wn_glob:
            self._skip_if_clean(
                wn_file,
                functools.partial(handle_wn, wn_file)
            )

    def on_page_markdown(self, markdown, page, config, **_): # pylint: disable=missing-function-docstring
        if page.file.src_uri in ("index.md", "support/whats-new.md"):
            level, cutoff = ((3, 6)
                            if page.file.src_uri == "index.md"
                            else (2, None))
            reducer = self.__get_reducer(
                pathlib.Path(config.docs_dir) / page.file.src_uri,
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
