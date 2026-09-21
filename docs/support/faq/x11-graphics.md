# X11 remote graphics does not work

Remote graphics requires tunneling X11 through SSH using the `-X` flag. On
Linux, connect to e.g. Roihu using:

```bash
ssh -X <your-user-name>@roihu-cpu.csc.fi
```

An error may occur if you have run out of disk quota.

Another (better) way to run remote graphics is to use a remote desktop through
the [Roihu web interface](../../computing/webinterface/index.md).

For more details, see our
[instructions for graphical connections](../../computing/connecting/index.md#graphical-connection).
