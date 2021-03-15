# How to configure and use the NoMachine remote desktop to access CSC servers

This document will briefly highlight benefits of using NoMachine, how to configure
connection to CSC and how to further tailor the settings.

[TOC]

A short video will appear in here.

## Why use NoMachine at all?

**Pros:**

- Enables remote graphics from CSC servers for Windows users
- Improved remote graphics performance for Linux and Mac users
- Suspendable session - continue later with all terminals etc. as they were, even from a different computer
- Easy way to leave jobs running e.g. on the [interative partition](../../computing/running/interactive-usage.md) while logging off from laptop
- Gives 4 virtual screens
- Resolution/frame rate can be tuned - enables usage with even a really slow network

**Cons:**

- Very heavy 3D remote graphics performance will be poor. In this case, consider
  [using GPUs for rendering in cPouta](../faq/how-to-use-cpouta-gpu-for-rendering.md)
- Requires installing the client (ssh + X11 forwarding are available on Mac & Linux anyway)

## Installation

!!! note 
    this _may_ require admin privileges

Download the **NoMachine Enterprise client** (not the Desktop) from here: [https://www.nomachine.com/download-enterprise](https://www.nomachine.com/download-enterprise)

## Configuration

1.   Open NoMachine and click "Add" at the top bar.
2.   In the address tab fill in:
     * name: CSC 
     * host: `nxkajaani.csc.fi`
     * port: `4000` (default)
     * protocol: `NX` (default)
3.  In configuration tab the default settings are normally ok, including `Use password authentication`. 
4.  Click Connect.

If you need to use proxy, it can be done from main menu Settings -> Security tab.

## Open connection

1.   Double click the icon of the connection you just configured.
2.   Fill in your CSC username and password. 
3.   After a while, you'll be shown a few pages presenting the different functionality of NoMachine.
    In the first screen, untick the box from "Change server resolution to match the client when I reconnect".
4.   Take a while to read through, and if you don't want to see them again, click the box at lower right corner, proceed with "ok".
5.   Once you see a black screen, you're there. Now right click at the black background and select "CSC local servers" then "Puhti" / "Mahti.
6.   You'll be prompted for your CSC password. Give it, and you'll have a terminal open on Puhti / Mahti. The terminal can display remote graphics.

## Recommended tips

1. To get rid of the scroll bars at the edges of your screen take the mouse to the upper right corner (peel menu) and click "resize remote screen".

2. The default font in the terminal is ugly and small. Use the initial terminal to launch new prettier terminals. In Puhti you can launch regular xterm with some options, for example, write `xterm -fs 12 -fa "Bitstream"`.

## Known issues

If something is not working, before contacting ServiceDesk, please check if your issue is covered/solved below:

- Deselect "Match the client resolution upon reconnection" -option from the Display menu (access from "peel menu"). GUIs will work better.

- To get rid of the scroll bars, maximise your NX window and select the 1:1 icon (Resize remote screen) from the "peel menu".

- In Windows, if you have problems in the installation, try disabling "direct draw" from the advanced settings.

- If copy/paste does not work with the middle mouse button, try ctrl-alt-c / ctrl-alt-v

- If right-click does not bring up the server/application menu on the remote desktop, you can try to exit from the session and create a new desktop instead of reconnecting to the old desktop.

- The key mappings for Macs are not perfect. If you don't get a dollar sign "$" with alt-4 in the x-terminal, try using the right side alt key. That has worked on all Macs we have tested...

- The default keyboard layout may be wrong, and may change between logins. See FAQ. You can change that by right clicking in the background, Choose "fluxbox menu" -> "keyboard layout" and your keyboard. If yours is not listed, contact servicedesk@csc.fi. This affects connections from nxkajaani to compute servers. Don't try too many times because that will cause your username/IP to be banned.

- By default the remote desktop screen is quite small. If you want to have a full screen desktop, you may need to change settings in two steps. First open the peel menu (top right corner), choose display, and activate either "full screen" or "resize remote display". Click "done", open the peel menu and choose display again, and select the other option. You may need additional steps, but the options you need are in this menu.

- The terminal window handle is bar outside desktop. If you open the NoMachine remote connection on a smaller screen than you used last time, some terminal window handle bars (that you can use to drag them) may be outside the screen. You can drag the window my pressing "alt" on your keyboard and dragging with left mouse button directly from the terminal window. Mouse pointer turns to a "hand" symbol when the terminal can be dragged.

- Connection problems in Macs may be caused by local extra user account "nx", created by installing Desktop version instead of Client version of NoMachine. The extra user account may persist even after replacing Desktop version with Client version. Installing Client version and removing extra user account in local Mac solves the issue.
