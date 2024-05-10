# How to use Python efficiently on CSC supercomputers

- This page should aim to:
	- Replace the existing docs/apps/python page
		- Does this page belong in docs/apps or is there a more suitable location?
	- Obviate the following pages:

"Usage and installation on HPC typically differ a lot from own laptop"
		
[General statements about using Python in HPC environment go here]

## Pre-installed software

"What pre-installed modules are available and for what purposes have they been
designed (data science, AI/ML bioinformatics, GIS)"

- We should have one or more pages for:
	- Listing our Python modules...
	- ...and their most important dependencies
		- All the dependencies a user requires might already be contained in a
pre-installed module, but finding out the contents requires inspecting source code,
which is inconvenient for most users
	- Can be one page with each module + contents
		- Link to Python module page in this section
	- Alternatively, individual pages for each module
		- Link to index page in this section

## Installing additional software

"How can you install your own python packages in an efficient manner"

- Extending pre-installed modules with a package manager
	- Recommended when:
		- Pre-existing module is missing just a few packages.
Straightforward with venv, existing instructions should suffice in most cases.
Since pip comes pre-installed on nodes and at least in some modules, this should
be a rather universal solution.
	- Caveats:
		- Could a pip installation compromise Conda environments e.g. by updating
dependencies whose older versions the software relies on?
		- Only works with venv, Conda is not pre-installed on nodes or modules.

- Tykky wrapper
	- Recommended when:
		- User wants to work within a Conda environment. No need to
really deal with containers. Of the different options we have, using a
containerized env with a wrapper is most like working with a regular Conda env,
since it can be used without Apptainer commands.
	- Caveats:
		- Tykky is great for wrapping environments, but might not work for all
applications. When desiring to install the latter, user could be encouraged to work
directly with containers.
- pip install --user
	- Recommended when:
		- User needs to use some less common library very
frequently, and so wants it to be available by default.
	- Caveats:
		- It is possible to exceed the $HOME directory file limit
with just a single pip installation.
		- Some installation commands do not work for user installations, e.g. spaCy.
	- NOTE: Is it possible that we do not want to recommend this as an option?
Creating venvs in project scratch storage generally involves much less hassle.

## Serial and parallel computing

"Batch script examples for a) serial b) parallel python scripts and warnings
about caveats (e.g. use threads instead of tasks, unless using mpi4py)"

## Interactive computing with Jupyter notebooks

"Using Python in OOD with Jupyter notebooks (maybe links to other existing pages
is enough)"
