"""Site content-related testing suite.
"""
import humps
from mkdocs.plugins import event_priority
from markdown.extensions import Extension

from classes import DocsHook
from .tests import DocsTests
from .processors import AppLicenseHeadingProcessor
from .parsers import SiteUrlLinkChecker


class TestingExtension(Extension):
    """Markdown extension for tapping into the Markdown conversion.
    """
    def __init__(self, *treeprocessors):
        self.treeprocessors = {
            humps.kebabize(processor.__class__.__name__): processor
            for processor in treeprocessors
        }

        super().__init__()

    def extendMarkdown(self, md):
        for name, processor in self.treeprocessors.items():
            md.treeprocessors.register(processor, name, 0)
            md.registerExtension(self)

    def reset(self): # pylint: disable=missing-function-docstring
        for processor in self.treeprocessors.values():
            if hasattr(processor, "reset"):
                processor.reset()


class TestingHook(DocsHook):
    """Run tests in appropriate phases of the build.
    """
    def __init__(self, **kwargs):
        self.extension = {}

        super().__init__(self, **kwargs)

    @event_priority(100)
    def on_pre_build(self, **_): # pylint: disable=missing-function-docstring
        self._logger.info("test build")

    @event_priority(-100)
    def on_config(self, config): # pylint: disable=missing-function-docstring
        self.extension = TestingExtension(
            AppLicenseHeadingProcessor(DocsTests.LICENSE_HEADING_LEVEL_RANGE)
        )

        config["markdown_extensions"].append(self.extension)

    @event_priority(-100)
    def on_files(self, files, **_): # pylint: disable=missing-function-docstring
        DocsTests.no_fixmes_are_present_in_documentation_sources(files)

    @event_priority(-100)
    def on_page_content(self, _, page, **__): # pylint: disable=missing-function-docstring
        DocsTests.app_page_contains_license_heading(
            page,
            self.extension.treeprocessors["app-license-heading-processor"]
        )

    @event_priority(-100)
    def on_post_page(self, output, page, config): # pylint: disable=missing-function-docstring
        DocsTests.doc_page_has_no_internal_links_to_production_domain(
            page,
            SiteUrlLinkChecker(config.site_url, output)
        )

    @event_priority(-100)
    def on_post_build(self, **_): # pylint: disable=missing-function-docstring
        DocsTests.log_results(self._logger)
