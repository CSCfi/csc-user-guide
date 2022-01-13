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
 - Make accessible content! In short:
 - **Links:** Link text needs to be descriptive
   - `[Read more here](link-to-some-page.md)` is not accessible. `[Read more about free use cases](link-to-some-page.md)` is better.
   - Pure URL is NOT an option! Imagine reading it: h-t-t-p-s colon slash slash...
   - If, for some rare reason, writing a descriptive link text is not possible, you can use html and aria-label: `<a href="https://code.visualstudio.com" aria-label="This is readable by screen readers">Visual Studio Code</a>` This label is read by the screen readers but is not visible to others.
- **Images:** 
   - Use descriptive alt-text and  in images:  `![This alt-text is for screen readers](/img/image.png 'Helpful text shown as mouse-over')` 
   - If the alt-text cannot explain the information contained in the image, mention that the text below contains it.
   - If image is only decorative, you can leave alt-text empty.
   - Alt-txt should not be too long (8+ words)
   - You can use the same text in alt-txt and mouse over
   - Images should be of high contrast and large enough font within them
- **Videos:** 
   - Use `title` to describe the video content: `<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/PrgMFna3DKw?rel=0" title="Intro to Geocomputing" width="560"></iframe>`
   - Avoid presenting something ONLY as a video, and use captions/subtitles in video (easy to add in Youtube). 
   - Also, do present important or difficult to follow things also with videos.
- Headers:
   - Only one h1 (#) per page 
   - Follow heading structure (don't go from h1 to h3 = # to ###). Don't make deep structures (they will confuse the table of contents).
- Avoid long walls of text and long sentences
- Lists and clear titles: good
- Avoid using loadable pdfs
- Avoid using only color to signal some meaning

## Embedded Videos
 - Iframes to youtube need to use the `srcdoc` attribute instead of `src`, this is due to a workaround
 we use to avoid cookies if consent has not been granted. 
 
 ## Links
 - For internal links, include `.md` in the target:
     - `[cool page](page.md)`
     - `[stuff in page](page.md#anchor)`
     - `[stuff in other section](../other_section/page.md)`
     - `[stuff elsewhere in page](../other_section/page.md#anchor)` 
     - **Do not make** _internal_ links with `https://...`
 - Common issues:
     - Incorrect number of parent directories (`../../accounts/how-to-create-new-user-account.md` vs `../accounts/how-to-create-new-user-account.md`)
     - including `/` between page and anchor
         - **Correct**: `../../accounts/how-to-create-new-user-account.md#getting-student-accounts-for-courses` 
         - **Incorrect**: ` ../../accounts/how-to-create-new-user-account.md/#getting-student-accounts-for-courses`

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
 - For code sections (marked with three backticks,\`\`\`) Mkdocs will by default try to auto-guess the 
   language for syntax highlighting. It's probably best to specify the language explicitly, e.g.  \`\`\`bash or  \`\`\`python
      - *Note!* Add a blank line _after_ the three-ticks-codeblock! (Also two whitespaces after ticks work, but that's unofficial dialect)
 - If you don't want any syntax highlighting, just use \`\`\`text
 - For a list of all supported languages see: http://pygments.org/docs/lexers/
 - Give commands, environment variables, command options, as well as partition 
   names between two backticks, i.e. \`srun\`, \`$LOCAL_SCRATCH\`, \`--gres\`, \`small\`
 - Refer to servicedesk via the docs contact page: as in `[contact ServiceDesk](/support/contact/)`  
      - Page has email, service times, phone, support request how-to
 
## Redirecting pages
 - If there's an url that has been linked to from the outside a lot and it changes (disappears), a (temporary) redirect can be made
 - Create a file with the name-of-the-old-page`.html` (or index.html if it was done that way) and as the content:
```
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="1; url='new-page/#anchor-on-that-page'" />
  </head>
  <body>
    <p><a href="new-page/#anchor-on-that-page">Dataset content reorganized!</a>.</p>
  </body>
</html>
```

 - edit `new-page` (and the anchor, if there, otherwise just remove) to match
 - to pass the tests, add the page to `tests/python_link_tests/whitelist`, too

## Terminology
 - When referring collectively to compute servers, use term "CSC supercomputers". Puhti and Mahti should be used explicitly only
   when needed.

## Advanced: page metadata

 - All pages use the _site_description_ metadata by default: 
    - _site_description: Instructions and user guides for the CSC supercomputers, cloud services, storage and software, including FAQ and tutorials_
 - This can be changed per page by adding this to the page top:
```
---
description: Relevant keywords describing this page
---
```
 - This _may_ be shown next to the url and title in a google search and this _may_ help in search result ranking.
 - Some [discussion on good metadata](https://themeisle.com/blog/meta-description-examples/)
 - Examples in docs: support/support-howto.md, TBA
