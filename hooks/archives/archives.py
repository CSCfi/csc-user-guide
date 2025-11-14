from datetime import date

import feedparser


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
        self.url = archive_url
        self.archive = feedparser.parse(self.url, sanitize_html=False)

    @property
    def status(self):
        return self.archive.get("status")

    @property
    def exception(self):
        return str(self.archive.get("bozo_exception"))

    @property
    def title(self):
        return self.archive.feed.get("title")

    @property
    def entries(self):
        return self.archive.get("entries")

    @property
    def items(self):
        return map(lambda e: str(ArchiveItem(e)), self.entries)

    @property
    def markdown(self):
        title = self.title
        content = "".join(self.items)
        return "## {}\n\n{}".format(title, content)
