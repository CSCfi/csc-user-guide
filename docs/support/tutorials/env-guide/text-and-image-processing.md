# 2.2 Editing text and viewing images {#editing-text-and-viewing-images .western style="page-break-before: always;"}

Editing text files by typing in Linux systems can be done with so called
*text editor* programs. Editors are normally used to modify or create
relatively small files like programs, parameter files or small input
files. Systematic modifications to large input or output data files are
normally done with other tools.

Several text editors are available in the CSC computing environment.
Here we briefly introduce just three of them: **nano**, **emacs** and
**vim**. Other frequently used text editors include **vi** and
**gedit*****.*** In addition to these general purpose text editors, many
application programs include their own special editing tools.

## [][1]2.2.1 Nano {#nano .western}

[][2]**Nano** is a simple and handy tool for editing small files. It is
easy to use and it suits well as the first text editor of a novice Linux
user. Nano is a text based editor: it does not include any mouse based
functions or command menus. Nano starts with command:

    nano text_file_name

 

This command opens the given file to the editor or creates a new empty
file if the file does not already exist.

When the nano editor has started, you can see the basic commands listed
in the bottom of the screen. The listed commands are executed by
pressing simultaneously the control key: *Ctrl*, into which the program
refers with **^** sign, and some of the listed keys. For example you can
read the exit from the program with ***Ctrl-x***, save the changes with
***Ctrl-o*** or read a new file to the editor with ***Ctrl-r*****.** If
you already have some text in *nano*, ***Ctrl-r*** will add the content
of the selected file to the end of the previously created text. With
***Ctrl-v*** you can browse the text one page forward and with
***Ctrl-y*** one page backwards. ***Ctrl-W*** command can be used to
search certain strings (words) from the text. ***Ctrl-k*** cuts one line
of text. To cut larger regions, first mark the beginning of the text to
be copied with ***Ctrl-6*** then move the cursor to the end of the area
and press ***Ctrl-k***. To paste the text that was cut, press
***Ctrl-u***. More commands can be found from the nano help text, that
is opened by pressing ***Ctrl-g***.

![][3]

**Figure 2.1** Nano editor.

## [][4]2.2.2 Emacs {#emacs .western}

[][5]**Emacs** is a versatile editor that contains large amount of
commands, functions and extensions. *Emacs* can be used in two ways: as
character based editor like *nano* or through a graphical interface.
Using the graphical interface requires that you have FreeNX or X-term
connection to CSC. In the character based mode emacs commands are given
using *Ctrl* and *Esc* keys much like in the case of nano commands. In
the graphical interface you can use also mouse based command menus which
makes working much more feasible for a new emacs user. To start emacs in
CSC environment type:

    emacs file_name

If a graphics enabling connection between CSC and your local computer
exists, the command will launch the graphical *emacs* interface.
Otherwise the character based mode is used. In the graphical user
interface the ***File*** menu is used to read in and save files.
***Edit*** menu include commands to copy, cut and paste text. This menu
also contains tools to search and replace strings. With the commands in
the *Options* menu you can control many properties of *emacs.* You can
for example use *Syntax highlighting* when you are working with a
program or a shell script file. You can have several files opened in one
emacs session. The ***Buffers*** menu allows you to choose the buffer to
be edited. The ***Tools*** menu contains miscellaneous commands and
tools.

![][6]  
**Figure 2.2:** Graphical interface of emacs editor.

 

## [][7]2.2.3 vim {#vim .western}

[][8]**Vim** is a highly configurable text editor built to enable
efficient text editing. It is an improved version of the ***vi*** editor
distributed with most UNIX systems.*[][9] vi* is the de facto standard
Linux editor. Essentially all Linux systems come with *vi* (or a
variant, like *vim*) built in.

*Vim* is often called a "programmer's editor," and so useful for
programming. It's however not just for programmers, though. *Vim* is
suitable for all kinds of text editing, from composing email to editing
configuration files.

To start *vim* in CSC environment type:

    vi file_name

*or*

    vim file_name

 

Vim differs from many editors in that it has two main modes of
operation: *command mode*, and *insert mode*. This is the cause of much
of the confusion when a new user is learning it.

To switch to the insert mode one needs to press the **i** key. When you
have finished entering a text, press **Esc** to return to the command
mode.  
To save the file enter command **:w *file\_name***. The command to quit
*vim* is **:q**, which needs to be issued in command mode.  
To exit vim without saving, and ignoring any warnings about unsaved
data, use a variation of the :q command, i.e., **:q!**  
This will return you to the prompt, without saving any changes to the
file, and with no warnings about unsaved data. This command should be
used carefully.

To enter insert mode and insert text at current position, type **i** and
start typing a text, to append text after current position, type **a**.
To delete characters while in insert mode, use *Backspace* and *Delete*
keys.

For more options, please refer to vim manual.

 

![][10]

  
**Figure 2.3:** Graphical interface of vim editor with welcome screen.

 

## [][7]2.2.4 Image and PostScript viewers {#image-and-postscript-viewers .western}

In some cases application programs, executed at CSC, produce image files
instead of text files. If you have a working FreeNX or X-term connection
between your local computer and CSC you can use [**eog**] (Eye of GNOME)
and [**evince**] programs to view image files. *Eog* is a simple image
viewing program that can display common image formats like *png*, *bmp*,
*jpg* and *tiff*. However *eog* is not able to show *PostScript* (ps) or
*pdf* files. For these file types you can use program *evince*.

To view a jpg file, type:

    eog image_name.jpg

 

and to view a PostScript file, type:

    evince file_name.ps

 

*Post script* files can be converted to *pdf* documents with command
**ps2pdf**. This command reads a *PostScript* file and prints out
corresponding *pdf* file. For example command:

    ps2pdf file1.ps

 

Produces a pdf-formatted file *file1.pdf*

![][11]  
**Figure 2.4**: Eog image viewing program

 

 

  [1]: https://research.csc.fi/ {#2.2.1}
  [2]: https://research.csc.fi/ {#nano}
  [3]: https://research.csc.fi/documents/48467/84606/nano.jpg/283cd66e-4edb-44bf-a9b1-27c78dd185c0?t=1383892703910
  [4]: https://research.csc.fi/ {#2.2.2}
  [5]: https://research.csc.fi/ {#emacs}
  [6]: https://research.csc.fi/documents/48467/84606/emacs.jpg/d1cc2ab9-66fc-4a2b-b1c1-aa078b2435ee?t=1383892792023
  [7]: https://research.csc.fi/ {#2.2.3}
  [8]: https://research.csc.fi/ {#vim}
  [9]: https://research.csc.fi/ {#vi}
  [10]: https://research.csc.fi/documents/48467/84606/vim_welcome_screen.jpg/68968b3a-36a2-4105-9502-7dbd979a74c0?t=1465579596279
  {width="685" height="365"}
  [**eog**]: https://research.csc.fi/ {#eog}
  [**evince**]: https://research.csc.fi/ {#evince}
  [11]: https://research.csc.fi/documents/48467/84606/eog.jpg/16f91075-1bed-4898-9e2a-5d2cee8175cf?t=1383892872990
