========================
IDA data storage service
========================

.. note::

   This page is under development

IDA is a storage service provided by the Ministry of Culture of
Education / the Finnish Open Science and Research initiative / CSC. It
can be used for storing very large files securely and for a reasonably
long time. Quota can be in many TB, and quota is allocated by
application.

The upstream instructions can be found at
http://openscience.fi/ida-user-instructions. The upstream description
can be found at http://openscience.fi/ida

What it is for
--------------

Main article: http://openscience.fi/ida

IDA is for stable research data which needs safe, somewhat long term
storage. (However, it isn't for very long term archival, another system
is coming for that). It isn't for active, day-to-day use. It can link
data to permanent identifiers, store metadata, and also publish data via
AVAA and make it searchable via Etsin.

If you just need large storage, Triton's scratch is good for that.
However, if you have many TBs of data, then finding a backup place is
difficult (scratch is not backed up). IDA can serve that need.

IDA can also serve to make small or large data open (searchable and
downloadable), via Etsin and AVAA. These three go together: IDA is
storage, Etsin is search, AVAA is download server.

You automatically get a quota from Academy of Finland projects (and it
says they encourage its use).

Registering and applying for space
----------------------------------

Main article: http://openscience.fi/becoming-an-ida-user

Everyone can apply for IDA space via your CSC account (but all IDA
space is allocated to projects, not individual users). Anyone at a
Finnish university can get a CSC account automatically. IDA space is

First, you need a CSC account. You can get this online via the Aalto
authentication: `https://sui.csc.fi/. <https://sui.csc.fi/>`__

Once you have the CSC account, you need a CSC project. Only senior level
staff (postdoc or above) can do this - you probably want it to be
someone who will be here long term, since that is the point!. Apply for
the project through the scientists user interface (SUI)
(https://sui.csc.fi). The SUI can be rather confusing. First, go to
eService → Resources and Applications → select "Academic CSC
project".  The bottom of the page then changes to an application form.
Fill this out: say you need a project for IDA (or whatever). You need
to wait for an email for the CSC project to be approved.

After this project is approved, you can apply for IDA storage space to
be connected to this project. Go to the SUI → eService → Resources and
Applications, then go to Resources → Storage → IDA Storage Service.
The application form below changes to the IDA application. Select the
project which will receive the resources, then fill out the application.

You will get another email with your IDA password and path once it has
been approved by Aalto's IDA contact person. This is different from the
project approval email from CSC (the right email has explicit IDA
usernames and passwords in it). If you do not get the IDA info email
within a day or two, ping Juha Juvonen at Aalto and ask if the project
has been approved.

Confidential data
-----------------

In many places, CSC states that IDA is not suitable for confidential
data. This is because the command line interface does not encrypt files
(though I had heard that it just doesn't by default, but maybe it could
be made to). Still, since they do not indent to support confidential
data, we should not count on this for the future. **However,
confidential data is OK if it is strongly encrypted.**

See our page on :doc:`encryption for scientists <../scicomp/encryption>`.

Access
------

Main instructions: http://openscience.fi/ida-user-instructions

iRODS (and thus IDA) is an API-based file storage service. Thus, you use
separate commands to get and put files. This comes out of the fact that
this is designed for very big files and flexible, long-term storage.
This is not too hard - it is like using FTP or scp. There are also
mountable filesystems, however this should not be used for daily work
since they are not very efficient.

Not all tools are suitable for very large files - there are some
reported problems that need to be worked around. See the CSC
instructions for details and hints for large files.

Note that the IDA password is different than your CSC or Aalto
passwords. Don't use your CSC or Aalto password with IDA accidentally,
some of the programs (command line tool in particular) don't seem to
handle it very securely (it is stored weakly obfuscated in a file in
``~/.irods``)

Browser
~~~~~~~

Through the CSC SUI, you can brows and upload files. See
http://openscience.fi/ida-browser.  This is probably not good for
extremely large files.

Command line
~~~~~~~~~~~~

Main instructions:
`http://openscience.fi/ida-command-line. <http://openscience.fi/ida-command-line>`__

**irods commands:** Aalto workstations and Triton have the irods command
line tools (the "icommands"). Use the module system:
``module load irods``.

**Configuration file:** You need to set up the config file (see the
openscience.fi instructions). You need a extra path in it here:

On Aalto Linux, this is needed in the config file
``.irods/irods_environment.json`` (be careful with commas to make sure
it stays valid JSON):

``"irods_plugins_home": "/work/modules/Ubuntu/14.04/amd64/common/irods/4.1.9/var/lib/irods/plugins/"``

On Triton, the corresponding directory is
``"/share/apps/irods/4.1.9/var/lib/irods/plugins/"``

Network mounting
~~~~~~~~~~~~~~~~

The IDA directories can be mounted via
DAV:\ http://openscience.fi/ida-network-directory

There is also an irods 4.x fuse module (irodsFs) included by default.
Use it like normal, though it is quite slow.

Practical usage
---------------

To be added once we have more specific use cases which are not covered
above.

More resources
--------------

Documentation

-  http://openscience.fi/ida-user-instructions - Instructions from
   avointiede
-  CSC webinar on IDA and opening data (2017):
   https://www.youtube.com/watch?v=b8nVRgUBH0Q,
   https://www.csc.fi/web/training/-/webinar_ida_2017.
-  https://research.csc.fi/csc-guide-archiving-data-to-the-archive-servers
   - CSC documentation, note that this is a bit out of date and less
   complete than Avointiede's one.
-  The CSC archive also uses irods, but it uses version 3 which is not
   compatible with these command line tools.


