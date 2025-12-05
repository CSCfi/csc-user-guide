"""Translate Markdown content using the OpenAI API.
"""
import sys
import logging

from openai import OpenAI, OpenAIError

from .prompt import prompt_template
from .classes import ContentWrapper


logger = logging.getLogger(__name__)

#Configure OpenAI client
try:
    client = OpenAI()
except OpenAIError as e:
    logger.error("Failed to initialize OpenAI client: %s", str(e))
    sys.exit(1)
else:
    logger.info("OpenAI client initialized")


def _translate_markdown(content,
                       target_language,
                       n=1,
                       source_language="English",
                       openai_model="gpt-5"):
    """Translate Markdown content from source_language to target_language
    using model openai_model.
    """
    try:
        response = client.responses.create(
            model=openai_model,
            instructions=prompt_template.substitute(source=source_language,
                                                    target=target_language),
            input=content,
            max_output_tokens=16000*n
        )

        return response.output_text
    except Exception as e:
        logger.error("Translation error: %s", str(e))
        raise


def translate_batch(items, target_language):
    """Process multiple Markdown files in one translation request.

    items
        Iterable of DiffPath objects.

    target_language
        The target language, i.e., the language to translate the
        content to, e.g. "Finnish".
    """

    wrapped_content = ContentWrapper(items)

    if wrapped_content.is_empty():
        logger.info("No files to translate.")
        return

    logger.info("Translating batch of %i files to %s...",
                len(wrapped_content),
                target_language)

    wrapped_content.translation = _translate_markdown(str(wrapped_content),
                                                      target_language,
                                                      n=len(wrapped_content))
    for diff_path, translation_result in wrapped_content:
        diff_path.write_translation(translation_result)
