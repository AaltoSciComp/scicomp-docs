=================
Aalto speech2text
=================


Aalto speech2text app is available to researchers of Aalto University. 

The app is run on the `Aalto Triton cluster <https://scicomp.aalto.fi/triton/>`_ and its usage is free for all Aalto researchers (master's thesis workers, doctoral students, post docs, visiting researchers). 

Supported languages are:

arabic, armenian, bulgarian, catalan, chinese, czech, danish, dutch, english, estonian, finnish, french, galician, german, greek, hebrew, hindi, hungarian, icelandic, indonesian, italian, japanese, kazakh, korean, latvian, lithuanian, malay, marathi, nepali, norwegian, persian, polish, portuguese, romanian, russian, serbian, slovak, slovenian, spanish, swedish, thai, turkish, ukrainian, urdu, vietnamese

.. note::

    If you use speech2text in your research, `please acknowledge Triton and the Aalto Science-IT project in your publication <https://scicomp.aalto.fi/triton/acknowledgingtriton/>`_. 

In order to transcribe your speech files into text, apply the following steps (detailed instructions in the sections below):

#. Create a Triton cluster account (only done once)
#. Connect to Triton
#. Copy your audio and/or video files to Triton
#. Submit the uploaded files for processing
#. Inspect and copy result to your personal computer
#. Delete unneeded files and folders from Triton workspace (optional)

.. note::

    The workflow described here is suitable for processing sensitive and personal data.
    All data uploaded to and processed on Triton are stored on servers managed by Aalto and can only be accessed from within Aalto network. The files and folders on Triton are protected by standard Unix permissions so that only their owner (you) and Triton administrators has access to them.

.. note::

    If at any point something doesn't work or you are unsure how to proceed, do not hesitate to contact `the Aalto RSEs <https://scicomp.aalto.fi/rse/>`_. 

    You can visit us at `the daily Zoom help session at 13.00-14.00 <https://scicomp.aalto.fi/help/garage/#id1>`_ where we can e.g. create a Triton account for you, walk through the speech2text workflow together, answer questions, help with data analysis, and more.

    You can also check the list of `known issues and troubleshooting <#known-issues-and-troubleshooting>`_.


Create a Triton account (only done once)
=========================================

Triton is the Aalto high-performance computing cluster where we will run the speech2text app. 

Access is free for Aalto researchers.

If you don't already have a Triton account, please, visit the `account page <https://scicomp.aalto.fi/triton/accounts/>`_ and proceed to fill the account request form. 

.. note::

    Activating the account takes on average 1-2 work days. 

    However, if you are in a hurry, visit us at `the daily Zoom help session at 13.00-14.00 <https://scicomp.aalto.fi/help/garage/#id1>`_ and we can speed up the process.


Connect to Triton
=================

Go to Triton's web browser interface `Open On Demand <http://ondemand.triton.aalto.fi>`_. 

Log in with your Aalto username and password. (You will be granted access since your Aalto account has been synced with your Triton account.)

.. note::

    To connect to Open On Demand, you need to be inside Aalto network OR use the Aalto VPN.


Copy your audio and/or video files to Triton
============================================

On the Open On Demand front page, click the ``Files`` dropdown menu from the left upper corner and select ``Work /scratch/work/yourusername``.

.. image:: speech2text_files_workspace.png

On the ``Files`` page, you can see the existing contents (files and folders) of your workspace on Triton.

Click on the ``Upload`` button in the right upper corner.

.. image:: speech2text_upload1.png

In the following pop-up window, select ``browse folders``.

.. image:: speech2text_upload2.png

In the following file browser, you will able to select the folder on your computer with the audio/video files. (Here, the folder we are uploading is called ``my-audio-folder``.)

.. note::

    Audio files can be of any common audio format, e.g. ``.wav``, ``.aiff``, ``.mp3``, ``.m4a``, ``.aac``, ``.ogg``
  
    The files can also be of any comon video format, e.g. ``.mp4``, ``.mov``, ``.avi``
 
.. note::

    We recommend following these practices when uploading your files to Triton:

    While not strictly necessary, it is a good practice to put the audio files in a folder even if you only have one. This will keep your workspace organized on both Triton and your own computer.

    Make sure your folder and file names do **not** contain white spaces or special characters apart from dash, underscore, and period, that is, use ``my-audio-folder`` and ``my_audio_file.mp3`` instead of ``my audio folder`` and ``my"audio"file!.mp3``, respectively.

    It is recommended to divide files into folders according to language, that is, put English interview files in folder ``my-english-interviews``, French interviews to ``my-french-interviews``, and so forth.

Finally, if your browser asks for confirmation, (``Are you sure you want to upload all files from “my-audio-folder”? Only do this if you trust the site.``), you can answer "yes".

Depending on the size of your audio files and the quality of your internet connection, the transfer can take a short or a long time (from a few seconds to several hours). Remember that video files are in general much bigger than audio files.

After the transfer is done, you should see your folder in the list of existing content on the `Files` page.

.. image:: speech2text_upload3.png

.. note::

   Some people have been experiencing difficulties with the Open On Demand file upload.

   If you receive a "File Upload Failed" error several times in a row, you can visit us at `the daily Zoom help session at 13.00-14.00 <https://scicomp.aalto.fi/help/garage/#id1>`_ and we can figure it out.


Submit the uploaded files for processing
=========================================

Open the `Applications` drop down menu from the left upper corner and choose speech2text.

.. image:: speech2text_applications.png

This opens the speech2text submission form.

.. image:: speech2text_submit.png

In the submission form

#. Use the `Select Path` button to browse and select your audio file/folder you just uploaded to Triton. This field is mandatory.

#. Add your Aalto email address. This field is mandatory.

#. Choose language of the audio. This field is mandatory.

#. You can leave the Model version field to "default" - this will use the latest available model.

Finally, press `Launch` and you're done! 

You will get an email notification when the results are available.



Inspect and copy result to your personal computer
==================================================

After receiving an email saying audio file(s) has finished processing, log back into `Open On Demand <http://ondemand.triton.aalto.fi>`_.

At the Open On Demand front page, select again the `Files` and `Work` page (upper left corner). Enter your audio folder. 

You should now see the newly created `results` folder.

Enter the `results` folder and notice there are two result files corresponding to each audio file:

- `.csv` files: e.g. `test.csv`

- `.txt` files: e.g. `test.txt`

Example of `.csv` output format (computer-friendly):

.. code-block:: csv

    start,end,speaker,transcription
    00:00:00,00:00:05,SPEAKER_00,"This is the first sentence of the first speaker."
    00:00:06,00:00:10,SPEAKER_00,"This is the second sentence of the first speaker."
    00:00:11,00:00:15,SPEAKER_01,"This is a sentence from the second speaker."
    00:00:16,00:00:20,SPEAKER_00,"This is the first speaker speaking again."

Corresponding example of `.txt` output format (human-friendly):

.. code-block:: text

    (00:00:00 - 00:00:10) SPEAKER_00

    This is the first sentence of the first speaker. This is the second sentence of the first speaker.

    (00:00:11 - 00:00:15) SPEAKER_01

    This is a sentence from the second speaker.

    (00:00:16 - 00:00:20) SPEAKER_00

    This is the first speaker speaking again.

The `.txt` files have basic text format and can be opened in a text editor (e.g. Microsoft Word, Google Docs). 

The `.csv` files have comma separated table format which is easy to read by computers and can be opened in a spreadsheet software (e.g. Microsoft Excel, Google Sheets).

You can either download individual result files or the whole `results` folder if you want to continue working on them on your personal computer using your preferred software. (Check the dropdown menus next to individual files and folders.)

.. note::

    The result files for a single audio file are created only **after** the processing of that audio file has been fully completed.

    In other words, if you can see and access the result files, you are free to move/copy them as the processing has already completed.







Delete unneeded files and folders from Triton workspace (optional)
==================================================================

If you do not need your audio and/or result files and/or folders, you can remove them by selecting `Delete` from the dropdown menus next to individual files and folders.



Known issues and troubleshooting
================================

If at any point something doesn't work or you are unsure how to proceed, do not hesitate to contact `the Aalto RSEs <https://scicomp.aalto.fi/rse/>`. You can visit us at `the daily Zoom help session at 13.00-14.00 <https://scicomp.aalto.fi/help/garage/#id1>`_ where we can walk through the speech2text workflow together, debug problems, answer questions, help with data analysis, and more.

My transcription has a weird segment where a word or two are repeated over and over.
-------------------------------------------------------------------------------------

This is a quite known issue with the OpenAI Whisper speech recognition model. 

The behavior is sometimes triggered by bad audio quality during that segment (background noise, mic issues, people talking over each other). However, sometimes this seems to happen even with good audio quality. 

Unfortunately, there is nothing we can do about this at the moment: you have to go through that particular audio segment and transcribe it manually.

Why do we use work directory `Work /scratch/work/user-name` instead of `Home Directory`?
------------------------------------------------------------------------------------------

`Home Directory` has a small disk space quota (10Gb) and `scratch/work/` has a large one (200Gb). Workspace disk is also faster than the home directory.

What if my audio file contains speech in more than one language?
-----------------------------------------------------------------

If a single audio file contains speech in more than one language, result files will (probably) still be produced but the results will (probably) be nonsensical to some extent. 

In some cases, this can be avoided easily. For example, if the language changes at the middle of the audio, just split the file into two parts and process them separately. You can use any available audio software to do this, for example, `Audacity <https://www.audacityteam.org/>`.

What happens if I submit speech2text audio file(s) that have already been processed and completed?
--------------------------------------------------------------------------------------------------

This is safe to do: speech2text checks if the expected result files already exist and if so, exits early without doing any further processing.

I submitted my audio files with wrong language. What to do?
----------------------------------------------------------

Wait until the processing is finished, delete the `results` folder, and submit the job again with the correct language.
