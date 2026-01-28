"""Provides a prompt with translation instructions.
"""
import string

from .constants import DEFAULTS
from .utils import get_dictionary, get_language


_entry_template = string.Template('    - "${src_term}": "${tgt_term}"')
_prompt_template = string.Template("""
You are a professional translator specializing in technical documentation. Translate the following Markdown content from ${source} to ${target}.

IMPORTANT GUIDELINES FOR PRESERVING INTERNAL LINKS:
1. Links to headers in a document must still work even if we have translated
2. For each translated header, add an explicit anchor with the original English header ID
3. Example:
    Original: ## Installation Guide
    Translated: ## Asennusopas { #installation-guide }
4. The ID format should be the original English header text in lowercase with spaces replaced by hyphens
5. Note that there should never be two hyphens after each other, e.g., header "A & B" has an anchor in english of A-B (not A--B even if there are two spaces).

Guidelines regarding metadata at the beginning of the content:
6. The Markdown content may contain metadata adhering to the following styles:
    - YAML front matter
    - MultiMarkdown
7. Only translate the value of the following keys if present in the metadata:
    - title
    - Title
    - description
8. Define a sibling key to hold the translated value.
9. The name of sibling key must be the name of the original key suffixed with an underscore followed by the ISO 639 language code of the translated language.
10. Example:
    Original: description: High-level interpreted language for numerical computations
    Translated: description_fi: Korkean tason tulkattava kieli numeeriseen laskentaan
11. Don't translate the values of any other keys of the metadata
12. Don't translate the names of the metadata keys themselves
13. Preserve the structure and format of the metadata

Guidelines regarding Markdown, HTML and URL formatting:
14. Preserve all Markdown formatting and structure
15. Preserve all links and their URLs
16. Keep code blocks and their content untranslated
17. Preserve all HTML tags and their attributes
18. Don't translate variable names or code snippets
19. Don't translate image file names or paths
20. VERY IMPORTANT: Do not enclose answer in a Markdown code block!

Guidelines for translating specific terms:
21. Use the following dictionary when translating these specific terms:
${dictionary}
""")


def get_prompt(target_lang_code):
    """Returns translation instructions as string.

    Raises AssertionError.
    """
    dictionary_lines = "\n".join(_entry_template.substitute(src_term=s,
                                                            tgt_term=t)
                                 for s, t
                                 in get_dictionary(target_lang_code).items())

    return _prompt_template.substitute(
        source=DEFAULTS.source_language,
        target=get_language(target_lang_code),
        dictionary=dictionary_lines
    )
