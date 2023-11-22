from http import HTTPStatus
from datetime import date
from logging import getLogger

import feedparser


ENVIRONMENT_KEY = "environment"
URL_KEY = "archive_feed"


class ArchiveItem:
    def __init__(self, entry):
        self.entry = entry

    def __str__(self):
        return self.markdown

    @property
    def date(self):
        return self.to_date_string(self.entry.published_parsed)

    @property
    def href(self):
        return self.to_https(self.entry.link)

    @property
    def markdown(self):
        heading = f"### {self.date}"
        link = f"[{self.entry.title}]({self.href}){{ target=_blank }}"
        return f"{heading}\n{link}\n"

    @staticmethod
    def to_date_string(struct_time):
        return "{0:%B} {0:%d}, {0:%Y}".format(
            date(*[getattr(struct_time, attr)
                   for attr
                   in ("tm_year", "tm_mon", "tm_mday")]))

    @staticmethod
    def to_https(href):
        if not href.startswith("http"):
            raise ValueError(f"Protocol must be HTTP(S): '{href}'")
        return (href.replace("http:", "https:", 1)
                if href.startswith("http:")
                else href)


class RSSArchive:
    def __init__(self, archive_url):
        self.archive = feedparser.parse(archive_url, sanitize_html=False)

    @property
    def status(self):
        return self.archive.get("status", None)

    @property
    def title(self):
        return self.archive.feed.title

    @property
    def entries(self):
        return self.archive.entries

    @property
    def items(self):
        return map(lambda e: str(ArchiveItem(e)), self.entries)

    @property
    def markdown(self):
        title = self.title
        content = "".join(self.items)
        return "## {}\n\n{}".format(title, content)


class ArchiveHook:
    def __init__(self, logger):
        self.logger = logger
        self.environment = None

    def __log_status(self, feed):
        msg = lambda feed, status: f"Archive '{feed.title}': {status.value} {status.phrase}"
        if feed.status is not None:
            status = HTTPStatus(feed.status)
            message = msg(feed, status)
            if 100 <= status.value <= 299:
                self.logger.info(message)
            elif 300 <= status.value <= 399:
                self.logger.warning(message)
            elif status.value >= 400:
                self.logger.error(message)

    def __get_heading(self, markdown):
        return markdown.split("\n")[0] + "\n"

    def on_config(self, config):
        self.environment = config.extra[ENVIRONMENT_KEY]

    def on_page_markdown(self, markdown, page, config, files):
        try:
            archive_url = page.meta[URL_KEY]
        except KeyError:
            return None
        else:
            self.logger.info(f"Fetching archive from {archive_url}...")
            archive = RSSArchive(archive_url)
            self.__log_status(archive)
            page.meta["title"] = archive.title
            return self.__get_heading(markdown) + archive.markdown


hook = ArchiveHook(getLogger("mkdocs"))
on_config = hook.on_config
on_page_markdown = hook.on_page_markdown
