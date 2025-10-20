from http import HTTPStatus
from string import Template

from classes import DocsHook
from .archives import RSSArchive


PRODUCTION_ENVIRONMENT = "production"
ENVIRONMENT_KEY = "environment"
URL_KEY = "archive_feed"


class ArchiveHook(DocsHook):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.environment = None

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

    def on_config(self, config):
        self.environment = config.extra[ENVIRONMENT_KEY]

    def on_page_markdown(self, markdown, page, config, files):
        if self.environment == PRODUCTION_ENVIRONMENT:
            try:
                archive_url = page.meta[URL_KEY]
            except KeyError:
                return None
            else:
                self._logger.info(f"Fetching archive from {archive_url}...")
                archive = RSSArchive(archive_url)
                self.__log_status(archive)

                if any((archive.title is None,
                        archive.entries is None)):
                    return None
                else:
                    page.meta["title"] = archive.title
                    return self.__get_heading(markdown) + archive.markdown
        else:
            return None
