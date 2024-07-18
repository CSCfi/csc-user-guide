---
tags:
  - Free
---

# Biopython

Biopython is a collection of Python modules that facilitate the development of Python scripts for 
bioinformatics applications. As such, it does not include ready to use programs in the sense that 
many commercial packages and free web-based interfaces do. On the other hand, Biopython provides 
reusable Python modules that facilitate writing scripts for sequence manipulation, accessing of 
databases using a range of data formats and execution and parsing of the results of various 
molecular biology programs. Consequently, Biopython enables developing scripts that can analyze 
large quantities of sequence data in ways that are typically difficult or impossible with web based systems.
 
[TOC]

## License

Biopython is free to use and open source. It is dual licensed under [Biopython License](https://raw.githubusercontent.com/biopython/biopython/master/LICENSE.rst) or [BSD 3-Clause License](https://docs.conda.io/en/latest/license.html).

## Available

- Puhti: Python 3.10.6 with Biopython 1.79
- Puhti: Python 3.12.3 with Biopython 1.83

On Puhti, Biopython libraries, as well as many other bioinformatics-related Python libraries are available.

```bash
module load biopythontools
```

When the module is loaded, you can launch a Biopython program with the command:

```bash
python my_biopython_code.py
```

Alternatively, you can change the python definition in the first line of your code to

```bash
#!/bin/env python
```

and execute the python program

```bash
./my_biopython_code.pm
```

New python libraries can be installed with `pip install` command.
For example, a Python library called OBITools3 could be installed with the command:

```bash
pip install --user OBITools3
```

Further instructions on how to set the installation location etc. can be found in the
[CSC Python usage guide](../support/tutorials/python-usage-guide.md).

## More information

More information about Biopython can be found form the homepage of Biopython.

* [www.biopython.org](https://biopython.org/)
