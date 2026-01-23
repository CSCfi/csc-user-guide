"""Translate Markdown content using the OpenAI API.
"""
import sys
import logging

import tiktoken
from openai import OpenAI, OpenAIError, APITimeoutError

from . import DEFAULTS, TARGET_LANGUAGE
from .prompt import prompt_template
from .pages import PageContentWrapper


logger = logging.getLogger(__name__)

#Configure OpenAI client
try:
    client = OpenAI()
    client.timeout.connect = DEFAULTS.openai.timeout
    client.max_retries = DEFAULTS.openai.retries
except OpenAIError as e:
    logger.error("Failed to initialize OpenAI client: %s", str(e))
    sys.exit(1)
else:
    logger.info("OpenAI client initialized.")


def _estimate_max_tokens(openai_model, input_content):
    encoding = tiktoken.encoding_for_model(openai_model)
    input_tokens = len(encoding.encode(input_content))
    estimation = int(input_tokens * DEFAULTS.openai.max_tokens_multiplier)

    return min(estimation, DEFAULTS.openai.max_tokens)


def _translate_markdown(content,
                        target_language,
                        source_language=DEFAULTS.source_language,
                        openai_model=DEFAULTS.openai.model):
    """Translate Markdown content from source_language to target_language
    using model openai_model.
    """
    try:
        response = client.responses.create(
            model=openai_model,
            instructions=prompt_template.substitute(source=source_language,
                                                    target=target_language),
            input=content,
            max_output_tokens=_estimate_max_tokens(openai_model, content)
        )

        return response.output_text
    except APITimeoutError as e:
        logger.error("Request timed out: %s", str(e))
        raise
    except Exception as e:
        logger.error("Translation error: %s", str(e))
        raise

    return None


def translate_batch(items, translator=_translate_markdown):
    """Process multiple Markdown files in one translation request.

    items
        Iterable of DiffPath objects.

    target_language
        The target language, i.e., the language to translate the
        content to, e.g. "Finnish".
    """

    wrapped_content = PageContentWrapper(items)

    if wrapped_content.is_empty():
        logger.info("No files in batch.")
        return

    logger.info("Translating batch of %i files to %s...",
                len(wrapped_content),
                TARGET_LANGUAGE)

    wrapped_content.translation = translator(str(wrapped_content),
                                                 TARGET_LANGUAGE)
    for page, translation_result in wrapped_content:
        page.write_translation(translation_result)
