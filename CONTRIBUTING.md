# Contributing

- [Contributing](#contributing)
  - [Starting as a writer](#starting-as-a-writer)
  - [For the impatient](#for-the-impatient)
  - [Making changes using pull requests](#making-changes-using-pull-requests)
    - [Overview](#overview)
      - [Writer](#writer)
      - [Reviewer](#reviewer)
      - [Admin](#admin)
    - [Previewing active branches](#previewing-active-branches)
    - [Making pull requests in the web GUI](#making-pull-requests-in-the-web-gui)
    - [Making pull requests on the command line](#making-pull-requests-on-the-command-line)
    - [Making pull requests in the desktop application](#making-pull-requests-in-the-desktop-application)
  - [Previewing the website using MkDocs](#previewing-the-website-using-mkdocs)
  - [Building the website using the included Dockerfile](#building-the-website-using-the-included-dockerfile)
  - [Hosting the website on OpenShift](#hosting-the-website-on-openshift)
  - [Finding pages that might be outdated](#finding-pages-that-might-be-outdated)

## Starting as a writer

CSC staff: do these two things _first_:

1. Join the Git organization [CSCfi](https://github.com/CSCfi) by sending email to vcs-support@csc.fi.
2. Then [join here the CSC employees team](https://github.com/orgs/CSCfi/teams/employees/members). Membership
gives you permissions to edit source files that build the user guide. (Wait for a confirmation email.)

The rest of this document describes the workflow in Github as well as instructions for previewing and
deploying the documentation. There are more resources available, though:

- [STYLEGUIDE.md](STYLEGUIDE.md) &mdash; Content and formatting instructions
- [FAQ.md](FAQ.md) &mdash; More in-depth explanations of common questions you might encounter while contributing
- [GETTING_STARTED.md](GETTING_STARTED.md) &mdash; Setting up a local development environment
- [Reference card](docs.csc.fi/ref) &mdash; On the available elements
    - [Markdown source for Reference card](docs/ref.md)

## For the impatient

Once you've completed the steps above:

* In [docs.csc.fi](https://docs.csc.fi) go to the page you want to edit and click the pen icon at top right
* (sign in to GitHub) and edit the content
* Scroll down to commit changes (create a new branch) -> make a pull request
* Assign a reviewer

## Making changes using pull requests

The csc-user-guide repository uses the 'master' as the default
branch. You can make changes in web gui, command line or desktop application.

Master branch is protected. You cannot make changes to it directly, but you
must use pull requests.

### Overview

#### Writer

 - Create your own branch from master (or work in an already existing branch, if agreed)
 - Create / bring there the content you want to work with. Pay attention to file naming!
 - Make sure the data is 100% correct (no Taito or other old references, language is correct, commands work, style is same as in other articles)
 - When creating a new article, add it also to the mkdocs.yml navigation OR in the index.md file in that folder (in case of FAQs for example). For new software (=apps) pages, add them to by_discipline.md. **Do not** manually edit by_license.md or index.md files under apps since these are automatically generated. See also the [FAQ](FAQ.md#how-to-include-my-new-page-in-the-navigation-panel).
 - Make a pull request for your work to be added to Master
    - Look at the test results of your PR: if they are red, check what's wrong and commit to the PR directly to fix it. See the [FAQ](FAQ.md#my-pr-did-not-pass-the-tests-what-to-do) for instructions.
    - Assign one or more reviewers, try to choose someone who knows the _content_. See also the [FAQ](FAQ.md#how-and-who-should-i-ask-to-review-my-pr).
        - Please add a link to the rahtiapp-preview page `https://csc-guide-preview.2.rahtiapp.fi/origin/<your-branch-name>/rest-of-url/`) in the Pull Request description to help reviewer.
    - You can also add a label to your PR. For example, if your edit is minor (e.g. fixed link or typo), you can add the label "trivial change" to expedite the reviewing process.
    - Pull requests which do not meet the requirements will not be accepted. Note that you can keep committing to a pull request after it has been submitted.
        - If your commits aren't showing up on the pull request, i.e., the pull request isn't updating when making new commits, try switching the base branch ('Edit' button, top-right) from `master` to something else and then back again.
    - Write meaningful pull request messages, so it is easier for reviewers to do their job.
    - Communicate! Use "WIP" (= Work In Progress) in your pull request title, if you don't wish the branch to be merged to master (i.e. you want to continue working with it).
 - Once your PR has been accepted, remove the temporary branch (if not deleted automatically at merge)

#### Reviewer

If you get a request to review a pull request, please contribute to help publish the changes!

 - See the [FAQ](FAQ.md#i-was-asked-to-review-a-pr-what-should-i-do) for detailed instructions.
 - Follow the link (or navigate to the pull request)
 - Make sure the tests pass
 - Edit the pages as needed (perhaps via the Web GUI)
     - It's ok to edit small typos directly in the text. Request changes if more extensive revisions are needed.
 - Once you're happy with the content, in the "Files changed" tab click "Review changes" -> "Approve"
 - Anyone can be a reviewer, while pull requests can be accepted only by a smaller group of people

#### Admin

If you see an approved branch:

 - "Squash and merge" it
 - Delete the (now unnecessary) branch (if not deleted automatically at merge)
 - Occasionally the number of (unnecessary) branches grows: prune.

**Note:** If you make bigger changes to the (main) categories / menu on the left, it might affect some links used on our webpages. Please communicate these changes, for example in the RC-channel #research.csc.fi.

### Previewing active branches

The GitHub web interface gives a preview (also while editing) but it does not render all syntax used in mkdocs correctly.
A full preview for ongoing work is available for all branches: <https://csc-guide-preview.2.rahtiapp.fi/origin/>. For more details, see the [FAQ](FAQ.md#how-can-i-preview-my-edits).

### Making pull requests in the web GUI

- In the master branch, navigate to the page you want to edit.
- Click the pen-logo at the top right to edit.
- Once ready, at the bottom choose "Create new branch from this commit and start a pull request". Note, that you should give the branch a descriptive name at this point.
- If you wish to edit an already existing branch, first change to the correct branch in the upper left "branch" button, next to the path to the file.
- If you found an error in the pull request of your own branch, you can commit to it directly instead of creating another pull request (the two choices at the bottom).

### Making pull requests on the command line

Overview:

 - Update your local repository
 - Make a new branch from the master branch
 - Work and commit in your new branch
 - Push changes to GitHub
 - Make a pull request to merge changes from your new branch into the master branch
 - Ask a person to review and merge the changes

 To get a copy of the repository, you need to clone it.

 ```bash
 git clone https://github.com/CSCfi/csc-user-guide.git
 ```

 All other Git commands are given inside the directory that you have
 cloned.

 ```bash
 cd csc-user-guide
 ```

When you have cloned the repository, master branch is what you
see. If you are unsure which branch you are in, you can run `git
branch`. The active branch can be changed with the `git checkout`
command.

Method:

```bash
git pull
git checkout master # switch to master branch
git checkout -b your_branch_name # create a new (temporary) branch and switch to it
# create some nice content, add files
git add example-file.md
git status # check the status
git commit -v
git push origin your_branch_name
```

Now, in the GitHub web GUI you can create a pull request, ask a person to review
it and (some admin to) merge the changes. After the PR has been merged, the branch
on GitHub should get deleted automatically (delete manually if not).

**Tip 1.** Git uses [Vim](https://www.vim.org) as the default editor for commit
messages. It is possible to change the default editor, but below are
the most important commands if you do not want to do it right now.

```
i    Enter insert mode
Esc  Exit insert mode
:wq  Save and exit
```

**Tip 2.** See instructions on [how to write a good Git commit
message](https://chris.beams.io/posts/git-commit/).

**Tip 3.** If pushing fails, the most probable reason is that somebody
else has made edits while you were editing. This situation is called a
conflict. For instructions on how to resolve a conflict, see [here (web GUI)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line) and [here (command line)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github).

### Making pull requests in the desktop application

[GitHub Desktop](https://desktop.github.com/) offers a third way to work
with the repository.

To clone the repository, do the following:
1. Click _Current repository_
1. Click _Add_ and select _Clone repository..._
1. Find `CSCfi/csc-user-guide` and click _Clone_

Pull requests can be created as follows:
1. Click _Pull origin_
1. Click _Current branch_ then _New branch_
1. Type the name of the new branch and click _Create branch_
1. Edit the files locally and commit the changes
1. Finally click _Publish branch_ and _Create Pull Request_
1. You are directed to web gui, where you click _Create pull request_

## Previewing the website using MkDocs

See the [FAQ](FAQ.md#how-can-i-preview-my-edits) for how to preview the Docs CSC website locally using MkDocs.

A newbie-friendly guide on how to set up the necessary tools on Windows is available [here](GETTING_STARTED.md).

## Building the website using the included Dockerfile

**This has some drawbacks, see [below](#development-container) for an alternative.**

You can also create a Docker container to host the docs. First build
an image from the included Dockerfile.

```bash
sudo docker build -t csc-user-guides .
```

This will build a container image called 'csc-user-guides'. Once the
image is built, you can run it.

```bash
sudo docker run --rm -it -p 80:8000 --name csc-user-guides csc-user-guides
```

This will run a web server on your laptop in port 80. You can view the
content of the user guides by pointing your browser to
[localhost](http://localhost).

### Development container

A [Containerfile](development/Containerfile.development) is included for building a container image with live-reload support.

#### Usage with rootless _Podman_

First, build the container image with the command

```bash
podman build -t docs-development -f development/Containerfile.development .
```

Then, start a container&mdash;bind-mounting the repository directory (`./`) to `/csc-user-guide` inside the container and publishing the port `8000`&mdash;with

```bash
podman run -it -v ./:/csc-user-guide -p 8000:8000 localhost/docs-development:latest serve
```

The site should be up at `localhost:8000` momentarily.

If you define an alias `mkdocs` for the Podman command like so

```bash
alias mkdocs='podman run -it -v ./:/csc-user-guide -p 8000:8000 localhost/docs-development:latest'
```

running the container is almost like running a regular installation of _MkDocs_:

```console
$ mkdocs --help
Usage: mkdocs [OPTIONS] COMMAND [ARGS]...

  MkDocs - Project documentation with Markdown.

Options:
  -V, --version         Show the version and exit.
  -q, --quiet           Silence warnings
  -v, --verbose         Enable verbose output
  --color / --no-color  Force enable or disable color and wrapping for the output. Default is auto-detect.
  -h, --help            Show this message and exit.

Commands:
  build      Build the MkDocs documentation.
  get-deps   Show required PyPI packages inferred from plugins in mkdocs.yml.
  gh-deploy  Deploy your documentation to GitHub Pages.
  new        Create a new MkDocs project.
  serve      Run the builtin development server.
```

#### Building with upgraded Python dependencies

The file [development/packages.txt](development/packages.txt) contains the currently used Python packages without explicit versions. To build an image with the latest versions for the packages available to _pip_ on the base image (`rockylinux:8`), include `--build-args upgrade=true` for the build command (possibly using a different tag, such as `docs-upgrade`):

```bash
podman build -t docs-upgrade -f development/Containerfile.development --build-args upgrade=true .
```

The image now has the latest available Python packages installed instead of the versions frozen in [requirements.txt](requirements.txt). The upgraded environment can now be, for example, frozen into `requirements.txt` with

```bash
podman run --entrypoint '["/bin/bash", "-c", "pip3 freeze"]' localhost/docs-upgrade:latest > requirements.txt
```

## Finding pages that might be outdated

Each page in Docs CSC shows a "Last update" timestamp. To ensure that content
stays up to date and valid, it is good practice to search for and check pages
that have not been updated in a long time. A script `scripts/last_update.sh`
is provided for this purpose that goes through the git log and prints for each
`.md` file its last update timestamp and who made the most recent commit.
Consider using the script from time to time to check pages that have not been
touched in a while, say, 1-2 years.

Run the script in the root of the repository as

```bash
bash scripts/last_update.sh
```

You can also filter out pages that no one has touched after you using the `-u`
option. The search pattern used here corresponds to your git username as
defined in your git config (see `git config user.name`). 

```bash
bash scripts/last_update.sh -u
```

Note that if you've changed your git username recently, the results may be
incomplete and you might need to manually grep for your commits.

If you find something worth updating, please do so and create a PR to help us
maintain Docs. If nothing needs to be modified, one way to update the timestamp
without actually making any visible changes is to add a comment in the file
using HTML tags, e.g.

```
<!-- Page OK, add comment to update timestamp -->
```
