"""Parse a What's new section from HTML data.
"""
import string
from html.parser import HTMLParser

class WhatsNewParser(HTMLParser):
    """Generate a section of links in Markdown, including a heading.
    """
    def __init__(self, path, level: int=2):
        super().__init__(convert_charrefs=False)

        self.__stack = []
        self.__markdown_lines = []
        self.__tags = {
            "h1": {
                "template": string.Template("$level $title\n\n"),
                "substitutions": {
                    "level": "#" * level,
                    "title": "",
                }
            },
            "h2": {
                "template": string.Template("- [$title]($path#$fragment)\n"),
                "substitutions": {
                    "title": "",
                    "path": path,
                    "fragment": None
                }
            }
        }

    def __getitem__(self, key):
        return self.__markdown_lines[key]

    def __append(self, data):
        try:
            self.__tags[self.__stack[0]]["substitutions"]["title"] += data
        except (IndexError, KeyError):
            pass

    def handle_starttag(self, tag, attrs):
        self.__stack.append(tag)

        try:
            self.__tags[tag]["substitutions"]["fragment"] = dict(attrs)['id']
        except KeyError:
            pass

    def handle_endtag(self, _):
        try:
            tag = self.__stack.pop()
            template, substitutions = self.__tags[tag].values()
        except (IndexError, KeyError, ValueError):
            pass
        else:
            self.__markdown_lines.append(template.substitute(substitutions))
            self.__tags[tag]["substitutions"]["title"] = ""

    def handle_charref(self, name):
        self.__append("&#{name};")

    def handle_entityref(self, name):
        self.__append(f"&{name};")

    def handle_data(self, data):
        self.__append(data)
