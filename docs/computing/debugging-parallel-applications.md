# Debugging Parallel Applications
## TotalView debugger
TotalView is a debugger with graphical user interface (GUI) for debugging parallel applications. TotalView can:

* run an application under TotalView control
* attach to a running application
* examine a core file

## Debugging an Application
Set up debugger environment

```
module load totalview
```
Compile the application to be debugged, for example Fortran, c or C++ program. The compiler option -g is generating the debug information. Below Intel MPI wrapper examples.

```
mpiifort -g -o myprog mycode.f90
mpiicc -g -o myprog mycode.c
mpiicpc -g -o myprog mycode.C
```
Enter a launching command to start TotalView on the application you would like to debug. For example 8 core half an hour session in parallel partition
```
salloc -n 8 -t 00:30:00 -p parallel totalview srun -a ./my_parallel_prog
```
Totalview Startup Parameters window may appear. Just clik Ok button (in a basic case).
![Startup Parameters window](/docs/img/StarupParameters1.png)
TotalView Root and Process window appear. Click the GO  button in the Totalview process window. A pop-up window appears, asking if you want to stop the job. 
Select Yes in this pop-up window.
![Process window](/docs/img/ProcessWindowTotalview1.png) 
**Figure** Totalview Process window

![Popup window](/docs/img/QuestionDoYouWantToStopJob1.png)
**Figure** PopUp window


![Root window](/docs/img/RootTotalview.png)

**Figure** Totalview Root window

## Very basic features of Totalview
The Process Window contains the code for the process or thread that you're debugging.
This window is divided into panes of information. The Stack Trace Pane shows the call stack of routines. 
The Stack Frame Pane displays all of a routine's parameters, its local variables, and the registers for the selected stack frame.

The left margin of the Source Pane displays line numbers. An ARROW over the line number shows the current location of the program counter (PC) in the selected stack frame. One can place a breakpoint (left mouse click) at any line whose line number is contained within a box. After setting one or many breakpoints Go button executes your code to the next breakpoint. When one is placing a breakpoint on a line, TotalView places an icon over the line number. To remove a breakpoint just click the breakpoint icon one more time.

To examine or change a value of a variable right click the variable and select Dive from the pop up menu. To see the values of that variable on all processes select Across Processes from the pop up menu. A new window will show the values and other information from that variable. On that window one can edit the variable values.

Stepping commands Go, Next, Step, Out and Run to (on the top of Process window) are controlling the way one is executing the code. Go means go to the next breakpoint, if a breakpoint locates inside a loop the next breakpoint is the same until loop ends. Next executes the current line and the program counter (arrow) goes to next line. Step executes one line in your program and if the source line or instruction contains a subroutine or function call, TotalView steps into it. Out executes all statements within subroutine or function and exits. Run To executes all lines until the program counter reaches the selected line. A line is selected by clicking a code line (not the line number) and the background of that line turn grey.

## Debugging running application
It is also possible to "attach" TotalView to an application which is already running. The job can be interactive or a batch job.

First find out the nodes where your application is running. That can be done if the identication number of the job is known. The command _squeue_ displays information about your SLURM jobs.
```
squeue -u $USER
```
With job-id-number option _squeue_ displays information about a chosen job.
```
queue -j <job id> -l
```
The variable "NODELIST" will contain the nodes where the job is running, for example if NODELIST=c[579-580], the nodes are c579 and c580.

Start TotalView (remember to run setup command *module load totalview* before launching TotalView).
```
totalview
```
From the Start a Debugging Session (see image, blue boundary line) select "a running program (attach)".

![Start a Debugging Session](/docs/img/StartDebuggingSession1.png)

**Figure**  Debug session type "attach to a running application"

Next window called Attach to running program(s) will open.  By Clicking the "H+" button the "Add Host" window will open. There it is possible to add the host(s) where an application processes are running. Add the first compute node name from the list "NODELIST" (in this example c579) and clik "Ok" button. The processes from the selected node(s) will appear. Now the processes can be selected/deselected by clicking. Select (double-click) the upper srun process (see blue arrow). Then click green "Start Session" button.

![Choose and attach to processes](/docs/img/attachtouppersrun1.png)

**Figure**  Attach to running program(s)

After some time the Totalview Process window and Root window will pop up. See which rank is on the Process window (Rank 1 in this example). From the Root window choose "unknown line" from the same Rank (1 in this example) by clicking "unknown line" (the line that has black background). Then by clicking source code file from the Stack Trace pane (the line that has black background) the source code will appear on the Source pane and it is possible to see in which code line is the Totalview Program Counter (the yellow line on the Source pane). Now normal Totalview debugging process may continue.

![Choose and attach to processes](/docs/img/attachrunning2.png)

**Figure**  Debugging session is ready to continue.

