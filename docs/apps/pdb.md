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
    - Roihu-CPU
    - Roihu-GPU
---

# pdb: Python debugger

## Available

- Mahti: Any Python version
- Puhti: Any Python version
- Roihu-CPU: Any Python version
- Roihu-GPU: Any Python version

## License

Usage is possible for both academic and commercial purposes.

## Usage

[pdb](https://docs.python.org/3/library/pdb.html) is an in-built Python
debugger that supports breakpoints, stepping through the source line by line,
inspection of stack frames, source code listing, etc.

In order to use the tool, launch first an [interactive session](running/interactive-usage.md)
and start then your Python program under the debugger:
```
python -m pdb myscript.py
```

Running `pdb` will open the prompt which supports various commands such as
`where`, `down`, `up`, `up`, `break`, `step`, `next`, `jump`, `list`.
