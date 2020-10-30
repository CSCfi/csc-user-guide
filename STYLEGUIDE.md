# Content and formatting instructions

 - Try to make standalone articles with a good name (user knows to select it from the left menu)
 - The content should be as concise as possible, but as lengthy as needed.
 - The main user guide should document only what is specific to CSC environment, for general usage instructions link to the real manuals of the tool
   - Lengthier tutorials can be written under Support->Tutorials.
 - Put all images in root images folder
 - Write SLURM flags in long format (--nodes instead of -N, etc.)
 - All examples should use minimum viable reserved resources. I.e don't write examples with --t=72:00:00 / --gres=gpu:v100:4 / --cpus-per-task=40, if it not needed. Users tend to use these as default values.
 - Don't make too deep hierarchy or too many entries per subcategory (combine very small pages)
 - When in doubt, check how other pages are formatted
 - Internal links as `page.md`, `page.md#anchor`, `../other_section/page.md`,
   `../other_section/page.md#anchor`
 - For code sections (marked with three backticks,\`\`\`) Mkdocs will by default try to auto-guess the language for syntax highlighting. It's probably best to specify the language explicitly, e.g.  \`\`\`bash or  \`\`\`python
If you don't want any syntax highlighting, just use \`\`\`text
For a list of all supported languages see: http://pygments.org/docs/lexers/
 - Don't refer to the same page twice in mkdocs.yml -> sitemap breaks + weird menu action
 - When referring collectively to compute servers, use term "CSC supercomputers". Puhti and Mahti should be used explicitly only
   when needed.
 - Give commands, environment variables, command options, as well as partition names between two backticks, i.e. \`srun\`, \`$LOCAL_SCRATCH\`, \`--gres\`, \`small\`
 - Put large files in Allas (write access with project 2001659) bucket docs-files,
 e.g.  [https://a3s.fi/docs-files/README.md]( https://a3s.fi/docs-files/README.md)
      - new files easy to share with `a-publish your-file.tgz -b docs-files` 

