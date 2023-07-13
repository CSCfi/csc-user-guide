# Auto-apptainer

Auto-apptainer is a help tool that can be used to add software to a SD Desktop virtual machine. It utilizes a library of
of Apptainer based software contaners, pre-loaded by CSC. You can suggest a container to be added to the library.

Auto apptainer is not available by default, but you must install it first using [SD Software installer](./sd-installer.md).
After that you can lauch the tool with command:

```test
auto-apptainer
```
By deafault, this lists all the Apptainer packages availabe. From the list you can select the backage to be installed.

Alternatively you can add a fltering criteria to the command. In this case only those containers whose name or one 
of commands that the container provides, matches the search creiteria, are listed.

For example command :

```test
auto-apptainer bam
```

asks the user to choose from two contaiers: _bamtools_ and _bedtools_. Bedtools is included as it provides commands _bamToBed_ and _bamToFasta_ that match the serach criteria in this case.

Once a container is selected, one more apptainer warpper based commands are created to drectory: _/shared-directory/sd-tools/bin_.
These commands can mostly be used like natively installed commands. For example after installing the Bamtools container, 
Bamtools can be startted with command:

```text
bamtools
```

