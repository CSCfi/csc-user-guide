# Biopython

Biopython is a collection of python modules that facilitate the development of python scripts for 
bioinformatics applications. As such, it does not include ready to use programs in the sense that 
many commercial packages and free web-based interfaces do. On the other hand, Biopython provides 
reusable python modules that facilitate writing scripts for sequence manipulation, accessing of 
databases using a range of data formats and execution and parsing of the results of various 
molecular biology programs. Consequently, Biopython enables developing scripts that can analyze 
large quantities of sequence data in ways that are typically difficult or impossible with web based systems.
 
[TOC]

## License

Biopython is free to use and open source. It is dual licensed under [Biopython License](https://raw.githubusercontent.com/biopython/biopython/master/LICENSE.rst) or [BSD 3-Clause License](https://docs.conda.io/en/latest/license.html).

## Available

In Puhti, Biopython libraries, as well as many other bioinformatics related Python libraries are available
in the Python installations that are used by the [bioconda](./bioconda.md) environments. These environment also include 
python virtual environments that allow users to create their own project specific Python environment with `pip` installation tool.

These virtual environments use the PROJAPPL directory for installing the user specific libraries.
Because of that, you must first set PROJAPPL environment variable to point to the PROJAPPL directory of the
project you want to use.
```text
export PROJAPPL=/projappl/project_your_proj_num
```
After that, a virtual Python environment using Python 3.7.3 and biopython can be set up with commands:
```text
module load bioconda
biopython-env
```
If you want to use old Python 2.7.5 with biopython in stead, use setup commands:

```text
module load bioconda/2
biopython-env
```
However, we strongly recommend using Python 3 versions in stead of Python 2.

When the virtual environment is activated, you can launch a biopython program with command:
```text
python my_biopython_code.py
```
Alternatively you can change the python definition in the first line of your code to
```text
#!/bin/env python
```
and execute the python program

```text
./my_biopython_code.pm
```

New python libraries can be installed with `pip install` command.
For example, Python library called OBITools3 could be installed with command:

```text
pip install OBITools3
```



## Manual

More information about biopython can be found form the homepage of biopython.

*  [www.biopython.org](http://www.biopython.org)

