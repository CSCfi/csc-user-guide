# X11 remote graphics does not work

Remote graphics requires either using [NoMachine remote desktop](/apps/nomachine) or tunnelling X11 through `ssh`. The former works on all operating systems.
The latter requires an emulator on Windows, and is not recommended. Detailed information can be found in the [Connecting to CSC](/connecting/index).

If you get an error like the following:

```
X11 connection rejected because of wrong authentication.
Connection to localhost:13.0 refused by server.Client is not authorized to connect to server.
```

You might have run out of disk quota. Check that with the command

```
quota -s
```

and delete files from $HOME if necessary.
