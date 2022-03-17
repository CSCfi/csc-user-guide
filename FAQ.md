# Frequently asked questions

The [contributing guide](CONTRIBUTING.md) outlines the basic steps of starting contributing to the CSC user guide, making pull requests (PRs) and reviewing them. This page highlights in more detail common questions and pitfalls you may encounter during the process.

## How to edit an existing page?

## How to create a new page?

## How to add an image or embed a video in a page?

To add an image:

* Add the image you want to include to the `/docs/img/` directory.
* Include the image in your page using the markdown syntax `![This is alt-text for screen readers](/path/to/docs/img/my-image.png 'This is mouse-over text')`
* **Note the importance of alt-text and mouse-over (title) text! These are required to make the content accessible for all.**
* Alt-txt should not be too long (8+ words). If the alt-text cannot explain the information contained in the image, mention that the text below contains it.
* You can use the same text in alt-text and mouse-over text
* Images should be of high contrast and large enough font within them.

To embed a video from an external source:

* You need to use HTML syntax, for example, `<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/PrgMFna3DKw?rel=0" title="Intro to Geocomputing" width="560"></iframe>`
* Use the `title` option to describe the content of the video. The use of `srcdoc` is also required (instead of plain `src`) to avoid cookies if consent not granted.
* Use captions/subtitles (easy to add in Youtube).

## My PR did not pass the tests, what to do?

Tests are run to check, for example, that your pull request complies with the CSC Docs style guide and that there are no broken links. If any such errors are found in your commits, the tests will not pass and you need to figure out what went wrong:

1. Find out which tests did not pass under the notification `Some checks were not successful` in the Review-dialogue (marked with a red x and text `Failing after X - Build Failed`).
2. To the right of the failed test, click `Details`, which opens the `Checks` tab.
3. Under the `Build Failed` section, click the link at `The build failed` to open the Travis CI page with logged details on the build.
4. Scan through the Job log for any text marked in red. These are errors that the test found, and the reason for them is written before the red text. 
5. An example error is shown below. Here, the `link_check.py` test script was run to see whether any links were broken. The test found two broken section links and it tells you in which files and on which lines the errors are.

```console
$ python3 tests/python_link_tests/link_check.py
The section link namd.md#batch-script-example-for-mahti in file docs/apps/namd.md on line 33 is broken
The section link cp2k.md#example-batch-script-for-mahti-using-mixed-mpi-openmp-parallelization in file docs/apps/cp2k.md on line 81 is broken
No broken file links found
No hidden files found
The command "python3 tests/python_link_tests/link_check.py" exited with 1.
```

6. Fix the errors, commit and push the revised files to the same branch and the tests should now pass.

## How can I preview my edits?

You can preview how the Docs CSC page would look like with your changes included in two ways:

1. Locally using the MkDocs tool
      * Install mkdocs 
2. Using the  

## How and who should I ask to review my PR?

1. Ask someone (one or two persons) who knows the *content* of the work you have committed to review your pull request. This is done in your pull request view using the right-hand-side panel, under `Reviewers`. The panel will suggest a few names for you based on, for example, who has edited the same pages recently. To view more reviewer options, click the cogwheel in the upper right corner of the `Reviewers` panel. If you're still unsure who to pick, you can always drop a message in the Rocket Chat channel #docs.csc.fi. Always request someone to review your PR, otherwise there's a high chance that it will just linger around.
2. To help the reviewer to get started with going through your PR, you should leave a comment in the PR with a link to the preview page `https://csc-guide-preview.rahtiapp.fi/origin/your-branch/path/to/page/` with your additions/changes (edit `/your-branch/path/to/page/` as needed). Any other comments are of course also helpful for the reviewer to understand what you have done.
3. Once the reviewer has gone through your PR, they will request changes or approve the PR. Once approved, someone with merge permissions will merge your PR to the master branch. You can always ping the Rocket Chat channel #docs.csc.fi to expedite the merging of your PR.
