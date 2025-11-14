from html.parser import HTMLParser


class LicenseParser(HTMLParser):
    heading_levels = ("h2", "h3",)

    def __init__(self):
        super().__init__()
        self.__heading_stack = []
        self.__heading_found = False

    def handle_starttag(self, tag, _):
        self.__heading_stack.append(tag)

    def handle_endtag(self, tag):
        self.__heading_stack.pop()

    def handle_data(self, data):
        if self.__heading_stack \
            and self.__heading_stack[-1] in self.heading_levels \
            and data.startswith("License"):

            self.__heading_found = True

    @property
    def valid(self):
        return self.__heading_found
