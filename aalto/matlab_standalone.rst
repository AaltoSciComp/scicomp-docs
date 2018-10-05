=================
Standalone Matlab
=================

General matlab hints: http://math.aalto.fi/opetus/Mattie/MattieO/matlab.html

Installation and license activation on staff-owned computers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Matlab academic license permits installation on home computers for
university personnel. Triton MDCS workers are available to anyone with a
Triton account, which means the workers can be utilized from personal
laptops as well.

Download image
''''''''''''''

Log into http://download.aalto.fi/ with your Aalto account. Look for the
link *Software for employees' home computers* which will take you to the
Matlab download links. Download the UNIX version for Linux and OSX or
the separate separate image for Windows.

The ISO image can be burned on a DVD or mounted on a virtual DVD drive.

-  Windows: Use
   `MagicDisk <http://www.magiciso.com/tutorials/miso-magicdisc-overview.htm>`__
   or `Virtual
   CloneDrive <http://www.slysoft.com/en/virtual-clonedrive.html>`__ OR
   burn the image on DVD. Double click on setup.exe icon.
-  Linux:

   ::

       # sudo mkdir /mnt/loop
       # sudo mount -o loop Download/Matlab_R2010b_UNIX.iso /mnt/loop
       # sudo /mnt/loop/install.sh

-  Mac OS X: Double click on InstallForMacOSX.app icon.

Installation steps
''''''''''''''''''

Select the installer options as shown in the screenshots.

Mathworks account is required to continue with the installation.

-  Enter your account information in the installer to log in. If the
   password has been lost, Click on the *Forgot your password?* option
   to receive your password in email.
   *OR*
-  Register to Mathworks with the installer.

   #. Click on *I need to create an account*.
   #. Enter your name and email address. To be recognized as Aalto
      academic user the email address must end in one of aalto.fi,
      tkk.fi, hut.fi, hse.fi, hkkk.fi or uiah.fi domains.
   #. The installer will ask for an activation key, which is shown here
      in the last screenshot.

You may leave out unnecessary toolboxes and change the installation
location. Remember however, that the Parallel Computing Toolbox is
necessary to run any Matlab batch jobs on Triton.

Install Triton-MDCS integration scripts
'''''''''''''''''''''''''''''''''''''''

Continue MDCS setup from `Matlab Distributed Computing
Server <LINK/Matlab%20Distributed%20Computing%20Server>`__.


FAQ
~~~

Matlab freezes with Out of Memory errors
''''''''''''''''''''''''''''''''''''''''
Q: Matlabs freezes and I get errors like this.  What to do?::

  Exception in thread "Explorer NavigationContext request queue" java.lang.OutOfMemoryError: GC overhead limit exceeded
        at com.mathworks.matlab.api.explorer.FileLocation.<init>(FileLocation.java:89)
        at com.mathworks.matlab.api.explorer.FileLocation.getParent(FileLocation.java:126)
       ... ... ...

A1: Add more memory in Home -> Preferences -> General -> Java Heap
memory

A2: Can you free up memory in your code sooner using the ``clear`` command?
https://se.mathworks.com/help/matlab/ref/clear.html


GPU acceleration?
'''''''''''''''''
Q: is there functional GPU acceleration?  Does the acceleration even work?

A: run code::

  >> g = gpuDevice;
  >> ng

A2: Just query some feature::

  >> fprintf('%s\n', g.ComputeCapability)


a3: Show multiple devices if found::

  >> for ii = 1:gpuDeviceCount
  g = gpuDevice(ii);
  fprintf(1,'Device %i has ComputeCapability %s \n', ...
  g.Index,g.ComputeCapability)
  end
