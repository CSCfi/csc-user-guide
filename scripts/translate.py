#!/usr/bin/env python3
import os
import re
import argparse
import openai
from pathlib import Path
import shutil
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure OpenAI client
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
print(f"Using API Key: {openai.api_key}")


def translate_markdown(content, target_language, source_language="English"):
    """Translate markdown content using LLM."""
    try:
        prompt = f"""
        Translate the following markdown content from {source_language} to {target_language}.

        IMPORTANT GUIDELINES FOR PRESERVING INTERNAL LINKS:
        1. Links to headers in a document must still work even if we have translated
        2. For each translated header, add an explicit anchor with the original English header ID
        3. Example:
           Original: ## Installation Guide
           Translated: ## Asennusopas {{#installation-guide}}
        4. The ID format should be the original English header text in lowercase with spaces replaced by hyphens
        5. Note that there should never be two hyphens after each other, e.g., header "A & B" has an anchor in english of A-B (not A--B even if there are two spaces).
           
        Additional guidelines:
        4. Preserve all Markdown formatting and structure
        5. Preserve all links and their URLs
        6. Keep code blocks and their content untranslated
        7. Preserve all HTML tags and their attributes
        8. Don't translate variable names or code snippets
        9. Don't translate image file names or paths

        VERY IMPORTANT: Do not enclose answer in a markdown code block!
        
        Here's the content to translate:
        
        {content}
        """
        
        response = openai.chat.completions.create(
            model="gpt-4o", 
            messages=[
                {"role": "system", "content": "You are a professional translator specializing in technical documentation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=8192
        )
        
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise

def process_file(file_path, docs_dir, target_language, lang_dir):
    """Process a markdown file and create translated version in language folder."""
    # Get relative path from docs directory
    rel_path = os.path.relpath(file_path, docs_dir)
    output_path = os.path.join(lang_dir, rel_path)
    
    # Create directory structure if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Skip if translation already exists and is newer than source
    if os.path.exists(output_path):
        src_mtime = os.path.getmtime(file_path)
        dst_mtime = os.path.getmtime(output_path)
        if dst_mtime > src_mtime:
            logger.info(f"Translation up to date: {output_path}")
            return
    
    logger.info(f"Translating {rel_path} to {target_language}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    translated_content = translate_markdown(content, target_language)
    
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

def update_mkdocs_config(docs_dir, language_name, language_code):
    """Update mkdocs.yml with i18n configuration if needed."""
    config_file = os.path.join(docs_dir, '..', 'mkdocs.yml')
    
    if not os.path.exists(config_file):
        logger.warning(f"mkdocs.yml not found at {config_file}")
        return
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if i18n plugin is already configured
    if 'mkdocs-static-i18n' in content or 'i18n:' in content:
        logger.info("i18n plugin already configured in mkdocs.yml")
        return
    
    # Simple string replacement to add i18n plugin configuration
    # Note: This is a basic approach. For complex YAML files, consider using a YAML parser
    i18n_config = f"""
plugins:
  - search
  - i18n:
      default_language: en
      languages:
        en:
          name: English
          build: true
        {language_code}:
          name: {language_name}
          build: true
      docs_structure: folder
      fallback_to_default: true
"""

    # Check if plugins section exists
    if 'plugins:' in content:
        # Add i18n to existing plugins
        content = re.sub(r'plugins:', f'plugins:\n  - i18n:\n      default_language: en\n      languages:\n        en:\n          name: English\n          build: true\n        {language_code}:\n          name: {language_name}\n          build: true\n      docs_structure: folder\n      fallback_to_default: true', content, count=1)
    else:
        # Add the entire plugins section
        content += i18n_config
    
    # Backup the original file
    shutil.copy2(config_file, f"{config_file}.backup")
    
    # Write the updated configuration
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    logger.info(f"Updated mkdocs.yml with i18n configuration")

def main():
    parser = argparse.ArgumentParser(description='Translate MkDocs markdown files to multiple languages.')
    parser.add_argument('--docs-dir', default='docs', help='Documentation directory')
    parser.add_argument('--language', required=True, help='Target language (e.g., Finnish)')
    parser.add_argument('--lang-code', required=True, help='Language code (e.g., fi)')
    parser.add_argument('--force', action='store_true', help='Force retranslation of all files')
    parser.add_argument('--update-config', action='store_true', help='Update mkdocs.yml with i18n configuration')
    args = parser.parse_args()
    
    docs_dir = Path(args.docs_dir)
    lang_code = args.lang_code
    target_language = args.language
    
    # Update mkdocs.yml if requested
    if args.update_config:
        update_mkdocs_config(docs_dir, target_language, lang_code)
    
    # Create language directory
    lang_dir = Path(f"{docs_dir}.{lang_code}")
    os.makedirs(lang_dir, exist_ok=True)
    
    # Process markdown files
    for file_path in docs_dir.glob('**/*.md'):
        # Skip files in language directories
        if f'/{lang_code}/' in str(file_path) or any(f'/{l}/' in str(file_path) for l in ['fi', 'fr', 'de', 'es']):
            continue
        
        process_file(file_path, docs_dir, target_language, lang_dir)
    
    # Copy assets (images, etc.)
    copy_assets(docs_dir, lang_dir)
    
    logger.info(f"Translation to {target_language} complete")

if __name__ == "__main__":
    main()
