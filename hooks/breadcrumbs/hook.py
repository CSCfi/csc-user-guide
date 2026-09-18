"""Handle missing breadcrumbs.
"""
import pathlib

from classes import DocsHook


class DummyParent:
    def __init__(self, page, anchor):
        self.__page = page
        self.__anchor = anchor

    def __toc_item(self, items):
        for item in items:
            if item.id == self.__anchor:
                return item
            if item.children:
                return self.__toc_item(item.children)

            return "None"

    @property
    def title(self):
        item = self.__toc_item(self.__page.toc)
        return item.title

    @property
    def url(self):
        item = self.__toc_item(self.__page.toc)
        return f"{self.__page.url}{item.url}"


class BreadcrumbsHook(DocsHook):
    """Look for adoptive parents for pages without ancestors.
    """
    # pylint: disable=missing-function-docstring

    LOOKUP = "index.md"
    IGNORE = [
        "support/index.md"
    ]
    INCLUDE = {
        "support/wn": "support/whats-new.md"
    }
    DUMMIES = {
        "support/archives": ("support/contact.md", "archives",)
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__adoptive_parents = {}
        self.__dummy_parents = {}

    def __find_dummy(self, relative_dir):
        return self.__dummy_parents.get(str(relative_dir))

    def __find_included(self, root_dir, relative_dir):
        return (self.__adoptive_parents.get(root_dir / self.INCLUDE[str(relative_dir)])
                if str(relative_dir) in self.INCLUDE
                else None)

    def __find_surrogate(self, root_dir, parent_dir):
        relative_dir = parent_dir.relative_to(root_dir)

        return self.__find_included(root_dir, relative_dir) or self.__find_dummy(relative_dir)

    def __find_adoptive_ancestors(self, root, page):
        root_dir = pathlib.Path(root)
        page_path = root_dir / page.file.src_uri
        parent_dir = (page_path.parent
                      if page_path.name != self.LOOKUP
                      else page_path.parent.parent)

        ancestors = []
        while parent_dir.is_relative_to(root_dir):
            adoptive_lookup = (self.__adoptive_parents.get(parent_dir / self.LOOKUP)
                               or self.__find_surrogate(root_dir, parent_dir))

            if adoptive_lookup:
                ancestors.append(adoptive_lookup)

            parent_dir = parent_dir.parent

        return ancestors

    def on_nav(self, nav, config, files):  # pylint: disable=unused-argument
        for key, (page, anchor) in self.DUMMIES.items():
            self.__dummy_parents[key] = DummyParent(files.get_file_from_path(page).page, anchor)

        for file_obj in files:
            if file_obj.page is None or file_obj.src_uri in self.IGNORE:
                continue

            if not file_obj.page.is_homepage:
                self.__adoptive_parents[pathlib.Path(file_obj.abs_src_path)] = file_obj.page

    def on_page_context(self, context, page, config, nav):
        if page.file.src_uri not in list(map(lambda p: p.file.src_uri, nav.pages)):
            return context | {
                "adoptive_ancestors": self.__find_adoptive_ancestors(config.docs_dir, page)
            }

        return None

