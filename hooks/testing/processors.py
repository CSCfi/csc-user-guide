"""Markdown processors for handling test cases.
"""
from itertools import chain

from markdown.treeprocessors import Treeprocessor


class AppLicenseHeadingProcessor(Treeprocessor):
    """Exposes the boolean 'license_found' with the value True
       if a license heading was seen in the processed Markdown.
    """
    def __init__(self, h_level_range):
        self.h_levels = range(*h_level_range)
        self.license_found = None

        super().__init__()

    def run(self, root):
        for heading in chain(*(root.iterfind(f".//h{level}")
                               for level in self.h_levels)):
            if "".join(heading.itertext()).startswith("License"):
                self.license_found = True

                return

    def reset(self): # pylint: disable=missing-function-docstring
        self.license_found = None
