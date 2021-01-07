# Content and formatting instructions

## General help
 - [Markdown syntax guide](https://www.markdownguide.org/tools/mkdocs/)
 - Also some special markup possible, e.g. coloured highlight boxes (please look at Markdown source for examples, and use preview)
 - When in doubt, check how other pages are formatted

## Organizing content
 - Try to make standalone articles with a good name (user knows to select it from the left menu)
 - The content should be as concise as possible, but as lengthy as needed.
 - The main user guide should document only what is specific to CSC environment, for general usage instructions link to the real manuals of the tool
   - Lengthier tutorials can be written under Support->Tutorials.
 - Don't make too deep hierarchy or too many entries per subcategory (combine very small pages)
 - Don't refer to the same page twice in mkdocs.yml -> sitemap breaks + weird menu action

## Accessibility
 - [General guidelines](https://www.saavutettavuusvaatimukset.fi/)
 - Docs specifics TBA
 - Make accessible content! In short:
      - `[Read more here](link-to-some-page)` is not accessible. `[Read more about free use cases](link-to-some-page)` is better.
      - Avoid long walls of text and long sentences
      - Lists and clear titles: good
      - Use descriptive alt texts for images and videos 
      - Avoid presenting something ONLY as a video, and use captions/subtitles in video. Also, do present import or difficult to follow things also with videos.
      - Use title **and** alt-text in images: `![This alt-text here explains what the picture contains](/img/image.png 'Title for image')` If the alt-text cannot explain the information contained in the image, mention that the text below contains it.
      - Avoid using loadable pdfs
      - Avoid using only color to signal some meaning

## Images, linked documents
 - Put all images in `/img` folder in docs root
 - Put large files in Allas (write access with project 2001659) bucket docs-files,
 e.g.  [https://a3s.fi/docs-files/README.md]( https://a3s.fi/docs-files/README.md)
      - new files easy to share with `a-publish your-file.tgz -b docs-files` 

## Syntax highlighting
 - Write SLURM flags in long format (`--nodes` instead of `-N`, etc.)
 - All examples should use minimum viable reserved resources. I.e don't write examples 
   with --t=72:00:00 / --gres=gpu:v100:4 / --cpus-per-task=40, if it not needed. 
   Users tend to use these as default values.
 - Internal links as `[cool page](page.md)`, `[stuff in
   page](page.md#anchor)`, `[stuff in other section](../other_section/page.md)`,
   `[stuff elsewhere](../other_section/page.md#anchor)` (no _internal_ links with https://...)
 - For code sections (marked with three backticks,\`\`\`) Mkdocs will by default try to auto-guess the 
   language for syntax highlighting. It's probably best to specify the language explicitly, e.g.  \`\`\`bash or  \`\`\`python
 - If you don't want any syntax highlighting, just use \`\`\`text
 - For a list of all supported languages see: http://pygments.org/docs/lexers/
 - Give commands, environment variables, command options, as well as partition 
   names between two backticks, i.e. \`srun\`, \`$LOCAL_SCRATCH\`, \`--gres\`, \`small\`

## Terminology
 - When referring collectively to compute servers, use term "CSC supercomputers". Puhti and Mahti should be used explicitly only
   when needed.
