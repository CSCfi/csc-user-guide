# Conda best practices

!!! warning "Do not install Conda environments directly on the shared file system!"
    Due to performance issues, CSC has deprecated the use of Conda environments that
    are installed directly on the shared file system on CSC supercomputers. Users should
    either containerize their Conda-based installations or consider alternative means
    of installation. See our separate [Conda deprecation page](../deprecate-conda.md)
    and [usage policy](../../computing/usage-policy.md#conda-installations) for more
    details. See also the [Tykky container wrapper](../../computing/containers/tykky.md),
    a tool using which you can easily containerize your Conda installations.
