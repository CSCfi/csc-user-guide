from classes import DocsHook
from .utils import check_license, find_fixmes


class TestingHook(DocsHook):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def on_files(self, files, **_):
        for file in files:
            if file.is_documentation_page():
                fixmes = find_fixmes(file.content_string)
                if fixmes:
                    lines = ', '.join(map(lambda i: str(i+1), fixmes))
                    message = f"FIXME found on {file.src_uri} line(s) {lines}"
                    self._logger.warning(message)

        return None

    def on_post_page(self, output, page, **_):
        if "catalog" in page.meta \
            and not page.meta.get("catalog", {}).get("unchecked"):

            if not check_license(output):
                message = f"No licensing information found on app page {page.file.src_uri}"
                self._logger.warning(message)

        return None
