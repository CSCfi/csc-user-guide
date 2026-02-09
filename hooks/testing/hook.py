from mkdocs.plugins import event_priority

from classes import DocsHook
from .tests import DocsTests


class TestingHook(DocsHook):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    @event_priority(100)
    def on_pre_build(self, **_):
        self._logger.info("test build")

    @event_priority(-100)
    def on_files(self, files, **_):
        DocsTests.no_fixmes_are_present_in_documentation_sources(files)

        return None

    @event_priority(-100)
    def on_post_page(self, output, page, **_):
        DocsTests.app_page_contains_license_heading(output, page)

        return None

    @event_priority(-100)
    def on_post_build(self, **_):
        warnings = DocsTests.get_report()

        if warnings:
            for message in warnings:
                self._logger.warning(message)
        else:
            self._logger.info("All tests passed.")
