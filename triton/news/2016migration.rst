:orphan:

Triton storage upgrade spring 2016
==================================

In the spring 2016 there are two major upgrades to the hardware. One is
the new cluster setup where we will upgrade also the whole operating
system to Centos7. This e.g. causes a transition period where we run the
old system (ssh old.triton.aalto.fi) and the new system (ssh
triton.aalto.fi) in parallel.

In addition we have obtained new storage solution to replace our old
Lustre system (/triton mount on nodes). The old system will be online
still by the end of May. While migrating to the new CentOS7 users need
to consider the data migration at the same time.

Data transfer
-------------

The outline is described in the image below. We have reserved a couple
of nodes (cn01 and cn02 from the old system and tb007 and tb008 from the
new system).

#. Login to old system old.triton.aalto.fi

#. Run syncLustre.sh script to sync the data to the new system

   ::

       $ ssh old.triton.aalto.fi
       $ syncLustre.sh

       # by default syncLustre.sh will use cn01 as source and copy to tb007, another option, if cn01 is crowded, run

       $ syncLustre.cn02.sh

       # the later one will use cn02 and tb008 as source and destination nodes correspondingly

       # the scripts are nothing else than a shortening for the rsync command

       $ cat /usr/local/bin/syncLustre.sh
       #!/bin/bash

       shost=cn01
       dhost=tb007
       rsync_args="$@"

       ssh $shost "rsync -au --no-g --chmod=Dg+s --progress --numeric-ids -e 'ssh -c arcfour128 -o Compression=no -o StrictHostKeyChecking=no' /triton/work/$USER/ $dhost:/scratch/work/$USER $rsync_args"

   | **Note:**\  Depending on the data size and how other people are
     utilizing the system, the transfer can take several hours. 
   | **Note2:** "``-o StrictHostKeyChecking=no``" is used as many may
     have old ssh-keys set in ~/.ssh/known\_hosts. If this gives WARNING
     you can clean the old keys for tb007 and tb008 to get rid of this
     message.

#. If you are using you Triton storage via Linux desktop machines,
   please contact you local support to update the system maps. This
   means, that when the data is migrated, you will get the NEW location
   visible to your workstation.

#. If in doubt or there are any challenges, please contact Triton
   support 

Data transfer for huge amount of files
--------------------------------------

For larger file amount (say 200k or more) it would be a good idea to
split the tranfer into chunks. E.g. as a shell script run this at cn01

::

    #!/bin/bash

    dhost=tb007
    rsync_args="$@"

    # simple for-loop over subfolders
    for dir in subfolder1 subfolder2 subfolder3
    do
     echo "now syncing subdir $dir"
     date
     rsync -au --no-g --chmod=Dg+s --progress --numeric-ids -e 'ssh -c arcfour128 -o Compression=no -o StrictHostKeyChecking=no' /triton/ics/project/myproject/$dir $dhost:/scratch/cs/myproject
    done

The script above does one subdirectory at time and makes the job more
manageable. Also, in case of a failure one may continue from the point
where the process failed. That is, if subfolder1 is already done, that
can be removed from the list

 
