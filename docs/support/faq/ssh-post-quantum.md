# SSH post-quantum key exchange algorithm warning

New SSH clients give out warning

```output
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
```

when connecting to servers that do not support post-quantum key exchange
algorithms.

The issue is not new, new SSH clients just make the users aware of it. Currently
we consider it safe to ignore, when not handling sensitive data.
