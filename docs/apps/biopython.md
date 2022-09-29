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

-   Puhti-rhel8: Python 3.10.6 with Biopython 1.79

In Puhti-rhel8, Biopython libraries, as well as many other bioinformatics related Python libraries are available.

```text
module load biopythontools
```

When the module is loaded, you can launch a biopython program with command:
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
pip install --user OBITools3
```

Further instructions on how to set the installation location etc can be found in the general
[Python](python.md) page.

## Manual

More information about biopython can be found form the homepage of biopython.

*  [www.biopython.org](http://www.biopython.org)

