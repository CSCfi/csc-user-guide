# Contributing

## Starting as a writer

CSC staff: do these two things _first_:

1. Join the Git organization [CSCfi](https://github.com/CSCfi) by sending email to vcs-support@csc.fi.
2. Then [join here the CSC employees team](https://github.com/orgs/CSCfi/teams/employees/members). Membership
gives you permissions to edit source files that build the user guide. (Wait for a confirmation email.)

The rest of this document describes the workflow in Github as well as instructions for previewing and deploying the documentation. See [Style guide](STYLEGUIDE.md) for content and formatting instructions and [Frequently Asked Questions](FAQ.md) for more in depth explanations of common issues you might encounter while contributing.

## For the impatient

Once you've completed the steps above:
* In [docs.csc.fi](https://docs.csc.fi) go the the page you want to edit and click the pen icon at top right
* (sign in GitHub) and edit then content
* Scroll down to commit changes (create a new branch) -> make a pull request
* Assign a reviewer

## Making changes using pull requests

The csc-user-guide repository uses the 'master' as the default
branch. You can make changes in web gui, command line or desktop application.

Master branch is protected. You cannot make changes to it directly, but you
must use pull requests.

### Overview

**Writer:**

 - Create your own branch from master (or work in an already existing branch, if agreed)
 - Create / bring there the content you want to work with. Pay attention to file naming!
 - Make sure the data is 100% correct (no Taito or other old references, language is correct, commands work, style is same as in other articles)
 - When creating new article, add it also to the mkdocs.yml navigation OR in the index.md file in that folder (in case of FAQs or softwares (= apps) for example). See also the [FAQ](FAQ.md#how-to-include-my-new-page-in-the-navigation-panel)
 - Make a pull request for your work to be added to Master
    - Look at the test results of your PR: if they are red, check what's wrong and commit to the PR directly to fix it
        - **How?** Click on the "Details" link for the failing test. Then click the "The Build" Failed -link more or less at the center of the page. This will open detailed results of the tests and help you pinpoint the error. See also the [FAQ](FAQ.md#my-pr-did-not-pass-the-tests-what-to-do) 
    - Assign one or more reviewers, try to choose someone who knows the _content_. See also the [FAQ](FAQ.md#how-and-who-should-i-ask-to-review-my-pr).
        - **Tip** Add a link to the rahtiapp-preview page (https://csc-guide-preview.rahtiapp.fi/origin/<your-branch-name>/rest-of-url/) in the Pull Request description to help reviewer 
    - Pull requests which do not meet the requirements will not be accepted. Note that you can keep committing to a pull request after it has been submitted.
    - Write meaningful pull request messages, so it is easier for reviewers to do their job.
    - Communicate! Use "WIP" (=Work In Progress) in your pull request title, if you don't wish the branch to be merged to master (i.e. you want to continue working with it).
 - Once PR has been accepted, remove the temporary branch (if not deleted by an admin at merge)

**Reviewer:** If you get a request to review a pull request, please contribute to help publish the changes!

 - Follow the link (or navigate to the pull request)
 - Make sure the tests pass
 - Edit the pages as needed (perhaps via the Web GUI)
     - It's ok to edit typos directly in the text
 - **Pro tip** 
      - Suggest changes so that they appear as `diff` in the conversation tab, so that the author can simply commit/reject them
      - In the "Files changed" tab, scroll to the line you want to change and press the blue "+" at the start of the line
      - In the appearing pop-up, press the sim-card-look-a-like icon with + and - on top of each other
      - write between the tics (including the suggestion) what you want to appear in the page
      - If you want to remove a line, delete the content (and leave the tics and the word suggestion)
      - If you want to remove lines, write the preceding and trailing lines
      - Write a comment outside the tics, if you want, and use Preview to see the resulting `diff`
      - Press "Add Single Comment"
 - Once you're happy with the content, in the "Files changed" tab click "Review changes" -> "Approve"
 - Anyone can be a reviewer, while pull requests can be accepted only by a smaller group of people

**Admin:** If you see an approved branch:

 - "Squash and merge" it
 - Delete the (now unnecessary) branch
 - Occasionally the number of (unnecessary) branches grows: prune.

**Note:** If you make bigger changes to the (main) categories / menu on the left, it might effect some links used on our webpages. Please communicate these changes, for example in the RC-channel #research.csc.fi.

### Previewing active branches

The GitHub web interface gives a preview (also while editing) but it does not render all syntax used in mkdocs correctly.
A full preview for ongoing work is available for all branches: https://csc-guide-preview.rahtiapp.fi/origin/
Note, currently absolute internal links don't work in the preview, but work on docs.csc.fi.

### Making pull requests in the web GUI

In the master branch, navigate to the page you want to edit, click the pen-logo at the top right and once ready, at the bottom choose "Create new branch from this commit and start a pull request". Note, that you can give the branch a descriptive name at this point. If you wish to edit already existing branch, first change to the correct branch in the "branch" button on upper left, next to the path to the file. If you found an error in the pull request of your own branch, you can commit to it directly instead of creating another pull request (the two choices at the bottom).

### Making pull requests on the command line

Overview:

 - Update local repository
 - Make a new branch from the master branch
 - Work and commit in your new branch
 - Push changes to github
 - Make a pull request to merge changes from your new branch into the develop branch
 - Ask a person to review and merge the changes

 To get a copy of the repository, you need a clone it.

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

Now, in the github web GUI you can create a pull request, ask a person to review
it and (some admin to) merge the changes.

After the PR has been merged, the branch on github can be deleted.

Tip 1. Git uses [Vim](https://www.vim.org) as the default editor for commit
messages. It is possible to change the default editor, but below are
the most important commands if you do not want to do it right now.

```
i    Enter insert mode
Esc  Exit insert mode
:wq  Save and exit
```

Tip 2. See instructions on [how to write a good Git commit
message](https://chris.beams.io/posts/git-commit/).

Tip 3. If pushing fails, the most probable reason is that somebody
else has made edits while you were editing. This situation is called a
conflict. (To be written: How to resolve conflicts?)

### Making pull requests in the desktop application

[GitHub Desktop](https://desktop.github.com/) offers the third way to work
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

This user guide uses [MkDocs](http://www.mkdocs.org/) to generate documentation
pages. You can install it on your computer by following the instructions given
in [MkDocs documentation](https://www.mkdocs.org/user-guide/installation/), or with
[conda](https://docs.conda.io/en/latest/miniconda.html) by simply

```bash
conda env create -f docs/support/tutorials/conda/conda-docs-env-1.0.yaml
conda activate docs
```

You can start a preview web server from the command line while in the
root of the project directory.

```bash
mkdocs build
mkdocs serve
```

This will start a web server on your computer listening on port
8000. Point your web server to [localhost:8000](http://localhost:8000)
to get a preview of the documentation.



## Bulding the website using the included Dockerfile

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



## Hosting the website on OpenShift

Install & authorize command line tools. For reference, see
[rahti documentation](https://rahti.csc.fi/tutorials/elemental_tutorial/#preparations).

The Dockerfile is also made to be compatible with OpenShift, so it
works with the source-to-image mechanism when using `oc
new-app`. First create a new project to host the user guide.

```bash
oc new-project my-user-guide-project
```

Note that the name of the project must be unique within the OpenShift
cluster you are running this in. Someone else may have already taken
`my-user-guide-project`.

You can then run `oc new-app` to create the user guide deployment.

```bash
oc new-app https://github.com/CSCfi/csc-user-guide#feature-a --name=csc-user-guide-feature-a
```

In the command above, the `#feature-a` at the end specifies the branch to
use. The option `--name=` is free to be chosen.

Now Rahti will build an image and a small webserver that can be exposed to
internet with the `oc expose` command:

```bash
oc expose svc/csc-user-guide-feature-a --hostname=cug-user-guide-feature-a.rahtiapp.fi
```

You are free to choose any unused hostname.

Rebuilding the content is done with `oc start-build` command:

```bash
oc start-build csc-user-guide-feature-a
```

Or by setting up a webhook (see [Rahti User
Guide](https://rahti.csc.fi/tutorials/patterns/#webhooks).)

If you always do your features in the branch with the same name, you only have
to issue `oc start-build` command to have your preview of the user-guide updated.

When you are sure you don't ever need the preview website again, please either
delete your project or clean it with `oc delete`:

```bash
oc delete all -l app=csc-user-guide-feature-a
```
