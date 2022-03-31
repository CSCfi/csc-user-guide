# Visual Studio Code
The Visual Studio Code interactive app can be used for editing and running code on Puhti.
Make sure to load the correct modules before launching the session for the debugger to work correctly.

## Extensions
The interactive app has Python, Jupyter and C/C++ extensions installed.
Other extensions can be installed in the extensions tab in VSCode.
Dependencies for the extensions need to be loaded or installed for the extensions to work correctly.
E.g. the `go` module must be loaded before installing the `golang` extensions in VSCode.

## Python
Python environments can be loaded by loading the correct module before launching VSCode.
Make sure to select the correct Python version in the bottom bar of VSCode as the correct Python is not always selected automatically.

## C/C++
The compiler used can be selected when launching the interactive app.

Changing compiler between the Intel compiler and gcc in the workspace may cause issues.
Most of the problems can be solved by removing the launch and build configurations and creating them again.

## Troubleshooting
If VSCode does not work properly you can clear the settings and launch the application again.
This can be done done by deleting the folder `~/.local/share/csc-vscode`.
