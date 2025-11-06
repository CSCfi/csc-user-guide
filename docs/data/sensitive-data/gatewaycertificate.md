# Fix

Virtual desktops created before November 5 2025 display an error that blocks Data Gateway application: Initializing Data Gateway failed.

To resolve this issue, a one time workaround is available. It must be applied per by each user by following these steps:

    connect to your virtual desktop, right click and click on open in terminal.

    Next, we need to test if another project member has already added the fixing tool. Type the following command in the terminal and press enter:

dg-fix

If the terminal says that command is not found, continue with the following steps:

    type this command and press enter:

gedit dg-fix

This opens a new user-friendly interface called Gedit text editor.

    Make sure that the editor view is active by clkiing in it.

    Next Then open the Clipboard-dashboard by pressing:
