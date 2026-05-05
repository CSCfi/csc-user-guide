---
tags:
  - Free
catalog:
  name: gdb
  description: GNU debugger for compiled programs
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# gdb: GNU Debugger

## Available

- Puhti
- Mahti
- Roihu-CPU

## License

Usage is possible for both academic and commercial purposes.

## Usage

GNU Debugger (GDB) can be used to debug compiled programs (written in C, C++,
Fortran). It can perform four main tasks: inform about everything that might
affect the behavior, make the program stop in specific conditions, examine why
the program stopped, and finally change things in the program in order to
correct the effects of a bug.

In order to use the debugger the program has to be compiled with `-g` flag to
enable symbolic debugging.

One can either start the application under the debugger, or attach the debugger 
to a running application.

In order to start the application under the debugger, launch first an
[interactive session](../computing/running/interactive-usage.md) and execute then:
```
gdb --tui ./myexecutable
```

In order to attach to a running application, 
[connect first to a compute node](../computing/running/interactive-usage.md#connecting-to-a-compute-node-of-a-running-job).
Next, you need to find the process ID `<pid>` e.g. by running the command `ps ux`,
attach then debugger to that:
```
gdb --tui ./myexecutable <pid>
```

If additional arguments are needed for the program, one can use the option
`--args` before the name of the executable. The `--tui` option starts a nice
terminal interface that shows the source code.

In the `gdb` prompt it is possible to enter commands such as `break`, `step`,
or `run`. For more information check the official page:
[GDB](https://www.gnu.org/software/gdb/).
