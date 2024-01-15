# I cannot login. What to do?

The first thing to do when you encounter login problems is to find out which
services you can login and which you cannot.

## I can login to MyCSC but not the system I want to use

If you can login to [MyCSC](https://my.csc.fi), there are three common reasons
for login problems affecting other services, like Puhti:

1. The service you are trying to login is down or has issues. See notifications
   in your mailbox or at [research.csc.fi](https://research.csc.fi). Wait until
   the maintenance is completed or the issue is resolved.
1. You have no projects enabled in the service that you are trying to login.
   Check the services linked to your projects at MyCSC.
   [Add service access for your project](../../accounts/how-to-add-service-access-for-project.md)
   if you have a suitable project, or [create a new project](../../accounts/how-to-create-new-project.md),
   and for it, add the access to the service.
1. You just changed your password and it has not yet been updated on the system
   you try to access. Please allow for up to one hour and retry. Too many
   repeated failed attempts will (temporarily) block your IP address or account.

## I cannot login to MyCSC

If you cannot login to MyCSC, there is one problem that is more common than
others:

1. Your account is locked. The most common reasons are:

* You have not changed your password for a year.
* We have sent email to you but it bounces back.
* Your account was granted for a fixed period and the time is up.

You need to contact us to get your account unlocked. Our email address is
[servicedesk@csc.fi](mailto:servicedesk@csc.fi).

## Why is my SSH client saying "Corrupted MAC on input"?

There is a known issue of **Windows OpenSSH clients**, which are using the LibreSSL library for
cryptography. The bug happens when the combination of cipher `aes128-ctr` and either the
`umac-128-etm@openssh.com` or `umac-128@openssh.com` MAC algorithm is used.
The client will show an error saying `Corrupted MAC on input`.

Here are some links to relevant bug reports:

- [https://github.com/libressl/portable/issues/603](https://github.com/libressl/portable/issues/603)
- [https://github.com/PowerShell/Win32-OpenSSH/issues/1359](https://github.com/PowerShell/Win32-OpenSSH/issues/1359)
- [https://github.com/PowerShell/Win32-OpenSSH/issues/2078](https://github.com/PowerShell/Win32-OpenSSH/issues/2078)

If you encounter this issue while trying to log in via SSH, you can try to add an explicit choice
of MAC algorithm to your SSH client, instead of using the automatically chosen algorithms.
This is achieved with the `-m <MAC algorithm>` option.
To find out what MAC algorithms your client technically supports, you can run the `ssh -Q mac` command.

At the moment of writing, "hmac-sha2-512" is a suitable alternative, for example.
This may change in the future, so it may be a good idea to not take it for granted that this
workaround will be good forever.

The `-o MACS=-<algorithms>` option will also work. This syntax prevents the use of the given
algorithms. This is preferable over the `-m <MAC algorithm>`, since it will rely on the system
defaults to choose the most suitable algorithm for you, also in the future.

```bash
# (Preferred way:) Tell SSH not to use the broken algorithms:
ssh -o MACS="-umac-128-etm@openssh.com,umac-128@openssh.com" yourcscusername@mahti.csc.fi

# Or override the default MAC algorithm:
ssh -m hmac-sha2-512 yourcscusername@puhti.csc.fi
# Show what MAC algorithms your SSH client supports:
ssh -Q mac
```

Please note that all the `*-etm` variants are disallowed by the SSH servers on the CSC supercomputers
for the time being, due to a newly discovered security weakness in them from December 2023,
called "Terrapin".
If you use an unsupported algorithm, the server will tell you:

```
Unable to negotiate with <server's IP> port 22: no matching MAC found.
```

If you experience this issue, and you find a working solution with a different MAC algorithm,
you might want to add a line to your `ssh_config` which would enable the workaround automatically.
For example, to tell SSH that the `umac-128` algorithm should be disallowed, use a configuration
like the one below:

```
# Place this in your home directory's ssh\config file:

Host *
    MACs -umac-128-etm@openssh.com,umac-128@openssh.com

# Note the minus in front of the listed algorithms, which indicates
# that these algorithms should be removed from the accepted ones.
```

## The SSH server says "Unable to negotiate ... no matching MAC found"

Please see the [section above](#why-is-my-ssh-client-saying-corrupted-mac-on-input)
about choosing a different MAC algorithm for your client.
