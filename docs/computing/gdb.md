# GNU Debugger (GDB)
DB can be used to debug programs written in C, C++, and Fortran. It can perform four main tasks: inform about everything that might affect the behavior, make the program stop in specific conditions, examine why the program stopped, and finally change things in the program in order to correct the effects of a bug. 
In order to use the debugger the program has to be compiled with -g for symbolic debugging. 
We recommand running ```gdb --tui``` (shows the source code reached at a specific point in time and the breakpoints) in an [interactive session](running/interactive-usage.md) under [tmux](tmux.md).
Examples of usage:
* Start the debugger specifying the executable:
```
gdb --tui ./myexecutable
```
* Attach a running process:
```
gdb --tui ./myexecutable pid
```
In the ```gdb```promt it is posible to eneter commands such as ```break```, ```step```, or ```run```. For more information check the oficial page, [GDB](https://www.gnu.org/software/gdb/).

