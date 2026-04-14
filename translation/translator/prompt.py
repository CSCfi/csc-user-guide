"""Provides a prompt with translation instructions.
"""
import string

from .constants import DEFAULTS
from .utils import get_dictionary, get_language


_entry_template = string.Template('    - "${src_term}": "${tgt_term}"')
_dictionary_template = string.Template("""
6. Translating specific terms:
- Use the following dictionary when translating these specific terms:
${entries}
""")
_prompt_template = string.Template("""
You are an expert technical translator with extensive experience translating technical documentation for CSC - IT Center for Science. Translate the following Markdown document from ${source} to ${target} according to these rules:

1. General Translation Guidelines
- Produce natural and fluent $target language with proper grammar and inflections, ensuring proper nouns are inflected correctly according to standard usage.
- Preserve the Markdown formatting exactly as in the source.

2. Header Translation and Internal Links
- Translate each header and always add an explicit anchor using the original English header ID.
- Strictly follow the example:
    Original: ## Installation Guide
    Translated: ## Asennusopas { #installation-guide }
    Note the spaces around the text.
- Always translate link headers but not the anchor.
- Strictly follow the Example:
    Original: [Create a CSC account](#1-create-a-csc-account)
    Translated: [Luo CSC-käyttäjätunnus](#1-create-a-csc-account)

3. Metadata Translation (YAML or MultiMarkdown)
- Only translate the values of these keys (if present): title, Title, description.
- Suffix the sibling key with a language code.
- Follow the Example:
    Original: description: High-level interpreted language for numerical computations
    Translated: description_fi: Korkean tason tulkattava kieli numeeriseen laskentaan
- Do not translate metadata key names themselves or other metadata values.

4. Code, Variables, and Assets
- Do not translate code blocks, variable names, or code snippets.
- Preserve all HTML tags and attributes.
- Do not translate image file names or paths.

5. Translating the word "upload"
- Do not confuse with "download", which is also "ladata".
- Clarify the meaning by specifying direction, e.g., "lataa SD Connectiin", if there's no destination mentioned, use "lataa palveluun".

${dictionary}

7. Do not leave any text untranslated unless otherwise specified. Output must be publication-ready and technically precise.
""")


def get_prompt(target_lang_code):
    """Returns translation instructions as string.
    """
    dictionary_entries = get_dictionary(target_lang_code)
    dictionary_lines = "\n".join(_entry_template.substitute(src_term=s,
                                                            tgt_term=t)
                                 for s, t
                                 in dictionary_entries.items())
    dictionary = _dictionary_template.substitute(entries=dictionary_lines)

    return _prompt_template.substitute(
        source=DEFAULTS.source_language,
        target=get_language(target_lang_code),
        dictionary=dictionary if len(dictionary_entries) > 0 else ""
    )
