# How to configure and use the NoMachine remote desktop to access CSC servers

This document will briefly highlight benefits of using NoMachine, how to configure
connection to CSC and how to further tailor the settings.

[TOC]

TODO: add video of the steps below in here.

## Why use NoMachine at all?

**Pros:**

- Enables remote grahpics from CSC servers for Windows users
- Improved remote graphics performance for Linux and Mac users
- Suspendable session - continue later with all terminals etc. as they were, even from a different computer
- Easy way to leave jobs running e.g. on Taito-shell while logging off from laptop
- Gives 4 virtual screens
- Resolution/frame rate can be tuned - enables usage with even a really slow network

**Cons:**

- Very heavy 3D remote graphics performance will be poor. In this case, consider GPU rendering (link)
- Requires installing the client (ssh + X11 forwarding are available on Mac & Linux anyway)
- ...

## Installation (may require admin privileges)

Download the NoMachine Enterprise _client_ (not the Desktop) from here: [https://www.nomachine.com/download-enterprise](https://www.nomachine.com/download-enterprise)

## Configuration (should not require admin privileges)

1.   Open NoMachine and click "new" at the top bar (or "Create a new connection" if you see one).
2.   Accept the "NX" protocol and click continue.
3.   Fill in nxkajaani.csc.fi as the host, keep the port default port (4000) and click continue.
4.   Accept the default (password) and click continue.
5.   Unless you know that you need a proxy, accept the default (no proxy) and click continue. If your organization uses a proxy, contact your local IT support for the configuration.
6    Give some name for your setup and click Done.

## Open connection

1.   Double click the icon of the connection you just configured.
2.   Fill in your CSC username and password. 
3.   After a while, you'll be shown a few pages presenting the different functionality of NoMachine.
    In the first screen, untick the box from "Change server resolution to match the client when I reconnect".
4.   Take a while to read through, and if you don't want to see them again, click the box at lower right corner, proceed with "ok".
5.   Once you see a black screen, you're there. Now right click at the black background and select "CSC local servers" then "Taito".
6.   You'll be prompted for your CSC password. Give it, and you'll have a terminal open on Taito. The terminal can display remote graphics.

## Recommended tips

1.   To get rid of the scroll bars at the edges of your screen take the mouse to the upper right corner (peel menu) and click "resize remote screen".
2.   To improve cognitive ergonomy, start a `gnome-terminal` in the fluxbox terminal as the first thing, once logged in Taito/Puhti/... It looks nicer and you can change font size (ctrl-+)

## Known issues

If something is not working, before contacting ServiceDesk, please check if your issue is covered/solved below:

Deselect "Match the client resolution upon reconnection" -option from the Display menu (access from "peel menu"). GUIs will work better.

To get rid of the scroll bars, maximise your NX window and select the 1:1 icon (Resize remote screen) from the "peel menu".

The default font in the terminal is ugly and small. To improve, start gnome-terminal (write
```
gnome-terminal
```
on the command line) as the first thing, when you have a terminal in either Taito or Sisu. The font is then resizable on the fly.

In Windows, if you have problems in the installation, try disabling "direct draw" from the advanced settings.

If copy/paste does not work with the middle mouse button, try ctrl-alt-c / ctrl-alt-v.

If right-click does not bring up the server/application menu on the remote desktop, you can try to exit from the session and create a new desktop instead of reconnecting to the old desktop.

If Mathematica stalls after the "splash" screen, kill your terminal and start Mathematica again with "--nosplash" on the command line.

The key mappings for Macs are not perfect. If you don't get a dollar sign "$" with alt-4 in the x-terminal, try using the right side alt key. That has worked on all Macs we have tested...

The default keyboard layout may be wrong, and may change between logins. See FAQ. You can change that by right clicking in the background, Choose "fluxbox menu" -> "keyboard layout" and your keyboard. If yours is not listed, contact servicedesk@csc.fi. This affects connections from nxkajaani to compute servers. Don't try too many times because that will cause your username/IP to be banned.

If you get garbled fonts in some (old) applications, it could be due to the old binary not being able to utilize server side fonts, but needs those fonts installed on the client side. This has happened at least with the old emacs version in vuori. To fix this, install additional fonts to the client. The instructions and fonts can be found in here: http://www.nomachine.com/download-package.php?Prod_Id=3565

Small screen size by default the remote desktop screen is quite small. If you want to have a full screen desktop, you may need to change settings in two steps. First open the peel menu (top right corner), choose display, and activate either "full screen" or "resize remote display". Click "done", open the peel menu and choose display again, and select the other option. You may need additional steps, but the options you need are in this menu.

Terminal window handle bar outside desktop. If you open the NoMachine remote connection on a smaller screen than you used last time, some terminal window handle bars (that you can use to drag them) may be outside the screen. You can drag the window my pressing "alt" on your keyboard and dragging with left mouse button directly from the terminal window. Mouse pointer turns to a "hand" symbol when the terminal can be dragged.

Frozen session Sometimes your remote desktop session may "freeze" e.g. due to insufficient memory on the gateway machine. It may then happen, that when you try to make a new session, the client will default to the old frozen session. You may try the following workaround. In the opening dialog click "configure" and change the desktop from e.g. gnome to KDE. Save, and connect. You should now get an option to kill the old session and start a new one. Instead of the KDE desktop you'll get the same fluxbox that is started with the gnome –choice.
