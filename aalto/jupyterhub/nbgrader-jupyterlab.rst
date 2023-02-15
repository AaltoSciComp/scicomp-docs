Doing Assignments in JupyterLab
===============================

.. note::

    This is a tutorial for courses that distribute and collect
    their assignments on `JupyterHub <https://jupyter.cs.aalto.fi>`__.
    Feel free to use it for your other courses as well, but
    note that you won't be able to collect and submit your
    assignments this way.

Go to https://jupyter.cs.aalto.fi and sign in with your account to access JupyterHub.
You can find more general information about it in :doc:`../jupyterhub`.
Select your course and start a session. Your will see that you are under the ``notebooks/`` folder,
which is your home directory. Make sure you put everything important here, files saved
elsewhere will get deleted when your session ends.

.. figure:: img/home.png
   :align: center
|
You can see currently available assignments by going to "Nbgrader->Assignment List"
in the menu bar.

.. figure:: img/assignment_list.png
   :align: center
|
If no assignments are visible, make sure the right course is selected
in the drop down menu. It might also be possible that your instructor has
not released any assignments yet.

Click in the "Fetch" button to download the assignment into ``notebooks/<course-name>/``.

.. figure:: img/fetch_before.png
   :align: center
.. figure:: img/fetch_after.png
   :align: center
|
You can also click on the assignment name under "Downloaded assignments" to list
and quickly open the associated notebooks.

.. figure:: img/downloaded.png
   :align: center
|
Follow the instructions in the notebook, and don't forget to save your work!
Once you are done, you can go back to the Assignment List and press the "Submit" button.
You can submit an assignment multiple times, but your instructor will probably use
only your latest submission.

At this point, you can delete the assignment files from your ``notebooks/`` directory if you'd like,
but it is often a good idea to keep a copy of your work somewhere.

Some courses might also give you feedback on your assignment here.
If you press the "Fetch Feedback" button before your instructor releases feedback,
nothing will happen. Pressing the button when feedback is available will download
it into ``notebooks/<course-name>/feedback/<submission>/``. You can also
click on "view feedback" to open this folder immediately.

.. figure:: img/feedback.png
   :align: center
|
Each notebook in the assignment will have a corresponding feedback file,
where you can see how your responses were graded along with comments left by the grader.
