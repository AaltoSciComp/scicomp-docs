============================================
Aalto Linux (Science-IT flavor specifically)
============================================


CS-Linux is built on top of centrally maintained Aalto Ubuntu by Aalto
IT Services (ITS). Both laptop and desktop setups are available.

Basics
~~~~~~

-  New installations are using Ubuntu 16.04 LTS, but some former
   installations might have Ubuntu 14.04. The day-to-day management is
   done by CSIT.
-  `Some basic information from Aalto is availiable at
   Inside <https://inside.aalto.fi/display/ITServices/Linux>`__.
-  **Login is with Aalto credentials**. Anyone (not just CS staff) can
   log in to any computer.
-  All systems are effectively identical, except for local Ubuntu
   packages installed. Thus, switching machines is a low-cost operation.
-  Systems are centrally managed using puppet. Any sort of configuration
   group can be set up, for example to apply custom configuration to one
   group's computers.
-  Large scientific computing resources are provided by the Science-IT
   project. `The compute cluster there is named
   Triton <../triton/index>`__. Science-IT is a school of
   science collaboration, and its administrators are embedded in each
   department's IT. In CS, these are Mikko and Simo.
-  Workstations are on a dedicated VLAN. The network port must be
   configured before it can be turned on. You can request other network
   ports enabled for personal computers, just ask.
-  Installation is fully automated via netboot. Once configuration is
   set up, you can reboot and PXE boot to get a fresh install. There is
   almost no local data (except the filesystem for tmp data on the hard
   disks which is not used for anything by default, /l/ below), so
   reinstalling is a low-cost operation. The same should be true for
   upgrading, once the new OS is ready you reboot and netinstall.
   Installation takes less than two hours.

**When requesting a new computer:**

-  Contact CSIT
-  Let us know who the primary user will be, so that we can set this
   properly.

**When you are done with a computer:**

-  Ensure that data is cleaned up. Usually, if returned to CSIT disks
   will be wiped, but if this is important then confirm this with them.
   There may be data if you use the workstation local disks (not the
   default). There is also a local cache ($XDG\_CACHE\_HOME), which
   stores things such as web browser cache. Unix permissions protect all
   data, even if the primary user changes, but it is better safe than
   sorry. Contact CSIT if you want wipes.

Project groups
~~~~~~~~~~~~~~

Unix groups (managed by CSIT) provide access control to data and some
workstations. See `data management <../data/index>`__.

Storage available
~~~~~~~~~~~~~~~~~

See the general `storage page <../data/aaltostorage>`__ for the full
story.

Full disk encryption
~~~~~~~~~~~~~~~~~~~~

All new (Ubuntu 16.04) laptops come with full disk encryption by default
(`instructions <https://inside.aalto.fi/display/ITServices/Disk+Encryption+in+Aalto+Linux>`__).
This is a big deal and quite secure, if you use a good password.

**When the computer is first turned on**, you will be asked for a disk
encryption password. Enter something secure and remember it - you have
only one chance. Should you want to change this password, take the
computer to an Aalto ITS service desk. They can also add more passwords
for alternative users for shared computers. Aalto ITS also has a backup
master key.

Primary User
~~~~~~~~~~~~

**The workstations have a concept of the "primary user". This user can
install software from the existing software repositories and ssh
remotely to the desktops.**

-  Primary users are implemented as a group with name
   \`$hostname-primaryuser\`. You can check primary users by using the
   group querying commands above.
-  If you have a laptop setup, make sure you have the PrimaryUser
   privileges!
-  **Make sure to let us know about primary users when you get a new
   computer set up or change computers.** You don't have to, but it
   makes it convenient for you.
-  It is not currently possible to have group-based primary users (a
   group of users all have primary user capabilities across a whole set
   of computers, which would be useful in flexible office spaces). TODO:
   are we working on this? (however, one user can have primary user
   access across multiple computers, and hosts can have multiple primary
   users, but this does not scale well)

Installing software
~~~~~~~~~~~~~~~~~~~

**Ubuntu packages:**
^^^^^^^^^^^^^^^^^^^^

If you have PrimaryUser privileges, you can install Ubuntu packages
using one of the following commands:

-  By going to the Ubuntu Software Center (Applications -> System Tools
   -> Administration -> Ubuntu Software Centre)
-  aptdcon --install $ubuntu\_package\_name
-  pkcon install $ubuntu\_package\_namesoftware
-  By requesting CSIT to make a package available across all computers
   as part of the standard environment. Help us to create a good
   standard operating environment!

The module system
^^^^^^^^^^^^^^^^^

The command \`module\` provides a way to manage various installed
versions of software across many computers. This is the way that we
install custom software and newer versions of software, if it is not
available in Ubuntu. Note that these are shell functions that alter
environment variables, so this needs to be repeated in each new shell
(or automated in login)

-  \`module avail\` to list available package.
-  \`module load $name\` to load a module. This adjusts environment
   variables to bring various directories into PATH, LD\_LIBRARY\_PATH,
   etc.
-  We will try to keep important modules synced across the workstations
   and Triton, but let us know

Useful modules:

-  \`anaconda2\` will always be kept up to date with the latest Python
   Anaconda distribution, and kept synced across CS and Triton.

Remote access
~~~~~~~~~~~~~

See the `remote access page <remoteaccess>`__.

Laptops
~~~~~~~

-  You can get laptops with CS Linux on it. The are also managed in
   CSIT.
-  Each user should log in the first time while connected to the Aalto
   network, to cache authentication information.
-  Home directories can be synced with the Aalto home directories. This
   is done using unison. TODO: what about this?
-  If you travel, make sure that your primary user is set correctly
   before you go. The system configuration can't be updated remotely.
-  Otherwise environment is like the workstations
-  If the keychain password no longer works (it is an old Aalto password
   and you have since changed it), see `this page on changing the
   keyring
   password <https://inside.aalto.fi/display/ITServices/Changing+your+Linux+keychain+password>`__.
   Some places recommend changing the password on the laptop itself to
   prevent this problem. The same procedure may apply to workstations as
   well.

Triton
~~~~~~

Triton is not a main part of the CS computers, but is heavily used by CS
researchers. You should see the main documentation at the Triton user
guide, but for convenience some is reproduced here.

-  `Triton user guide <../triton/index>`__
-  **You can request a dedicate group node as part of Triton**.

   -  This is paid however your group would normally pay for dedicated
      resources
   -  Your group gets interactive and dedicated login access
   -  project/archive **are** mounted on your own node.
   -  You can more easily scale from your own node to the rest of
      triton.
   -  You have high-performance access to the scratch filesystem.
   -  The disadvantage is that it is not an identical environment to the
      workstations (though all files are still there).

-  Triton is CentOS (compatible with the Finnish Grid and Cloud
   Infrastructure), while CS workstations are Ubuntu. So, they are not
   identical environments, but we are trying to minimize the
   differences.

   -  Since it is is part of FGCI, it is easy to scale to more power if
      needed.

-  We will try to have similar software installed in workstation and
   Triton module systems.
-  The paths **/m/cs/** are designed to be standard across computers
-  The **project** and **archive** filesystems are not available on all
   Triton nodes. This is because they are NFS shares, and if someone
   starts a massively parallel job accessing data from here, it will
   kill performance for everyone. Since history shows this will
   eventually happen, we have not yet mounted them across all nodes.

   -  These are mounted on the login nodes, certain interactive nodes,
      and dedicated group nodes.
   -  TODO: make this actually happen.

-  Triton was renewed in 2016.
-  It is the goal to eventually have virtual machines for non-batch
   computing.
-  Triton login: login.triton.aalto.fi (requires account activation)

Common problems
~~~~~~~~~~~~~~~

Network shares are not accessible
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If network shares do not work, there is usually two things to try:

-  Permission denied related problems are usually solved by obtaining
   new Kerberos ticket with command 'kinit'

-  If share is not visible when listing directories, try to 'cd' to that
   directory from terminal. Shares are mounted automatically when they
   are accessed, and might not be visible before you try to change to
   the directory.

Graphical User Interface on Aalto CS Linux desktop is sluggish, unstable or does not start
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  

   #. Check your disk quota from terminal with command ``quota``. If you
      are not able to log in to GUI, you can change to text console with
      CTRL+ALT+F1 key combo and log in from there. GUI login can be
      found with key combo CTRL+ALT+F7.
   #. If you are running low on quota (blocks count is close quota), you
      should clean up some files and then reboot the workstation to try
      GUI login again

      -  You can find out what is consuming quota from terminal with
         command:
         bash -c 'cd && du -sch .[!.]\* \* \|sort -h'

Enter password to unlock your login keyring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should change your Aalto password in your main Aalto workstation. If
you change the password through e.g. https://password.aalto.fi, then
your workstation's password manager (keyring) does not know the new
password and requests you to input the old Aalto password.

If you remember your old password, try this:

#. Start application 'seahorse'
#. Click the "Login" folder under "Passwords" with right mouse button
   and select "Change password"
#. Type in your old password to the opening dialog
#. Input your current Aalto password to the "new password" dialog
#. Reboot the workstation / laptop

If changing password didn't help, then try this:

-  Then instead of selecting the "change password" from the menu behind
   right mouse key select "delete" and reboot the workstation. When
   logging in, the keyring application should use your logging key
   automatically.
