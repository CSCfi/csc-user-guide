# I can login to nxkajaani, but I can't login to Sisu/Taito from there.

The problem is likely your keyboard mapping in the remote desktop. Don't try too many times, or your account will be (temporarily) banned.

As you can't see what comes out when you're typing your password, to confirm that the mapping is the problem, do the following (in a NoMachine session)

1.   Right click somewhere in the background -> choose fluxbox menu -> Workspace list -> Rename current workspace.
2.   Start typing your password here (or the some of the special keys). If they go wrong, your password will go wrong when you try to login from nxkajaani.

To fix this, right click in the backround, choose fluxbox menu, keyboard layout, Finnish. And try again. More known issues of NoMachine can be found in the [CSC NoMachine tutorial](../tutorials/nomachine-usage.md)

If this is the first time you're logging in to Taito and you got the error while either logging in to taito-shell or opening an application from the drop down menu, choose first taito from the server menu. This will set up your environment properly and then you can use the other options.
