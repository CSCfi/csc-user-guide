"""Parsers for handing test cases.
"""
from html.parser import HTMLParser
from urllib.parse import urlsplit


class SiteUrlLinkChecker(HTMLParser):
    """Exposes the list 'hits' holding the link text for
       each link found in 'markup' that points to 'site_url'.
    """
    def __init__(self, site_url, markup):
        if (netloc := self.__parse_url(site_url)) is None:
            raise ValueError("Could not determine site url.")

        self.netloc = netloc
        self.hits = []
        self.__stack = []
        self.__buffer = []

        super().__init__()
        super().feed(markup)

    def __parse_url(self, url):
        try:
            netloc = urlsplit(url).netloc

            return None if netloc == "" else netloc
        except ValueError:
            return None

    def handle_starttag(self, tag, attrs):
        match tag, dict(attrs):
            case "a", {"href": href} if self.__parse_url(href) == self.netloc:
                self.__stack.append(tag)
            case _:
                pass

    def handle_data(self, data):
        try:
            if self.__stack[-1] == "a":
                self.__buffer.append(data.replace("\n", " ").strip())
        except IndexError:
            pass

    def handle_endtag(self, tag):
        try:
            if self.__stack[-1] == tag:
                self.hits.append(" ".join(self.__buffer))
                self.__stack.pop()
        except IndexError:
            pass
