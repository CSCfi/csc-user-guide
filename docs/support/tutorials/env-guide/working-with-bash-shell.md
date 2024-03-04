# Working with bash shell

**bash** has several features that make command-line usage easier
and more effective. You do not have to always type the whole command-line
character by character. When you are typing the command, you can go
backwards and forward by using the *left and right arrow
keys*. You can delete the character left of the cursor with *Backspace*
key. Pressing `Ctrl-d` or the *Delete* key deletes the character under
the cursor. In addition to these basic command-line editing functions,
you can use the keyboard commands listed in the table below.

| Command  | Function                                                     |
|----------|--------------------------------------------------------------|
| `Ctrl-a` | Move the cursor to the beginning of the command-line         |
| `Ctrl-e` | Move the cursor to the end of the command-line               |
| `Ctrl-k` | Cuts all the characters right of the cursor                  |
| `Ctrl-y` | Paste the characters to the command-line (cut with `Ctrl-k`) |

In bash the executed commands are stored in user's home directory in a
file called `.bash_history`. To see the full list of recently executed
commands, give command `history`. On the command-line, you can browse
the list of previous commands with the *up and down arrow keys*. 
In cases where you need to give similar commands several times, it is
often handy to get one of the previous commands to the command-line with
the arrow key. Then you can edit just the modifications needed to the
old command and execute the modified command by pressing `Enter`.

It's possible to search through the command history. Press `Ctrl-r`, then
type what you want to search for. You do not need to type a complete
search as the search results will update with each character pressed.
To move between the search results, use the *up and down arrow keys*.
To run the command, press the *Return* key. If you
wish to edit the search result before running the command, use the
*left arrow key*, then edit the command.

## Automatic Tab completion

If you press the *Tab* key, the bash shell tries to complete the command or
argument you are writing. The completion is done as far as possible
using the list of available commands and files. Using auto-completion
is very recommended as it saves the user from typing all command or
argument characters and also takes care that commands don't get mistyped.
For example, let's say we are in a directory where we have two files:
`final_research_report_old.pdf` and `final_research_report_new.pdf`.

!!! info "Tip"
    This will save you a lot of typing and typos!

To open the latter of the files with Evince program, we would need to
type the command:

```bash
evince final_research_report_new.pdf
```

This command would require you to type 36 characters. However, by using
*Tab completion* you need to type only 5 characters. First type

```bash
evi
```

and then press the *Tab* key. Normally at CSC, Evince is the only
available program or command that starts with letters *evi*, so when the
Tab completion is executed, it knows to complete the rest of the
command:

```bash
evince
```

Then, to define the file name, you can type just the first letter of the
file name

```bash
evince f
```

When you now press *Tab*, the completion process checks which files
starting with *f* are available. In this case there are two of them and
as the beginning of the two file names is the same string, the command
can now be completed to:

```bash
evince final_research_report_
```

Now you just need to type one *n* to the end of file name to distinguish
the file from the *old* version,

```bash
evince final_research_report_n
```

When the *Tab* key is now pressed again there is only one option that
matches the beginning of the argument that has been typed, and thus the
command is completed and ready to be executed:

```bash
evince final_research_report_new.pdf
```

## Stopping programs and running programs in background

In Linux, graphical interfaces and commands that are not interactive
once they have started, can be executed as *background processes*. When
the command is executed as a background process, the command shell does
not wait until the command is finished. Instead, it remains active and
allows the user to submit new commands while the background command gets
executed. However, note that in the computing clusters of CSC, heavy
computing tasks should not be executed as background processes, but they
should be submitted to the batch queue system.
  
In normal interactive usage you can launch the command to be executed in
the background by adding `&` character to the end of the command. For
example, the command

```bash
eog image1.jpg &
```

would open the *Eye of GNOME* image viewing program (requires X-term
connection) to the background so that the command shell could
still be used even though the `eog` command is still running. A background
process can be changed to normal, foreground process with command 
`fg`. When a command and program is running interactively, i.e. the
command shell is waiting that the execution finishes, you can terminate
the execution by pressing `Ctrl-c`. Another possibility is to
halt the program by pressing `Ctrl-z`. When a command (or process) is
halted, it can be continued with `fg` command or changed to be executed
as a background process with command `bg`.
  
A command that is still running can be terminated with `kill`
command. To be able to use `kill`, you need to know the *process
identification number* (PID) of the command you want to terminate. You
can check your active processes, meaning the commands that you are
currently executing, with command `ps`. For example:

```bash
$ ps
PID TTY          TIME CMD
385 pts/12   00:00:00 tcsh
2001 pts/12   00:00:00 eog
2003 pts/12   00:00:00 gconfd-2
2203 pts/12   00:00:00 ps
```

By default, the `ps` command shows only those processes that have been
launched from the command shell you are currently using. To see all your
processes in the server you have logged in to, give command:

```bash
ps -f username
```

Once you have identified the correct process number, you can kill the
process with command:

```bash
kill PID
```

For example, the command

```bash
kill 2001
```

would kill the `eog` process, listed in the output of the previous `ps`
example. You can only kill processes that are owned by your account.
Sometimes when you want to kill a process that is malfunctioning, the
normal kill command may not able to terminate the process. In those
cases you can try to terminate the process by adding option `-9` to
the `kill` command:

```bash
kill -9 PID
```
