# X11 remote graphics does not work

Remote graphics requires tunnelling X11 through SSH using the `-X` flag. On Linux connect to e.g. Puhti using:  

```
ssh -X <your-user-name>@puhti.csc.fi
```

An error may occur if you have run out of disk quota.

Another way to run remote graphics is to use the [Puhti web interface](../../computing/webinterface/index.md).
