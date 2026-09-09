# Using tmux for long-running commands on Roihu

Large data transfers, large file deletions etc. can take a long time to finish on the login node.
If your SSH connection breaks while such a command is running, the command usually stops.

To avoid this, run long-running interactive commands inside a `tmux` session.
The session keeps running on the login node even if you disconnect from SSH.

This tutorial is written mainly for the Roihu supercomputer, but the workflow
is applicable to most Linux workstations that have `tmux` installed.

!!! note
     Use `tmux` for long-running interactive commands such as data  transfers and file cleanup and move commands.
     For computationally intensive work, or very long compilation times, use batch jobs instead,
     or the [interactive partitions on Roihu](../../computing/running/batch-job-partitions.md#roihu-cpu-interactive-use).

## Start a tmux session

Connect to Roihu:

```bash
ssh <username>@roihu-cpu.csc.fi
```

Notify which login node you start the `tmux` session in, in the left corner of your terminal:

```bash
# E.g., if the session is on login2
[username@roihu-cpu-login2 ~]$
```

Start a new named `tmux` session:

```bash
tmux new -s my-session
```

After this, you are inside the `tmux` session and can run your commands as usual.

## Detach from a tmux session

To leave the `tmux` session while keeping the command running, press `Ctrl` and `b` at the same time, followed by pressing `d`:

```text
Ctrl-b d
```

After detaching, you can log out from Roihu or continue working in the normal terminal session.
Any commands you started in the `tmux` session will continue running in the session, in the background.

## Reconnect to a tmux session

Connect to Roihu, onto the same login node where you have the `tmux` session.

To target a specific login node (e.g. roihu-cpu-login2), use:

```bash
ssh <username>@roihu-cpu-login2.csc.fi
```

Then list your `tmux` sessions:

```bash
tmux ls
```

The output shows the names of your active sessions. For example:

```text
allas-upload: 1 windows (created Tue Jun 16 13:10:24 2026)
data-cleanup: 1 windows (created Tue Jun 16 14:05:02 2026)
```

Reconnect to a session of your choosing with e.g.:

```bash
tmux attach -t allas-upload
```

## End a tmux session

When your command has finished and you no longer need the session, exit the shell inside `tmux`:

```bash
exit
```

You can also press:

```text
Ctrl-d
```

This closes the shell and ends the `tmux` session.

## Navigating tmux

Tmux is slightly different from a normal terminal session you have on Roihu,
but it has some additional features that can be useful for managing parallel sessions.

### Scrolling in a tmux session

To scroll inside a `tmux` session, enter scroll mode:

```text
Ctrl-b [
```

Use the arrow keys or Page Up and Page Down to scroll.

Press `q` to leave scroll mode.

### Split the terminal into panes

You can split the terminal vertically with:

```text
Ctrl-b %
```

You can split the terminal horizontally with:

```text
Ctrl-b "
```

Move between panes with:

```text
Ctrl-b arrow-key
```

Close the current pane with:

```text
Ctrl-b x
```

And confirm by pressing `y`.

!!! warning
     Closing a pane also closes the shell running in that pane. If a command is
     running in the pane, closing the pane stops the command.

### Create another window inside tmux

Inside a `tmux` session, you can create another window with:

```text
Ctrl-b c
```

Move to the next window with:

```text
Ctrl-b n
```

Move to the previous window with:

```text
Ctrl-b p
```

Rename the current window with:

```text
Ctrl-b ,
```

## Troubleshooting

### I do not remember the session name

List your active `tmux` sessions:

```bash
tmux ls
```

Then attach to the correct session:

```bash
tmux attach -t session-name
```

### tmux says: no server running

If `tmux ls` prints an error like this:

```text
no server running
```

you do not have any active `tmux` sessions on that login node.

If you recently reconnected to the supercomputer, you may have ended up on a
different login node than the one where you started the `tmux` session.

### I cannot attach to a session

Check the available sessions:

```bash
tmux ls
```

Then attach to one of the listed sessions:

```bash
tmux attach -t session-name
```

If no sessions are listed, the session may have ended e.g. due to a login node reboot,
or you may be connected to a different login node than the one where you have your session open.