## Using wget to download data from web sites to CSC 
**Wget** is a command for downloading files from  WWW-sites and FTP servers. Once you have resolved the URL of the file, just give it as an argument to the `wget` command to download the file to your current directory.

```bash
wget URL
``` 
So for example 

```bash
wget http://ftp.gromacs.org/pub/gromacs/gromacs-2019.3.tar.gz
```
would download a file called _gromacs-2019.3.tar.gz_ to your current directory.
Pattern matching in the URL is possible when using _ftp_ , i.e. the URL starts with _ftp_:

```bash
wget "ftp://ftp.gromacs.org/pub/gromacs/gromacs-5*.tar.gz"
```
This command would retrieve all the files, whose name start with _gromacs-5_ and end with
_.tar.gz_

You can fine tune the behaviour of `wget` command with several options. 
You can see the full list of available command options with the command:
```bash
man wget
```
Below are listed some of the most commonly used options.

|Option 	| Argument | Description |
|---------------|----------|-------------|
|`-i`		|URL	   |Read a file containing the URL:s to retrieve.		 |
|`-O`		|file name |Name of the output file.		 |
|`-o`		|file name |Name of the download log file.		 |
|`-p`		|directory |Defines the directory where the downloaded data will be saved to. The default is . (the current directory).<Paste>		 |
|`-c`		|	   |Continue getting a partially-downloaded file.		 |
|`--user= `	|username  |Specify the user name for file retrieval		 |
|`--password=  `	|password  |Specify the password for file retrieval.		 |
|`-N`		|	   |Use time-stamping. Download the file only if it is newer that the file in the target directory.		 |
|`-m`		|	   |Turn on options suitable for mirroring. This option turns on recursion and time-stamping, sets infinite recursion depth and keeps FTP directory listings.|
