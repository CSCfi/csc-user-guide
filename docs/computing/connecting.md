# Additional ways to connect to Puhti.


## Using Putty to connect to Puhti

In the case of using PuTTY in Windows, you should specify, that you want connect _Host Name_: **puhti.csc.fi** (using the default port 22 and SSH connection type). Once you click the _Open_ button a new terminal session will ask for your CSC-username and password.

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). Introduction to
operating command line linux can be found for example from [here](https://research.csc.fi/csc-guide-linux-basics-for-csc). You can have several Puhti connections open in the same time.


## Using graphics

If you wish to use applications that use graphics you have to use X-term connections. (Faster and better NoMachine connections are not yet available in Puhti). To be able to use X-term based tools your local computer must have an X11 server (often called as X window server program) installed and running. In linux and MacOSX machines X11 server is normally installed and running automatically. In Windows machines, an X server program must be installed to the users local machine. In addition to several commercial xterm programs there are also some free ones like [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local _ssh_ version, you may also need to add option `-X` or `-Y` to your ssh command:
```
ssh -X <csc_username>@puhti-login2.csc.fi
```

In _Putty_, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).





