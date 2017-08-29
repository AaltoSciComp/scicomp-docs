=====================
VNC for graphical use
=====================

There is a vnc server and a lightweight desktop environment installed
on \ **the 1 TB fat node fn01**.

Create file in ~/.vnc/xstartup containing the following two lines:

::

    xfce4-session
    vncserver -kill $DISPLAY 

Add execute permissions:

::

    chmod +x .vnc/xstartup

Then run the vnc server, and note the display name (e.g. fn01:1):

::

    vncserver -geometry 1580x1140

Connecting the client later:

::

    vncviewer : 

The output of 'module avail' may look a little funky but all modules are
available under the X session.

 
