# VS Code

VS Code is a code editor redefined and optimized for building and debugging modern web and cloud applications.

VS Code 1.90.2 can be installed to a SD Desktop virtual machine with [SD software installer](./sd-software-installer.md).
The installation creates a desktop button for VS Code.

The VS Code installation does not include any extensions.

Some extensions are available in SD Connect directory _tools-for-sd-desktop/apps/vscode-extensions_ .
If you don't find the extension you  need from this location, you can import them yourself.

On your own computer, open VS Code extensions library:

*   [https://marketplace.visualstudio.com/VSCode](https://marketplace.visualstudio.com/VSCode)

Once you have found the right extension, use the _Download Extension_ function to
download the extension to your local computer as a `.vsix` file.

Then use [SD Connect](https://sd-connect.csc.fi) to encrypt and upload the `.vsix` file to SD Connect.

In SD Desktop, refresh the Data Gateway connection and copy the `.vsix` file to your
SD Desktop environment.

Finally, open VS Code. Open the _Extensions Manager_ (lowest icon, in the first column of the interface).
In the Extensions Manager, click the three dots `...` to open the menu that contains function _Install from VSIX_
Use that function to read in the `.vsix` file you imported.
