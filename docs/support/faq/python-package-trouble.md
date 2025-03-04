# How to troubleshoot Python installation problems

## Use `pip list -v` to find out where your packages are coming from

When troubleshooting Python installation problems, we often see
that users have installed their own versions of packages
that can conflict with those coming from CSC's pre-installed
modules. It can be very easy to forget something you installed a long
time ago, and it is also easy to miss that pip is installing some
additional packages that you are not aware of.

The command `pip list -v` is an easy way to find out where your
packages are coming from. The list might be very long, so you might
want to use `less` to get a view where you can scroll up and down, or
`grep` to extract the lines you are interested in.

```bash
pip list -v | less
```

In `less` you can use the arrow keys or Page Up and Page Down keys to
move around. Press 'q' to quit.

Below is an example (with many lines removed) using the python-data
module combined with a venv and some packages installed into the
user's home directory.

```sh
Package    Version  Location                                                                Installer
---------- -------- ----------------------------------------------------------------------- ---------
aiohttp    3.9.3    /PUHTI_TYKKY_FRQGCcR/miniconda/envs/env1/lib/python3.10/site-packages   conda    # ← tykky
alembic    1.13.1   /PUHTI_TYKKY_FRQGCcR/miniconda/envs/env1/lib/python3.10/site-packages   pip      # ← tykky
..
biopython  1.85     /users/mvsjober/.local/lib/python3.10/site-packages                     pip      # ← user's home
..
cowsay     6.1      /projappl/project_2001659/mvsjober/my-venv/lib/python3.10/site-packages pip      # ← project venv
```

In the `pip list -v` output, check the Location column. In the example
above the packages with locations starting with `/PUHTI_TYKKY_` are
those coming from the python-data module, which has been installed
with [Tykky][tykky]. Note that these are paths inside the container
created with Tykky. The package `biopython` seems to be installed into
the user's home directory, while `cowsay` is in the user's venv
virtual environment found in a project folder.

To see only packages not coming from the CSC-installed python-data module:

```bash
pip list -v | grep -v /PUHTI_TYKKY
```

Note that some modules are not using [Tykky][tykky] and Conda, for
example pytorch has packages installed into `/usr/local/lib` or
`/usr/local/lib64`. Note that these are paths inside the pytorch
container.

```bash
Package    Version  Location                                  Installer
---------- -------- ----------------------------------------- ---------
absl-py    1.4.0    /usr/local/lib/python3.11/site-packages   pip      # ← pytorch container
aiohttp    3.11.10  /usr/local/lib64/python3.11/site-packages pip      # ← pytorch container
```

[tykky]: ../../computing/containers/tykky.md
