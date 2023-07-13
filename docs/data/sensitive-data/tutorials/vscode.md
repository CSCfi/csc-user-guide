# VS Code

VS Code is a code editor redefined and optimized for building and debugging modern web and cloud applications.

VS Code 1.78.2 can be installed to a SD Desktop virtual machine with [SD software installer](./sd-software-installer.md).
The installation creates a desktop button for VS Code

The VS Code instalation does not include any extensions. However you can add them yourself.

On you own computer open VS Cone extension library:

*   [https://marketplace.visualstudio.com/VSCode](https://marketplace.visualstudio.com/VSCode)

Once you have found the right extension, use the _Donwload Extension_ function to
download the extension to your local computer as a _.vsix_ file.

Then use [SD Connect](https://sd-connect.csc.fi) to encrypt and upload the .vsix file to SD Connect.

Then in SD Desktop, refresh the DataGateway connection and copy the _.vsix_ file to your
SD Desktop environment.

Finally open VS Code. Open the _extensions manager_ ( lowest icon, in the first column if the interface).
In the Extensions manager, point the three dots ... to open the menu that contains function _Install from VSIX_
Use that function to read in the .vsix file you imported.
