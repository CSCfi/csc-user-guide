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

## Making changes to 'develop'

The csc-user-guide repository uses the 'develop' as the default
branch. When you have cloned the repository, this branch is what you
see. If you are unsure which branch you are in, you can run `git
branch`. The active branch can be changed with the `git checkout`
command.

Before you start to edit the content, pull the changes made by others
to your local copy of the repo.

```bash
git pull
```

After editing the files, try to push them to GitHub. The commands are
given below. See also the tips after the commands.

```bash
git status
git add example-file.md
git commit -v
git push
```

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



## Making changes directly to 'master'

This is not recommended.



## Copying changes from 'develop' to 'master'

When you have made changes to 'develop', you can copy them to
'master'. This is best done file by file. First change to the master
branch.

```bash
git checkout master
```

Select which files you want to 'merge'.

```bash
git checkout develop example-file.md
```

Now `example-file.md` is from the development branch and all the rest
is from the master branch. Commit and push.

```bash
git commit -v
git push
```

You can return to the develoment branch with `git checkout develop`.

## Making changes using GitHub Pull Requests(PR) and branches

Overview:

 - Update local repository
 - Make a new branch from the develop branch
 - Work and commit in your new branch
 - Push changes to github
 - Make a pull request to merge changes from your new branch into the develop branch
 - Ask a person to review and merge the changes

Method:

```bash
git pull
git checkout develop
git checkout -b your_branch_name
# create some nice content, add files
git commit -v
git push origin your_branch_name
```

Now you can ask a person to review and merge the changes. One can request
reviewers in the Github web interface.

After the PR has been merged, the branch on github can be deleted.

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

The Dockerfile is also made to be compatible with OpenShift, so it
should work with the source-to-image mechanism when using `oc
new-app`. First create a new project to host the user guide.

```bash
oc new-project my-user-guide-project
```

Note that the name of the project must be unique within the OpenShift
cluster you are running this in. Someone else may have already taken
`my-user-guide-project`.

You can then run `oc new-app` to create the user guide deployment.

```bash
oc new-app https://github.com/CSCfi/csc-user-guide#master
```

In the command above, the `#master` at the end specifies the branch to
use. If you have a feature branch that you would like to test on
OpenShift, you can specify a branch different from master.
