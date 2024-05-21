# Shell

The shell apps can be found under _Pinned Apps_ or on the top navbar under the
_Tools_ section. There are two different shells.

The _Login node shell_ launches a normal Linux shell on one of the login nodes.
Any command that is running when the login node shell browser tab is closed
will stop. Note that the same rules apply here as during a normal SSH session:

!!! error-label 
    **Login nodes are only for light pre/postprocessing**
    (see [usage policy](../usage-policy.md)).

The _Compute node shell_ launches a persistent shell on a compute node for
heavier commands that should not be run on login nodes. The persistent shell
will keep running even if you close your browser or lose internet connection.
