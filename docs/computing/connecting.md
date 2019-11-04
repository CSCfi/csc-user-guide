# Additional ways to connect to Puhti.


## Using Putty to connect to Puhti

In the case of using [PuTTY](https://putty.org/) in Windows, you should specify, that you want connect _Host Name_: **puhti.csc.fi** (using the default port 22 and SSH connection type). Once you click the _Open_ button a new terminal session will ask for your CSC-username and password.

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). Introduction to
operating command line linux can be found for example from [here](https://research.csc.fi/csc-guide-linux-basics-for-csc). You can have several Puhti connections open at the same time.


## Using graphics

[NoMachine](../apps/nomachine.md) virtual desktop is the recommended way to use graphical applications in Puhti.
It is possible to use X-term connections too, but NoMachine is faster and better in many ways.
In addition to fast remote graphics, NoMachine enables you to 
keep your Puhti remote terminals active, even if you closed your local computer. 
Therefore, NoMachine is a good option for long interactive processes, with or without graphics.

*   [NoMachine tutorial for Puhti](../support/tutorials/nomachine-usage.md)

If you for some reason want to use a slower, X-term based graphical connection, your local computer must have an X11 server
(often called as X window server program) installed and running. In linux and MacOSX an X11 server is 
normally installed automatically, while for Windows, it needs to be installed separetely. 
In addition to several commercial xterm programs there are also some free ones 
like [MobaXterm](https://mobaxterm.mobatek.net/) or [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local _ssh_ version, you may also need to add option `-X` or `-Y` to your ssh command:
```
ssh -X <csc_username>@puhti.csc.fi
```

In _Putty_, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).





