---
tags:
  - Free
catalog:
  name: pdb
  description: Built-in Python debugger
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# pdb: Python debugger

## Available

- Mahti: Any Python version
- Puhti: Any Python version

## License

Usage is possible for both academic and commercial purposes.

## Usage

[pdb](https://docs.python.org/3/library/pdb.html) is an in-built Python
debugger that supports breakpoints, stepping through the source line by line,
inspection of stack frames, source code listing, etc.

There are two ways to use the debugger. Within the code (or from the
interpreter):

```
import pdb
pdb.run('functbd(list_parameters)')
```

Alternatively pdb can also be invoked as a script to profile another script:

```
python -m pdb myscript.py
```

Running `pdb` will open the prompt which supports various commands such as
`where`, `down`, `up`, `up`, `break`, `step`, `next`, `jump`, `list`.
