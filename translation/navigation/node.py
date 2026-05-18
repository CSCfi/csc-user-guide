
import itertools

from .classes import MultiNode, NavSection, IndexSection, NavDiscrepancy


class NavNode(MultiNode):
    def __init__(self, *items, parent=None):
        self.__items = tuple(items)
        self.orig, *self.alts = self.__items
        self.parent = parent
        self.__parents = {tuple(item): parent[i]
                          for i, item in enumerate(items)
                          if None not in (item, parent,)}
        self.discrepancies = []
        self.__child_nodes = self.__validate()

    def __repr__(self):
        items = ", ".join(f"{type(item).__name__}(title='{item.title}', ...)"
                          for item
                          in self.__items)

        return f"{type(self).__name__}({items}, parent={self.parent})"

    def __getitem__(self, key):
        return self.__items[key]

    def __len__(self):
        return len(self.__items)

    def parent_of(self, item):
        return self.__parents.get(item)

    def __validate(self):
        if hasattr(self.orig, "children"):
            child_nodes = [self.orig.children] + [(None,)]*len(self.alts)

            for i, alt in enumerate(self.alts, start=1):
                if alt is not None:
                    try:
                        self.orig.validate_against(alt, self)
                    except NavDiscrepancy as nd:
                        self.discrepancies.append(nd)
                    else:
                        child_nodes[i] = alt.children

            return child_nodes

        for alt in self.alts:
            if alt is not None:
                try:
                    self.orig.validate_against(alt, self)
                except NavDiscrepancy as nd:
                    self.discrepancies.append(nd)

        return ()

    @property
    def children(self):
        for node in itertools.zip_longest(*self.__child_nodes):
            yield NavNode(*node, parent=self)

    @property
    def has_subsection(self):
        return any((isinstance(child, (NavSection, IndexSection))
                    for child
                    in self.orig.children))
