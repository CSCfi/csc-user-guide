# Connecting Puhti 

## Opeing connection

To connect Puhti, you should use terminal programs like `ssh`  (linux, MacOSX) or [PuTTY](https://putty.org/) (Windows), which provide secure connection to the remote server. 

In Linux and MacOSX machines, you first need to open a terminal session. Then you can open connection to Puhti using the `ssh` command:

<pre>
ssh puhti.csc.fi -l <i>csc_username</i>
</pre>
or alternatively:
<pre>
ssh <i>csc_username</i>@puhti.csc.fi
</pre>

In the case of using PuTTY in Windows, you should specify, that you want connect _Host Name_: **puhti.csc.fi** (using the default port 22 and SSH connection type). Once you click the _Open_ button a new terminal session will ask for your CSC-username and password.

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). Introduction to
operating command line linux can be found for example from [here](https://research.csc.fi/csc-guide-linux-basics-for-csc). You can have several Puhti connections open in the same time.

## Login nodes

The Puhti supercluster has two login nodes ( puhti-login1.csc.fi and puhti-login2.csc.fi). When you open a new terminal connection using the server name _puhti.csc.fi_ you will end up to one of these login nodes. You can also open the connection directly to two of the login nodes ( puhti-login1.csc.fi and puhti-login2.csc.fi) if needed:

<pre>
ssh <i>csc_username</i>@puhti-login2.csc.fi
</pre>

Note that login nodes are not intended for heavy computing but for managing files and submitting batch jobs.

## Using graphics

If you wish to use applications that use graphics you have to use X-term connections. (Faster and better NoMachine connections are not yet available in Puhti). To be able to use X-term based tools your local computer must have an X11 server (often called as X window server program) installed and running. In linux and MacOSX machines X11 server is normally installed and running automatically. In Windows machines, an X server program must be installed to the users local machine. In addition to several commercial xterm programs there are also some free ones like [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local _ssh_ version, you may also need to add option `-X` or `-Y` to your ssh command:

<pre>
ssh -X <i>csc_username</i>@puhti-login2.csc.fi
</pre>

In _Putty_, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).





