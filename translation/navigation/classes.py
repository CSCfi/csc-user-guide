import abc
import itertools
from typing import Self, NamedTuple, Iterable, Union

import yaml


class NavPage(NamedTuple):
    title: str
    page: str

    def asdict(self) -> dict:
        return {self.title: self.page}

    def validate_against(self, other: "NavPage", node: "MultiNode") -> bool | None:
        if not isinstance(other, NavPage):
            raise NavDiscrepancy("Not a page", other, node)

        if not isinstance(other.page, str):
            raise NavDiscrepancy("Not a page", other, node)

        if not self.page == other.page:
            raise PageDiscrepancy("Page discrepancy", other, node)


class NavSection(NamedTuple):
    title: str
    children: tuple

    @staticmethod
    def validate_children(a: tuple["NavItem"], b: tuple["NavItem"]) -> bool:
        def classnames(children):
            return tuple(map(lambda child: type(child).__name__, children))

        classes = (classnames(a), classnames(b),)

        return len(a) == len(b) and len(set(classes)) == 1

    def asdict(self) -> dict:
        return {self.title: [child.asdict() for child in self.children]}

    def validate_against(self, other: "NavSection", node: "MultiNode") -> bool | None:
        if not isinstance(other, NavSection):
            raise NavDiscrepancy("Not a section", other, node)

        if not self.validate_children(self.children, other.children):
            raise SectionDiscrepancy("Section discrepancy", other, node)

        return True


class IndexSection(NamedTuple):
    title: str
    page: str
    children: tuple

    def asdict(self) -> dict:
        return {self.title: [self.page] + [child.asdict() for child in self.children]}

    def validate_against(self, other: "IndexSection", node: "MultiNode") -> bool | None:
        if not isinstance(other, IndexSection):
            raise NavDiscrepancy("Not an index section", other, node)

        if self.page != other.page:
            raise IndexDiscrepancy("Index page discrepancy", other, node)

        if not NavSection.validate_children(self.children, other.children):
            raise SectionDiscrepancy("Section discrepancy", other, node)

        return True


NavItem = Union[NavPage, NavSection, IndexSection]


class MultiNode(abc.ABC):
    @abc.abstractmethod
    def __init__(self,
                 *items: Iterable[NavItem],
                 parent: Self | None):
        ...

    @abc.abstractmethod
    def parent_of(self, item: NavItem) -> NavSection | IndexSection | None:
        ...

    @property
    @abc.abstractmethod
    def children(self) -> Iterable[Self]:
        ...


class NavDiscrepancy(Exception):
    PLACEHOLDER = "..."
    INDICATOR = "  <--- "

    @staticmethod
    def _dummy_title(item, node, parent=False):
        item, orig = ((node.parent_of(item), node.parent.orig)
                      if parent
                      else (item, node.orig))

        return f"{item.title} [{orig.title}]"

    @staticmethod
    def _dummy_index(item, node):
        parent_item = node.parent_of(item)

        return parent_item.children.index(item) + int(isinstance(parent_item, IndexSection))

    @classmethod
    def _dummy_section(cls, item, node, parent=False):
        item = node.parent_of(item) if parent else item
        n_children = len(item.children) + int(isinstance(item, IndexSection))

        return [cls.PLACEHOLDER] * n_children

    def __init__(self, message, item: NavItem, node: MultiNode):
        super().__init__(message)
        self.item = item
        self.node = node

    def _dummy_tree(self, leaf):
        tree = leaf
        item = self.item
        node = self.node

        while node.parent is not None:
            dummy = self._dummy_section(item, node, parent=True)

            dummy[self._dummy_index(item, node)] = tree
            tree = {self._dummy_title(item, node, parent=True): dummy}

            item, node = node.parent_of(item), node.parent

        return tree

    def show(self, leaf=None):
        if leaf is None:
            leaf = f"{self.item}{self.INDICATOR}???"

        return yaml.dump(self._dummy_tree(leaf)).replace("'", "")


class PageDiscrepancy(NavDiscrepancy):
    def __init__(self, message, page: NavPage, node: MultiNode):
        super().__init__(message, page, node)

    def show(self):
        page = f"{self.item.page}{self.INDICATOR}{self.node.orig.page}"
        leaf = f"{self._dummy_title(self.item, self.node)}: {page}"

        return super().show(leaf)

    def overlay(self, *others):
        layers = self.show()

        for other in others:
            if (not isinstance(other, PageDiscrepancy)
                    or self.node.parent_of(self.item) != other.node.parent_of(other.item)):
                raise TypeError(f"Cannot overlay {other} with {self}")

            layers = "\n".join(
                (top if self.PLACEHOLDER in bottom else bottom)
                for bottom, top
                in zip(*map(str.splitlines, (layers, other.show(),)))
            )

        return layers


class IndexDiscrepancy(NavDiscrepancy):
    def __init__(self, message, section: IndexSection, node: MultiNode):
        super().__init__(message, section, node)

    def show(self):
        dummy_section = [f"{self.item.page}{self.INDICATOR}{self.node.orig.page}",
                         *self._dummy_section(self.item, self.node)[1:]]
        leaf = {self._dummy_title(self.item, self.node): dummy_section}

        return super().show(leaf)


class SectionDiscrepancy(NavDiscrepancy):
    def __init__(self, message, section: NavSection, node: MultiNode):
        super().__init__(message, section, node)

    def show(self):
        indicator_section = []
        orig_children, alt_children = self.node.orig.children, self.item.children
        for orig, alt in itertools.zip_longest(orig_children, alt_children):
            match orig, alt:
                case _, None:
                    dummy_item = f"??? [{orig.title}]{self.INDICATOR}missing "
                    match orig:
                        case NavPage():
                            dummy_item += "page"
                        case NavSection() | IndexSection():
                            dummy_item += "section"
                        case _:
                            dummy_item += "item"
                case None, _:
                    dummy_item = f"{alt.title} [???]{self.INDICATOR}extra item"
                case NavPage(), _ if not isinstance(alt, NavPage):
                    dummy_item = f"{alt.title} [{orig.title}]{self.INDICATOR}should be a page"
                case NavSection(), _ if not isinstance(alt, NavSection):
                    dummy_item = f"{alt.title} [{orig.title}]{self.INDICATOR}should be a section"
                case IndexSection(), _ if not isinstance(alt, IndexSection):
                    dummy_item = f"{alt.title} [{orig.title}]{self.INDICATOR}should be an index section"
                case NavPage(), NavPage() if orig.page != alt.page:
                    dummy_item = f"{alt.title} [{orig.title}]: {alt.page}{self.INDICATOR}{orig.page}"
                case _:
                    dummy_item = self.PLACEHOLDER
            indicator_section.append(dummy_item)

        leaf = {self._dummy_title(self.item, self.node): indicator_section}

        return super().show(leaf)
