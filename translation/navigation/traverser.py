import itertools

from .node import NavNode
from .classes import PageDiscrepancy, SectionDiscrepancy
from .trees import get_nav_trees


class NavTraverser:
    """Traverse navigation trees picking up discrepancies.
    """

    SECTION_WARNING = """
*** Section discrepancy was found in a section that has one or more subsections. ***
Please re-check after fixing the section discrepancy, as the subsections cannot be traversed due to the discrepancy.\
"""

    def __init__(self, filename: str):
        self.__root = NavNode(*get_nav_trees(filename))
        self.__stack = [self.__root]
        self.__discrepancies = self.__traverse()

    def __traverse(self):
        discrepancies = []

        while self.__stack:
            node = self.__stack.pop()
            self.__stack.extend(reversed(tuple(node.children)))
            discrepancies.extend(node.discrepancies)

        return discrepancies

    def __output(self):
        for key, group in itertools.groupby(self.__discrepancies, key=lambda d: (d.node.parent_of(d.item), isinstance(d, PageDiscrepancy),)):
            discrepancies = list(group)

            if key[1] and len(discrepancies) > 1:
                base, *layers = discrepancies
                yield f"{str(base)[:-1]}ies in " + base.overlay(*layers)
            else:
                yield from (f"{discrepancy} in " + discrepancy.show() for discrepancy in discrepancies)

    @property
    def filenames(self):
        return tuple(nav.title for nav in self.__root)

    @property
    def output(self):
        output = ("\n"*2).join(self.__output())

        if any(((isinstance(discrepancy, SectionDiscrepancy)
                    and discrepancy.node.has_subsection)
                for discrepancy
                in self.__discrepancies)):
            output += self.SECTION_WARNING

        return output
