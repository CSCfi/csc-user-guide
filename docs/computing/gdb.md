# gdb: GNU Debugger

GNU Debugger (GDB) can be used to debug compiled programs (written in C, C++,
Fortran). It can perform four main tasks: inform about everything that might
affect the behavior, make the program stop in specific conditions, examine why
the program stopped, and finally change things in the program in order to
correct the effects of a bug.

In order to use the debugger the program has to be compiled with `-g` flag to
enable symbolic debugging.

The debugger can either start a new process or attach to a running process.

Example of starting a new process to be debugged:

```
gdb --tui ./myexecutable
```

Example of attaching to an existing process (with process ID `pid`):

```
gdb --tui ./myexecutable pid
```

If additional arguments are needed for the program, one can use the option
`--args` before the name of the executable. The `--tui` option starts a nice
terminal interface that shows the source code.

In the `gdb` prompt it is possible to enter commands such as `break`, `step`,
or `run`. For more information check the official page:
[GDB](https://www.gnu.org/software/gdb/).
