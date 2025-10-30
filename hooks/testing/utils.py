from .parsers import LicenseParser


def check_license(markup):
    parser = LicenseParser()
    parser.feed(markup)

    return parser.valid

def find_fixmes(markdown):
    lines = markdown.split("\n")
    fixme_indices = []

    for i, line in enumerate(lines):
        if "FIXME" in line: fixme_indices.append(i)

    return fixme_indices
