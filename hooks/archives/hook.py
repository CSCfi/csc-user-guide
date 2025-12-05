from http import HTTPStatus
from string import Template

from classes import DocsHook
from .archives import RSSArchive


class ArchiveHook(DocsHook):
    url_key = "archive_feed"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __log_status(self, archive):
        archive_template = Template("Archive '$title': $code $phrase")
        fail_template = Template("Failed to fetch $url: $code $phrase")
        none_template = Template("Failed to fetch $url: $exception")

        if archive.status is not None:
            status = HTTPStatus(archive.status)
            if 100 <= status.value <= 399:
                message = archive_template.substitute(title=archive.title,
                                                      code=status.value,
                                                      phrase=status.phrase)
                if status.value <= 299:
                    self._logger.info(message)
                else:
                    self._logger.warning(message)
            elif status.value >= 400:
                message = fail_template.substitute(url=archive.url,
                                                   code=status.value,
                                                   phrase=status.phrase)
                self._logger.error(message)
        else:
            message = none_template.substitute(url=archive.url,
                                               exception=archive.exception)
            self._logger.error(message)

    def __get_heading(self, markdown):
        return markdown.split("\n")[0] + "\n"

    def on_page_markdown(self, markdown, page, config, files):
        try:
            archive_url = page.meta[self.url_key]
        except KeyError:
            return None
        else:
            self._logger.info(f"Fetching archive from {archive_url}...")
            archive = RSSArchive(archive_url)
            self.__log_status(archive)

            if None in (archive.title, archive.entries,):
                return None
            else:
                page.meta["title"] = archive.title
                return self.__get_heading(markdown) + archive.markdown

        return None
