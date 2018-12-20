# CSC user guides

## Editing the documentation

The guide is written using the [Markdown markup
language](https://en.wikipedia.org/wiki/Markdown).
[MkDocs](http://www.mkdocs.org/) is used to generate static documentation pages
out of the Markdown files.

Markdown can be edited using any text editor, but you will need to install
MkDocs if you wish to preview your changes while editing your documentation. You
can find installation instructions in the [MkDocs
documentation](http://www.mkdocs.org/#installation).

You can start a preview web server from the command line
while in the root of the project directory:

```bash
mkdocs serve
```

This will start a web server on your computer listening on port 8000. Point your
web server to [localhost:8000](http://localhost:8000) to get a preview of the
documentation.

The configuration for MkDocs is in the mkdocs.yml file in the root of this
repository. The name of the documentation site, the structure of the
documentation pages and the theme to use for the site are described in this
document.

The documentation files themselves are under the docs directory.

## Using the included Dockerfile

You can also create a Docker container to host the docs. First build an image
from the included Dockerfile:

```bash
sudo docker build -t csc-user-guides .
```

This will build a container image called "csc-user-guides". Once the image is
built, you can run it like this:

```bash
sudo docker run --rm -it -p 80:8000 --name csc-user-guides csc-user-guides
```

This will run a web server on your laptop in port 80. You can view the content
of the user guides by pointing your browser to [localhost](http://localhost).

## Hosting on OpenShift

The Dockerfile is also made to be compatible with OpenShift, so it should work
with the source-to-image mechanism when using `oc new-app`. First create a new
project to host the user guide:

```bash
oc new-project my-user-guide-project
```

Note that the name of the project must be unique within the OpenShift cluster
you are running this in. Someone else may have already taken
`my-user-guide-project`.

You can then run `oc new-app` to create the user guide deployment:

```bash
oc new-app https://github.com/CSCfi/csc-user-guide#master
```

In the command above, the `#master` at the end specifies the branch to use. If
you have a feature branch that you would like to test on OpenShift, you can
specify a branch different from master.
