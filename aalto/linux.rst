===========
Aalto Linux
===========


Aalto Linux is provided to all departments in Aalto.  Department IT
co-maintains this, and in some departments provides more support
(specifically, CS, NBE, PHYS at least).  It contains a lot of software
and features to support scientific computing and data.  Both laptop and desktop
setups are available.

This page is mainly about the Linux flavor in CS/PHYS/NBE, co-managed
by these departments and Science-IT.  Most of it is relevant to all
Aalto, though.



Basics
------

-  Aalto home directory. In the Aalto Ubuntu workstations, your home
   directory will be your Aalto home directory. That is, the same home
   directory that you have in Aalto Windows machines and the Aalto
   Linux machines, including shell servers (kosh, taltta, lyta, brute, force).
-  Most installations have Ubuntu 16.04, 18.04 is coming soon.
-  `Some basic information from Aalto is availiable at
   Inside <https://inside.aalto.fi/display/ITServices/Linux>`__.
-  **Login is with Aalto credentials**. Anyone can
   log in to any computer.  Since login is tied to your Aalto account,
   login is tied to your contract status.  Please contact HR if you
   need to access systems after you leave the university or your
   account stops working due to contract expiration.
-  All systems are effectively identical, except for local Ubuntu
   packages installed. Thus, switching machines is a low-cost operation.
-  Systems are centrally managed using puppet. Any sort of configuration
   group can be set up, for example to apply custom configuration to one
   group's computers.
-  Large scientific computing resources are provided by the Science-IT
   project. :doc:`The compute cluster there is named
   Triton <../triton/index>`. Science-IT is a school of
   science collaboration, and its administrators are embedded in NBE,
   PHYS, CS IT.
-  Workstations are on a dedicated network VLAN. The network port must be
   configured before it can be turned on and you can't just assume
   that you can move your computer to anywhere else. You can request
   other network
   ports enabled for personal computers, just ask.
-  Installation is fully automated via netboot. Once configuration is
   set up, you can reboot and PXE boot to get a fresh install. There is
   almost no local data (except the filesystem for tmp data on the hard
   disks which is not used for anything by default, ``/l/`` below), so
   reinstalling is a low-cost operation. The same should be true for
   upgrading, once the new OS is ready you reboot and netinstall.
   Installation takes less than two hours.
-  Default user interface. The new default user interface for Aalto
   Linux is `Unity
   <https://en.wikipedia.org/wiki/Unity_(user_interface)>`__. If you
   want to switch to the previous default interface (`Gnome
   <https://en.wikipedia.org/wiki/GNOME>`__), before logging in please
   select "Gnome Flashback (Metacity)" by clicking the round ubuntu
   logo close to the "Login" input field.
-  Personal web pages. What you put under ``~/public_html`` will be
   visible at ``https://users.aalto.fi/~username``.  See
   :doc:`aaltostorage`.

**When requesting a new computer:**

-  Contact your department IT
-  Let us know who the primary user will be, so that we can set this
   properly.

**When you are done with a computer:**

-  Ensure that data is cleaned up. Usually, disks
   will be wiped, but if this is important then you must explicitly
   confirm before you leave.
   There may be data if you use the workstation local disks (not the
   default). There is also a local cache (``$XDG_CACHE_HOME``), which
   stores things such as web browser cache. Unix permissions protect all
   data, even if the primary user changes, but it is better safe than
   sorry. Contact IT if you want wipes.

Laptops
~~~~~~~

-  You can get laptops with Linux on it.
-  Each user should log in the first time while connected to the Aalto
   network.  This will cache the authentication information, then you
   can use it wherever you want.
-  Home directories can be synced with the Aalto home directories. This
   is done using unison. TODO: not documented, what about this?
-  If you travel, make sure that your primary user is set correctly
   before you go. The system configuration can't be updated remotely.
-  Otherwise, environment is like the workstations.  You don't have
   access to the ``module`` system, though.
-  If the keychain password no longer works: see FAQ at the bottom.

Workstations
~~~~~~~~~~~~

Most material on this page defaults to the workstation instructions.



Primary User
------------

The workstations have a concept of the "primary user". This user can
install software from the existing software repositories and ssh
remotely to the desktops.

- Primary users are implemented as a group with name
   ``$hostname-primaryuser``. You can check primary user of a computer
   by using ``getent group $hostname-primaryuser`` or check your
   primary-userness with ``groups``.
-  If you have a laptop setup, make sure you have the PrimaryUser
   set!  This can't be set remotely.
-  **Make sure to let us know about primary users when you get a new
   computer set up or change computers.** You don't have to, but it
   makes it convenient for you.
-  It is not currently possible to have group-based primary users (a
   group of users all have primary user capabilities across a whole set
   of computers, which would be useful in flexible office spaces). TODO:
   are we working on this? (however, one user can have primary user
   access across multiple computers, and hosts can have multiple primary
   users, but this does not scale well)



Data
----

See the general :doc:`storage page <aaltostorage>` for the full story
(this is mainly oriented towards Linux).  All of the common shared
directories are available on department Linux by default.

We recommend that most data is stored in shared group directories, to
provide access control and sharing.  See :doc:`the Aalto data page
<aaltodata>`.

You can use the program ``unison`` or ``unison-gtk`` to synchronise
files.



Full disk encryption (Laptops)
------------------------------

All new (Ubuntu 16.04) laptops come with full disk encryption by default
(`instructions <https://inside.aalto.fi/display/ITServices/Disk+Encryption+in+Aalto+Linux>`__).
This is a big deal and quite secure, if you use a good password.

**When the computer is first turned on**, you will be asked for a disk
encryption password. Enter something secure and remember it - you have
only one chance. Should you want to change this password, take the
computer to an Aalto ITS service desk. They can also add more passwords
for alternative users for shared computers. Aalto ITS also has a backup
master key.  (If you have local root access, you can do this with
``cryptsetup``, but if you mess up there's nothing we can do).

Desktop workstations do not have full disk encryption, because data is
not stored directly on them.



Software
--------

Already available
~~~~~~~~~~~~~~~~~
- Python: ``module load anaconda`` (or anaconda2 for Python 2) (desktops)
- Matlab: automatically installed on desktops, Ubuntu package
  on laptops.

Ubuntu packages
~~~~~~~~~~~~~~~

If you have PrimaryUser privileges, you can install Ubuntu packages
using one of the following commands:

-  By going to the Ubuntu Software Center (Applications -> System Tools
   -> Administration -> Ubuntu Software Centre).  Note: some software
   doesn't appear here!  Use the next option.
-  ``aptdcon --install $ubuntu_package_name`` (search for stuff using
   ``apt search``)
-  By requesting IT to make a package available across all computers
   as part of the standard environment. Help us to create a good
   standard operating environment!

The module system
~~~~~~~~~~~~~~~~~

The command ``module`` provides a way to manage various installed
versions of software across many computers. This is the way that we
install custom software and newer versions of software, if it is not
available in Ubuntu. Note that these are shell functions that alter
environment variables, so this needs to be repeated in each new shell
(or automated in login).

-  See the :doc:`Triton module docs <../triton/tut/modules>` docs for
   details.
-  ``module avail`` to list all available package.
-  ``module spider $name`` to search for a particular name.
-  ``module load $name`` to load a module. This adjusts environment
   variables to bring various directories into ``PATH``, ``LD_LIBRARY_PATH``,
   etc.
-  We will try to keep important modules synced across the workstations
   and Triton, but let us know.

Useful modules:

-  ``anaconda`` and ``anaconda2`` will always be kept up to date with the latest Python
   Anaconda distribution, and we'll try to keep this in sync across
   Aalto Linux and Triton.



Admin rights
------------

Most times you don't need to be an admin on workstations.  Our Linux
systems are centrally managed with non-standard improvements and
features, and 90% of cases can be handled using existing tools:

Do you want to:

- Install Ubuntu packages: *Use* ``aptdcon --install $package_name`` *as
  primary user.*
- This website tells me to run ``sudo apt-get`` to install
  something.  *Don't, use the instructions above.*
- This website gives me some random instructions involving ``sudo`` to
  install their program.  These are not always a good idea to run,
  especially since our computers are networked, centrally managed, and
  these instructions don't always work.  Sometimes, these things can
  be installed as a normal user with simple modifications.  Sometimes
  their instructions will break our systems.  In this case, try to
  install as normal user and then send a support request first.  *If
  none of these work and you have studied enough to understand the
  risk, you can ask us.  Make sure you give details of what you want
  to do.*
- I need to change network or some other settings.  Desktops are
  bound to a certain network and settings can't be changed, users
  can't be managed, etc.
- It's a laptop: *then yes, there are slightly more cases you need
  this, but see above first.*
- I do low-level driver, network protocol, or related systems
  development.  *Then this is a good reason for root, ask us.*

If you do have root and something goes wrong, our help is limited to
reinstalling (wiping all data - note that most data is stored on
network drives anyway).

If you do need root admin rights, you will have to fill out a form and get a
new ``wa`` account, then Aalto has to approve.  Contact your
department IT to get the process started.



Remote access to your workstation
---------------------------------

If you are primary user, you can ssh to your own workstation from
certain Aalto servers, including at least ``taltta``.  See the
:doc:`remote access page <remoteaccess>`.



More powerful computers
-----------------------

There are different options for powerful computing.

First, we have desktop Linux workstations that are more powerful than
normal.  If you want one of these, just ask.  It includes a
medium-power GPU card.  You can buy a more powerful workstation if you
need, but...

Beyond that, we recommend the use of Triton rather than constructing
own servers which will only be used part-time.  You can either use
Triton as-is for free, or pay for dedicated hardware for your group.
Your own hardware as part of Triton means that you can use all Triton
and even CSC if you need with little extra work.  You could have your
own login node, or resources as part of the queues.

Triton is Aalto's high-performance computing cluster.  It is not a
part of the department Linux, but is heavily used by researchers. You
should see the main documentation at the :doc:`Triton user guide
<../triton/index>`, but for convenience some is reproduced here:

-  Triton is CentOS (compatible with the Finnish Grid and Cloud
   Infrastructure), while CS workstations are Ubuntu. So, they are not
   identical environments, but we are trying to minimize the
   differences.

   -  Since it is is part of FGCI, it is easy to scale to more power if
      needed.

-  We will try to have similar software installed in workstation and
   Triton module systems.
-  The paths ``/m/$dept/`` are designed to be standard across computers
-  The *project* and *archive* filesystems are not available on all
   Triton nodes. This is because they are NFS shares, and if someone
   starts a massively parallel job accessing data from here, it will
   kill performance for everyone. Since history shows this will
   eventually happen, we have not yet mounted them across all nodes.

   -  These are mounted on the login nodes, certain interactive nodes,
      and dedicated group nodes.
   -  TODO: make this actually happen.

-  Triton was renewed in 2016 and late 2018.
-  All info in the :doc:`triton user guide <../triton/index>`

Common problems
---------------

Network shares are not accessible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If network shares do not work, there is usually two things to try:

-  Permission denied related problems are usually solved by obtaining
   new Kerberos ticket with command 'kinit'

-  If share is not visible when listing directories, try to 'cd' to that
   directory from terminal. Shares are mounted automatically when they
   are accessed, and might not be visible before you try to change to
   the directory.

Graphical User Interface on Aalto CS Linux desktop is sluggish, unstable or does not start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  

   #. Check your disk quota from terminal with command ``quota``. If you
      are not able to log in to GUI, you can change to text console with
      CTRL+ALT+F1 key combo and log in from there. GUI login can be
      found with key combo CTRL+ALT+F7.
   #. If you are running low on quota (blocks count is close quota), you
      should clean up some files and then reboot the workstation to try
      GUI login again.

      -  You can find out what is consuming quota from terminal with
         command:
         ``bash -c 'cd && du -sch .[!.]\* \* \|sort -h'``

Enter password to unlock your login keyring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should change your Aalto password in your main Aalto workstation. If
you change the password through e.g. https://password.aalto.fi, then
your workstation's password manager (keyring) does not know the new
password and requests you to input the old Aalto password.

If you remember your old password, try this:

#. Start application Passwords and Keys ("seahorse")
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

In linux some process is stuck and freezez the whole session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can kill a certain (own) process via text console.

How do I use eJournals, Netmot and other Aalto library services from home?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is a weblogin possibility at Aalto Library. After this, all
library provided services are available. There are links for journals
(nelli) and netmot.

Rsync complains about Quota, even though there is plenty left.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The reason usually is that default ``rsync -av`` tries to preserve the
group. Thus, there is wrong group in the target. Try using
``rsync -rlptDxvz --chmod=Dg+s <source> <target>``. This will make group
setting correct on ``/scratch/`` etc and quota should then be fine.

Quota exceeded or unable to write files to project / work / scratch / archive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most likely this is due to wrong Linux filesystem permissions. Quota
is set per group (e.g. braindata) and by default file go to the
default group (domain users). If this happens under some project,
scratch etc directory it will complain about "Disk quota exceeded".

In general this is fixed by admins by setting the directory
permissions such that all goes ok automatically. But sometimes this
breaks down. Some programs often are responsible for this (rsync, tar
for instance).

There are two easy ways to fix this

- In terminal, run the command ``find . -type d -exec chmod g+rwxs {} \;``
  under your project directory. After this all should be working
  normally again.
- If it's on scratch or work, see the :doc:`Triton quotas page <../triton/usage/quotas>`
- Contact NBE-IT and we will reset the directory permissions for the given directory

I cannot start Firefox
~~~~~~~~~~~~~~~~~~~~~~
There are two reasons for this.

.. rubric:: 1. Your network home disk is full

.. code-block:: bash

  # Go to your user dir
  cd ~/..
  # Check disk usage
  du -sh *

The sum should be less than the max quota which is 20GB. If your disk is full then delete something or move it to a local directory, ``/l/``.

.. rubric:: 2. Something went wrong with your browser profile

If you get an error like "*The application did not identify itself*", following might solve the issue.

Open terminal,

.. code-block:: bash

    firefox -P -no-remote

This will launch Firefox and ask you to choose a profile. **Note that when you delete a profile you delete passwords, bookmarks and etc.** So it's better to create a new profile, migrate bookmarks and delete the old one.
