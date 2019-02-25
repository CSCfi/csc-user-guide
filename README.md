# CSC User Guide

This repository contains master data for two websites. Public website 
(https://docs.csc.fi) is in sync with 'master' branch and internal development
website (https://csc-user-guide.rahti-int-app.csc.fi) is in sync with 'develop'
branch.

## Contributing

How you can contribute depends on whether you are CSC staff or user.

* Both CSC staff and users may create issues.
* CSC staff may edit source code.

If you find that anything is wrong, badly written or missing, please help us to 
fix it. We try to make this guide as good as possible. We appreciate your help.

## Creating issues

You can create issues at https://github.com/CSCfi/csc-user-guide/issues. You 
need to have a GitHub account to do this, though.

## Starting as a writer

CSC staff can join the Git organization [CSCfi](https://github.com/CSCfi) by 
sending email to vcs-support@csc.fi. After this you can [join the CSC employees 
team](https://github.com/orgs/CSCfi/teams/employees/members), which gives you 
permissions to edit source files that build the user guide.

To get a copy of the repository, you need a clone it.

```bash
git clone https://github.com/CSCfi/csc-user-guide.git
```

All other Git commands are given inside the directory that you have cloned.

```bash
cd csc-user-guide
```

## Directory structure

Below are guidelines on where to put new content.

```
csc-user-guide/
|__docs/
|   |__articles/      <== Put new articles here
|   |__images/         <== Put images here
|   |__videos/          <== Put videos here
|   |__accounts.md
|   |__applications.md    <== Link the article at least to one category
|   |__cloud.md               (accounts, applications, ... , support)
|   |__compiling.md
|   |__computing.md
|   |__connecting.md
|   |__data.md
|   |__index.md        <== You may link the article also here
|   |__support.md
|__ mkdocs.yml       <== Remember to link the article here
|__README.md
```

## Making changes to 'develop'

Working in the development branch is the recommended way of editing the guide. 
Select it as the active branch.

```bash
git checkout develop
```

After editing the files, give the following commands.

```bash
git pull origin
git add <pathspec>
git commit -m <msg>
git push origin develop
```

See instructions on [how to write a good Git commit 
message](https://chris.beams.io/posts/git-commit/).

## Making changes to 'master'

This is not recommended.

## Making changes to both 'master' and 'develop'

Urgent changes can be made to all branches at the same time. First make changes 
to the develop branch as described above. Then make the same changes to the 
master branch.

```bash
git checkout develop
git log
git checkout master
git cherry-pick <commit>
git push origin master
```

The `log` command is needed to get commit hash or hashes for the `cherry-pick` 
command.

## Merging 'master' and 'development'

Do not merge master and development branches. We are in pre-release phase and 
want them to be different.

## Building the website using MkDocs

[MkDocs](http://www.mkdocs.org/) is used to generate static documentation pages 
out of the Markdown files. You can install it on your computer by following the 
instructions given in [MkDocs 
documentation](http://www.mkdocs.org/#installation).

You can start a preview web server from the command line while in the root of 
the project directory.

```bash
mkdocs serve
```

This will start a web server on your computer listening on port 8000. Point 
your web server to [localhost:8000](http://localhost:8000) to get a preview of 
the documentation.

The configuration for MkDocs is in the mkdocs.yml file in the root of this 
repository. The name of the documentation site, the structure of the 
documentation pages and the theme to use for the site are described in this 
document.

The documentation files themselves are under the docs directory.

## Bulding the website using the included Dockerfile

You can also create a Docker container to host the docs. First build an image 
from the included Dockerfile.

```bash
sudo docker build -t csc-user-guides .
```

This will build a container image called "csc-user-guides". Once the image is 
built, you can run it.

```bash
sudo docker run --rm -it -p 80:8000 --name csc-user-guides csc-user-guides
```

This will run a web server on your laptop in port 80. You can view the content 
of the user guides by pointing your browser to [localhost](http://localhost).

## Hosting the website on OpenShift

The Dockerfile is also made to be compatible with OpenShift, so it should work 
with the source-to-image mechanism when using `oc new-app`. First create a new 
project to host the user guide.

```bash
oc new-project my-user-guide-project
```

Note that the name of the project must be unique within the OpenShift cluster 
you are running this in. Someone else may have already taken 
`my-user-guide-project`.

You can then run `oc new-app` to create the user guide deployment.

```bash
oc new-app https://github.com/CSCfi/csc-user-guide#master
```

In the command above, the `#master` at the end specifies the branch to use. If 
you have a feature branch that you would like to test on OpenShift, you can 
specify a branch different from master.
