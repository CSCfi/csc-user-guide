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


## Making changes using GitHub Pull Requests(PR) and branches

Overview:

 - Update local repository
 - Make a new branch from the master branch
 - Work and commit in your new branch (e.g. checkout from develop as below)
 - Push changes to github
 - Make a pull request to merge changes from your new branch into the master branch
 - Ask a person to review and merge the changes

Method:

```bash
git pull
git checkout master
git checkout -b your_branch_name
# create some nice content, add files
git commit -v
git push origin your_branch_name
```

Now you can ask a person to review and merge the changes. One can request
reviewers in the Github web interface.

After the PR has been merged, the branch on github can be deleted. This is the
preferred way to make larger changes in the develop branch as well, just replace master
above with develop.

## Copying a single file from 'develop' to 'master'

When you have made changes to 'develop', you can copy them to
'master'. This can be done file by file. First change to the master
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

You can return to the develoment branch with `git checkout develop`, but to
get the changes into master, you need to make a Pull Request at the web GUI,
see above.


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
