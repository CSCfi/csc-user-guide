from .parsers import LicenseParser


def is_app_page(page_obj):
    try:
        catalog = page_obj.meta["catalog"]
    except KeyError:
        return False
    else:
        return not catalog.get("unchecked", False)

def contains_license_heading(markup):
    parser = LicenseParser()
    parser.feed(markup)

    return parser.valid

def find_fixmes(markdown):
    lines = markdown.split("\n")
    fixme_indices = []

    for i, line in enumerate(lines):
        if "FIXME" in line: fixme_indices.append(i)

    return fixme_indices
