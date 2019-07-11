## NoMachine

The NoMachine Client and server enable a fast graphical work from CSC to
your local computer. This makes using GUIs fluent. The idea is to
connect to nxkajaani.csc.fi with the NoMachine client (free) installed
at your computer (available for Win, Mac, Linux). Then from
nxkajaani.csc.fi i.e. within Kajaani connect with ssh to the server
where you want do your science e.g. run RStudio or VMD. The speedup vs.
X11 (native or emulated) can be many fold, so you will experience
substantial improvement. Note that with NoMachine you don't need
X-emulators or X-term (in Linux).

[TOC]

![NoMachine sketch][NoMachine sketch]

## Available

The client is installed on your local machine, and the version 6 NoMachine
Terminal Server runs on nxkajaani.csc.fi.

## License

The NoMachine *client* is free and access to nxkajaani.csc.fi is
allowed for all CSC users. 

## Usage

1.  You will need a user account at CSC (on the server where you run
    applications). If you don't have one, you can get it from [here].
2.  Download the latest NoMachine **client** (win, mac, linux) from the
    NoMachine site, see detailed instructions from the link below.
3.  Install and configure your NoMachine client. See [CSC NoMachine Tutorial]
4.  Start the NoMachine client and log on to nxkajaani.csc.fi.
5.  Right click in the Desktop and choose the CSC server you want to use
    (opens an ssh terminal).
6.  Start working on great science.
7.  When you're done, disconnect or terminate the connection from the
    Desktop top right corner (peel menu). The number of overall sessions,
    including suspended ones, is limited.

## More Information

* NoMachine [knowledge base](https://www.nomachine.com/knowledge-base)
* User support via CSC through servicedesk@csc.fi

------------------------------------------------------------------------

  [NoMachine sketch]: /images/nomachine.png
  [here]: ../accounts/creating-a-new-user-account.md
  [CSC NoMachine Tutorial]: /support/tutorials/nomachine-usage
