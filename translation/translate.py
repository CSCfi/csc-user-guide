#!/usr/bin/env python3
import os
import re
import argparse
import shutil
import logging
from pathlib import Path
from itertools import chain
from string import Template

from openai import OpenAI, OpenAIError


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure OpenAI client
try:
    client = OpenAI()
except OpenAIError as e:
    logger.error(f"Failed to initialize OpenAI client: {str(e)}")
else:
    print(f"""OpenAI client initialized

    API key: {client.api_key}
    Base URL: {client.base_url}
""")

# Define a template prompt
# Placeholders:
#   - $source: Language of the Markdown source content, e.g. "English"
#   - $target: The target language, i.e., the language to translate the content to, e.g. "Finnish"
#   - $markdown: The Markdown content to translate from $source to $target
prompt_template = Template("""
Translate the following Markdown content from $source to $target.

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

Additional guidelines:
14. Preserve all Markdown formatting and structure
15. Preserve all links and their URLs
16. Keep code blocks and their content untranslated
17. Preserve all HTML tags and their attributes
18. Don't translate variable names or code snippets
19. Don't translate image file names or paths

VERY IMPORTANT: Do not enclose answer in a Markdown code block!

Here's the content to translate:

$markdown
""")

def translate_markdown(content, target_language, source_language="English", openai_model="gpt-4.1", **_):
    """Translate Markdown content using LLM.

    Uses gpt-4.1 by default. This can be changed by including a supported model via the 'openai_model' keyword argument.
    """

    try:
        response = client.responses.create(
            model=openai_model,
            instructions="You are a professional translator specializing in technical documentation.",
            input=prompt_template.substitute(source=source_language,
                                             target=target_language,
                                             markdown=content),
            max_output_tokens=16000
        )

        return response.output_text
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise

def process_file(file_path, docs_dir, target_language, lang_dir, **kwargs):
    """Process a markdown file and create translated version in language folder.

    Passes kwargs to translate_markdown().
    """

    # Get relative path from docs directory
    rel_path = os.path.relpath(file_path, docs_dir)
    output_path = os.path.join(lang_dir, rel_path)

    # Create directory structure if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Skip if translation already exists and is newer than source (can be forced with force=True)
    if (not kwargs.get("force")) and os.path.exists(output_path):
        src_mtime = os.path.getmtime(file_path)
        dst_mtime = os.path.getmtime(output_path)
        if dst_mtime > src_mtime:
            logger.info(f"Translation up to date: {output_path}")
            return

    was_forced = kwargs.get('force')
    logger.info(f"Translating {rel_path} to {target_language}{' (forced)' if was_forced else ''}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    translated_content = translate_markdown(content, target_language, **kwargs)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)

    logger.info(f"Created {output_path}")

def copy_assets(docs_dir, lang_dir):
    """Copy non-markdown files (assets) to the language directory."""
    for root, _, files in os.walk(docs_dir):
        # Skip language directories
        if any(lang in root for lang in ['/fi/', '/fr/', '/de/', '/es/']):
            continue

        for file in files:
            if not file.endswith('.md'):
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(src_file, docs_dir)
                dst_file = os.path.join(lang_dir, rel_path)

                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)

                # Copy file if it doesn't exist or if source is newer
                if not os.path.exists(dst_file) or os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                    shutil.copy2(src_file, dst_file)
                    logger.info(f"Copied asset: {rel_path}")

def col_width(rows, col_i):
    """Return the length of the longest item in
        column 'col_i' of 2D iterable 'rows'.
    """
    return len(max([*zip(*rows)][col_i], key=len))

def file_in_iterable(f: Path, iterable) -> bool:
    """Return True if a Path object pointing to the same file
        as f is found in iterable. Raises FileNotFoundError if
        either f or any f_ in iterable is not found in the
        filesystem.
    """
    return any(f.samefile(f_) for f_ in iterable)

def main():
    parser = argparse.ArgumentParser(description='Translate MkDocs markdown files to multiple languages.')
    parser.add_argument('file', type=Path, nargs='*', help="Path to documentation file")
    parser.add_argument('-d', '--docs-dir', type=Path, default=Path('docs'), help='Documentation directory (default: docs)')
    parser.add_argument('-l', '--language', type=str, required=True, help='Target language (e.g., Finnish)')
    parser.add_argument('-c', '--lang-code', type=str, required=True, help='Language code (e.g., fi)')
    parser.add_argument('-g', '--glob', type=str, metavar='PATTERN', default='**/*.md', help='Replace the default pattern **/*.md with PATTERN (relative to DOCS_DIR, --glob \'\' to disable)')
    parser.add_argument('-e', '--exclude', type=Path, metavar='EXCLUDED', nargs='+', help='Exclude the file EXCLUDED')
    parser.add_argument('-a', '--copy-assets', action='store_true', default=False, help='Copy non-Markdown assets (images, etc.)')
    parser.add_argument('-m', '--model', type=str, default='gpt-4.1', help='Use the model MODEL for translation (default: GTP-4.1)')
    parser.add_argument('--force', action='store_true', default=False, help='Force retranslation of up-to-date files')
    parser.add_argument('--dry-run', action='store_true', default=False, help='Only perform a dry-run, i.e. only print parameters')
    args = parser.parse_args()

    docs_dir = args.docs_dir
    target_language = args.language
    lang_code = args.lang_code
    lang_dir = docs_dir.with_name(f"{docs_dir.name}.{lang_code}")
    excluded_files = args.exclude or []
    positional_files = args.file or []
    globbed_files = [*docs_dir.glob(args.glob)] if args.glob else []
    source_files = []

    # Add files from positional arbuments
    source_files.extend(f for f in positional_files
                        if f.is_file() and not file_in_iterable(f, excluded_files))
    # Add files from globbing
    source_files.extend(f for f in globbed_files
                        if f.is_file() and not file_in_iterable(f, chain(excluded_files, source_files)))

    if not args.dry_run:
        # Create language directory
        lang_dir.mkdir(exist_ok=True)

        # Process markdown files
        for file_path in source_files:
            # Skip files in language directories
            if f'/{lang_code}/' in str(file_path) or any(f'/{l}/' in str(file_path) for l in ['fi', 'fr', 'de', 'es']):
                continue

            process_file(file_path, docs_dir, target_language, lang_dir, force=args.force, openai_model=args.model.lower())

        if args.copy_assets:
            # Copy assets (images, etc.)
            copy_assets(docs_dir, lang_dir)

        logger.info(f"Translation to {target_language} complete")
    else:
        # Prepare and print a dry-run report
        report = (
            ("Documentation directory:", str(docs_dir)),
            ("Language [code]:", f"{target_language} [{lang_code}]"),
            ("Destination directory:", str(lang_dir)),
            ("Glob:", f"'{args.glob}'" if args.glob else '<disabled>'),
            ("OpenAI model:", args.model),
            ("Copy assets:", f"{'Yes' if args.copy_assets else 'No'}"),
            ("Force retranslation:", f"{'Yes' if args.force else 'No'}")
        )
        header_lines = [k.ljust(col_width(report, 0)+1) + v
                        for k,v in report]
        source_lines = [str(source) for source in source_files] if source_files else ["No files!"]

        print("DRY-RUN".rjust(col_width(report, 0), '-') + '-'*(col_width(report, 1)+1),
              *header_lines,
              sep="\n")
        print(f"Source files ({len(source_files)}):",
              *source_lines,
              sep="\n  ")

if __name__ == "__main__":
    main()
