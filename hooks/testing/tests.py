"""Content testing module.
"""

def _testmethod(method):
    test_name = method.__qualname__

    def collect_results(cls, *args, **kwargs):
        if test_name not in cls.test_runs:
            cls.test_runs[test_name] = {"description": method.__doc__,
                                        "results": [],
                                        "passed": 0,
                                        "failed": 0}

        results = method(cls, *args, **kwargs)

        if results is None:
            return

        if not len(results) > 0:
            cls.test_runs[test_name]["passed"] += 1
        else:
            cls.test_runs[test_name]["failed"] += 1

        cls.test_runs[test_name]["results"].extend(results)

    return collect_results


class DocsTests:
    """The content test automation suite.
    """
    LICENSE_HEADING_LEVEL_RANGE = (2, 4) # h2 & h3

    test_runs = {}

    @classmethod
    @_testmethod
    def no_fixmes_are_present_in_documentation_sources(cls, source_files):
        """None of the documentation source files should include the word 'FIXME'.
        """
        results = []

        for src_file in source_files:
            if src_file.is_documentation_page():
                src_lines = src_file.content_string.split("\n")
                fixme_indices = []

                for i, line in enumerate(src_lines):
                    if "FIXME" in line:
                        fixme_indices.append(i)

                if fixme_indices:
                    lines = ', '.join(map(lambda i: str(i+1), fixme_indices))
                    message = f"FIXME found on {src_file.src_uri} line(s) {lines}!"

                    results.append(message)

        return results

    @classmethod
    @_testmethod
    def app_page_contains_license_heading(cls, page_obj, processor):
        """All app pages must include a license section.
        """
        try:
            if not page_obj.meta["catalog"].get("unchecked", False):
                # App page where "unchecked" is not defined or not True
                return ([f"No licensing information found on app page '{page_obj.file.src_uri}'!"]
                        if not processor.license_found else [])

            # An "unchecked" app page, ignored
            return None
        except KeyError:
            # Not an app page
            return None

    @classmethod
    @_testmethod
    def doc_page_has_no_internal_links_to_production_domain(cls, page_obj, checker):
        """No internal links should point to the site domain.
        """
        return [f"The hyperlink '{text}' on page {page_obj.file.src_uri}"
                f" points to '{checker.netloc}'!"
                for text in checker.hits]

    @classmethod
    def log_results(cls, logger):
        """Log the test results with 'logger'.

           Failed test cases are logged with level WARNING.
        """
        for name, case in cls.test_runs.items():
            summary = f"{name}: [Passed: {case['passed']}, Failed: {case['failed']}]"

            logger.info(summary)
            for line in case["results"]:
                logger.warning(line)
            if len(case["results"]) > 0:
                logger.info(case["description"])
