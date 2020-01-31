# Contributing

## Starting as a writer

CSC staff can join the Git organization
[CSCfi](https://github.com/CSCfi) by sending email to
vcs-support@csc.fi. After this you can [join the CSC employees
team](https://github.com/orgs/CSCfi/teams/employees/members), which
gives you permissions to edit source files that build the user guide.

To get a copy of the repository, you need a clone it.

```bash
git clone https://github.com/CSCfi/csc-user-guide.git
```

All other Git commands are given inside the directory that you have
cloned.

```bash
cd csc-user-guide
```

## Making changes

The csc-user-guide repository uses the 'master' as the default
branch. You can make changes in web gui or on command line.

Overview: 
 - Create your own branch from master (or work in an already existing branch, if agreed)
 - Create / bring there the content you want to work with. Pay attention to file naming!
 - Make sure the data is 100% correct (no Taito or other old references, language is correct, commands work, style is same as in other articles)
 - When creating new article, add it also to the mkdocs.yml navigation OR in the index.md file in that folder (in case of FAQs or softwares (=apps) for example)
 - Make a pull request for your work to be added to Master 
    - You can also aim it at someone specifically (recommended)
    - Pull requests which do not meet the requirements will not be accepted. Note that you can keep committing to a pull request after it has been submitted.
    - Write meaningful pull request messages, so it is easier for reviewers to do their job.
    - Communicate! Use "WIP" (=Work In Progress) in your pull request title, if you don't wish the branch to be merged to master (i.e. you want to continue working with it).
    - Look at the test results of your PR: if they are red, check what's wrong and commit to the PR directly to fix it
 - Once PR has been accepted, remove the temporary branch

Reviewer: If you get a request to review a pull request, follow the link, edit the pages as needed (perhaps via the Web GUI), and click "comment" not "close" if you're happy with the content. Anyone can be a reviewer. Pull requests can be accepted only by a smaller group of people. 

## Making changes directly to 'master'

This is not recommended, and master branch is protected.

## Making changes using pull requests in the web GUI

In the master branch, navigate to the page you want to edit, click the pen-logo at the top right and once ready, at the bottom choose "Create new branch from this commit and start a pull request". If you wish to edit already existing branch, first change to the correct branch in the "branch" button on upper left, next to the path to the file. If you found an error in the pull request of your own branch, you can commit to it directly instead of creating another pull request (the two choices at the bottom).

## Making changes using pull requests on the command line

Overview:

 - Update local repository
 - Make a new branch from the master branch
 - Work and commit in your new branch
 - Push changes to github
 - Make a pull request to merge changes from your new branch into the develop branch
 - Ask a person to review and merge the changes

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

Now you can ask a person to review and merge the changes. One can request
reviewers in the Github web interface.

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

## Content and formatting instructions

 - Put all images in root images folder
 - Try to make standalone articles with a good name (user knows to select it from the left menu)
 - Write SLURM flags in long format (--nodes instead of -N, etc.)
 - All examples should use minimum viable reserved resources. I.e don't write examples with --t=72:00:00 / --gres=gpu:v100:4 / --cpus-per-task=40, if it not needed. Users tend to use these as default values.
 - Don't make too deep hierarchy or too many entries per subcategory (combine very small pages)
 - When in doubt, check how other pages are formatted
 - For code sections (marked with three backticks,\`\`\`) Mkdocs will by default try to auto-guess the language for syntax highlighting. It's probably best to specify the language explicitly, e.g.  \`\`\`bash or  \`\`\`python
If you don't want any syntax highlighting, just use \`\`\`text
For a list of all supported languages see: http://pygments.org/docs/lexers/
- Don't refer to the same page twice in mkdocs.yml -> sitemap breaks + weird menu action

## Previewing 

Preview is available for all branches: https://csc-guide-preview.rahtiapp.fi/origin/
Here you can preview your ongoing work. Note, currently absolute internal links don't work in the preview, but work on docs.csc.fi.

## Previewing the website using MkDocs

This user guide uses [MkDocs](http://www.mkdocs.org/) to generate documentation
pages. You can install it on your computer by following the instructions given
in [MkDocs documentation](http://www.mkdocs.org/#installation), or with
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
