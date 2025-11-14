from .utils import find_fixmes, is_app_page, contains_license_heading


class DocsTests:
    _warnings = []

    @classmethod
    def no_fixmes_are_present_in_documentation_sources(cls, source_files):
        for src_file in source_files:
            if src_file.is_documentation_page():
                fixmes = find_fixmes(src_file.content_string)
                if fixmes:
                    lines = ', '.join(map(lambda i: str(i+1), fixmes))
                    message = f"FIXME found on {src_file.src_uri} line(s) {lines}"

                    cls._warnings.append(message)

    @classmethod
    def app_page_contains_license_heading(cls, page_output, page_obj):
        if is_app_page(page_obj):
            if not contains_license_heading(page_output):
                message = f"No licensing information found on app page {page_obj.file.src_uri}"

                cls._warnings.append(message)

    @classmethod
    def get_report(cls):
        return cls._warnings
