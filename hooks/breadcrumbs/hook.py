"""Handle missing breadcrumbs.
"""
import pathlib

from classes import DocsHook


class BreadcrumbsHook(DocsHook):
    """Look for adoptive parents for pages without ancestors.
    """
    # pylint: disable=missing-function-docstring

    IGNORE = ["support/index.md"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__orphans = {}

    def on_pre_page(self, page, config, files): # pylint: disable=unused-argument
        if not page.ancestors:
            self.__orphans[pathlib.Path(page.file.src_uri)] = page

    def on_page_context(self, context, page, config, nav):
        if page not in nav.pages and not page.is_homepage:
            page_file = pathlib.Path(config.docs_dir) / page.file.src_uri
            parent_dir = (page_file.parent
                          if page_file.name != "index.md"
                          else page_file.parent.parent)

            ancestors = []
            while parent_dir.is_relative_to(config.docs_dir):
                adoptive_lookup = parent_dir / "index.md"
                if adoptive_lookup.exists():
                    relative_path = adoptive_lookup.relative_to(config.docs_dir)
                    if (relative_path in self.__orphans
                            and relative_path not in (pathlib.Path(p)
                                                      for p
                                                      in self.IGNORE)):
                        ancestor_page = self.__orphans[relative_path]
                        if not ancestor_page.is_homepage:
                            ancestors.append(ancestor_page)

                parent_dir = parent_dir.parent

            return context | {"adoptive_ancestors": ancestors}

        return None
