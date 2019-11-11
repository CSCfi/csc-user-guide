# X11 remote graphics does not work

Remote graphics requires either using [NoMachine](../../apps/nomachine.md)
remote desktop or tunnelling X11 through ssh. The former works on all 
operating systems. The latter requires an emulator on Windows, and is not
recommended for demanding graphics. On Linux connect to e.g. Puhti using:  
`ssh -X -l your-user-name puhti.csc.fi` An error may occur if you have run out
of disk quota. 
