"""Translate Markdown content using the OpenAI API.
"""
import os
import logging

import tiktoken
from openai import OpenAI, OpenAIError, APITimeoutError

from .constants import DEFAULTS
from .utils import check_environment, get_language
from .prompt import get_prompt
from .pages import PageContentWrapper


logger = logging.getLogger(__name__)

try:
    check_environment("LANG_CODE")

    client = OpenAI()
    client.timeout.connect = DEFAULTS.openai.timeout
    client.max_retries = DEFAULTS.openai.retries

    logger.info("OpenAI client initialized.")
except OpenAIError:
    logger.error("Failed to initialize OpenAI client.")
    raise
except:
    logger.error("Failed to initialize '%s'.", __name__)
    raise


def _estimate_max_tokens(openai_model, input_content):
    encoding = tiktoken.encoding_for_model(openai_model)
    input_tokens = len(encoding.encode(input_content))
    estimation = int(input_tokens * DEFAULTS.openai.max_tokens_multiplier)

    return min(estimation, DEFAULTS.openai.max_tokens)


def translate_markdown(content,
                       target_lang_code=os.getenv("LANG_CODE"),
                       openai_model=DEFAULTS.openai.model):
    """Translate Markdown content.
    """
    try:
        response = client.responses.create(
            model=openai_model,
            instructions=get_prompt(target_lang_code),
            input=content,
            max_output_tokens=DEFAULTS.openai.max_tokens
        )

        return response.output_text
    except APITimeoutError as e:
        logger.error("Request timed out: %s", str(e))
        raise
    except Exception as e:
        logger.error("Translation error: %s", str(e))
        raise

    return None


def translate_batch(items, translator=translate_markdown):
    """Process multiple Markdown files in one translation request.

    Raises AssertionError.
    """
    target_lang_name = get_language(os.getenv("LANG_CODE"))
    wrapped_content = PageContentWrapper(items)

    if wrapped_content.is_empty():
        logger.info("No files in batch.")
        return

    logger.info("Translating batch of %i files to %s...",
                len(wrapped_content),
                target_lang_name)

    wrapped_content.translation = translator(str(wrapped_content))
    for page, translation_result in wrapped_content:
        page.write_translation(translation_result)
