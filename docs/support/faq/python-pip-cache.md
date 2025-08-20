# How to avoid Python pip cache filling up my home directory

## The default pip cache directory

The [Python package manager pip uses a cache][pip-caching] to reduce
network access and to avoid having to rebuild packages that have
already been built. By default this cache resides in the user's home
directory in `~/.cache/pip`. You can check what is your current pip
cache directory with the command `pip cache dir`. For example:

```console
$ pip cache dir
/users/mvsjober/.cache/pip
```

For example installing PyTorch will put around 3.7 GB of files into
the cache, this can easily fill up your [home directory
quota][home-dir]. You can clean up your cache either by simply
deleting it with `rm -rf ~/.cache/pip` or (more gently) by using the
command `pip cache purge`:

```console
$ pip cache purge
Files removed: 52
```

## Changing the pip cache directory

To avoid problems in the future it might be a good idea to store your
pip cache on the scratch file system instead. The pip cache can be set
with the `--cache-dir` flag or, globally by setting the
`PIP_CACHE_DIR` environment variable. For example (change the path to
something appropriate for your project and user):

```console
$ export PIP_CACHE_DIR=/scratch/project_2001659/mvsjober/pip-cache/
$ mkdir -p $PIP_CACHE_DIR
```

You can now test that pip has picked up this change:

```console
$ pip cache dir
/scratch/project_2001659/mvsjober/pip-cache/
```

If you want to make this setting permanent for your user, you can add
the export-line to the `.bashrc` file in your home directory.


[pip-caching]: https://pip.pypa.io/en/stable/topics/caching/
[home-dir]: https://docs.csc.fi/computing/disk/#home-directory
