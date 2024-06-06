Whisper
==========

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

.. highlight:: console

This uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

There are two variants of Whisper available. The "standard" Whisper uses 
whisper-ctranslate2, which is a CLI for faster-whisper, a reimplementation 
of OpenAI's Whisper using Ctranslate2. Original repository for this 
project can be found 
`here <https://github.com/Softcatala/whisper-ctranslate2>`__.

The second variant is whisper-diarization, which is a fork of faster-whisper 
with support for speaker detection (diarization). 
Original repository for this project can be found 
`here <https://github.com/MahmoudAshraf97/whisper-diarization>`__.

Of these two, whisper-diarization runs noticable slower and has less versatile 
options. Using base Whisper is recommended if speaker detection is not necessary.

Usage (Whisper)
-------------------

This example shows you a sample script to run Whisper.

.. code-block:: console

    $ module load whisper
    $ srun --mem=4G singularity_wrapper run your_audio_file.wav --model_directory $medium_en --local_files_only True --language en

Option ``--model_directory $medium_en`` Tells whisper to use a local model, in 
this case the model ``medium.en`` with the path to the model given through 
the environment variable ``$medium_en``. For list of all local models, you can 
run ``echo $model_names`` as long as the module is loaded. (These models are pre-downloaded by us and the variables
are defined when the module is loaded.)
You can also give it 
a path to your own model if you have one. The other imporant option here is 
``--local_file_only True``. This stops Whisper from checking 
if there are newer versions of the model online. The option ``--language LANG`` 
is not necessary, but whisper's language detection is sometimes weird. 

If you are transcribing language different 
from English, use a general model e.g. ``$medium``. If your source 
audio is in English, using English-specific models is usually a 
performance gain.

For full list of options, run:

.. code-block:: console

   $ singularity_wrapper run --help

Notes on general Slurm resources: 

  - For memory, requesting roughly 4G for medium model or smaller, 
    and 8G for large should be sufficient. 
    
  - When running on CPU, requesting additional CPUs should give a 
    performance increase until 8 CPUS. Whisper doesn't scale properly 
    beyond 8 CPUS, and will actually run slower in most cases.

Running on GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~

Singularity-wrapper takes care of making GPUs available for the container, 
so all you need to do to run Whisper on a GPU is use the previous 
command and add additional flag: ``--device cuda``. 
Without this, Whisper will only run on a CPU even if a GPU is available. Remember to :doc:`request a GPU </triton/tut/gpu>` in the Slurm job.

Usage (Whisper-diarization)
------------------------------------

This example shows you a sample script to run whisper-diarization.

.. code-block:: console

    $ module load whisper-diarization
    $ srun --mem=6G singularity_wrapper run -a your_audio_file.wav --whisper-model $medium_en

Option ``--whisper-model $medium_en`` Tells whisper which model to use, in this case 
``medium.en``. If you use environment variables that come with the module to specify the 
model, whisper will run using a local model. Otherwise it will download the model to 
your home directory. For list of all local models, run ``echo $model_names`` with 
whisper-diarization loaded.

Note that syntax is unfortunately somewhat different compared to plain whisper. You 
need to specify the audio file to use with the argument ``-a audio_file.wav`` and 
similarily the syntax to specificy the model is different.

For full list of options, run:

.. code-block:: console

   $ singularity_wrapper run --help

Notes on general Slurm resources:

  - Whisper-diarization requires slightly more memory than plain Whisper. 
    Requesting roughly 6G for medium model or smaller, 
    and 12G for large should be sufficient.
    
  - When running on CPU, requesting additional CPUs should give a
    performance increase until 8 CPUS. Whisper doesn't scale properly
    beyond 8 CPUS, and will actually run slower in most cases.


Running on GPU
~~~~~~~~~~~~~~~~~~~~~~~~

Compared to plain Whisper, running whisper-diarization on GPU takes little 
more work. Singularity-wrapper still takes care of making GPUs available 
for the container and you still specify you want to use GPU using the flag 
``--device cuda``. 

Unfortunately whisper-diarization requires multiple models when using a GPU
, and there isn't a practical way to use local models for this. For this 
reason, you should create a symlink from whisper's cache folder in your 
home, to your work directory. This way you avoid filling your home 
directory's quota.

To do this, run following commands:

.. code-block:: console
    
    $ mkdir -p ~/.cache/huggingface/ ~/.cache/torch/NeMo temp_cache/huggingface/ temp_cache/NeMo/ $WRKDIR/whisper_cache/huggingface $WRKDIR/whisper_cache/NeMo
    $ mv ~/.cache/huggingface/* temp_cache/huggingface/
    $ mv ~/.cache/torch/NeMo/* temp_cache/NeMo/
    $ rmdir ~/.cache/huggingface/ ~/.cache/torch/NeMo
    $ ln -s $WRKDIR/whisper_cache/huggingface ~/.cache/
    $ ln -s $WRKDIR/whisper_cache/NeMo ~/.cache/torch/
    $ mv temp_cache/huggingface/* ~/.cache/huggingface/
    $ mv temp_cache/NeMo/* ~/.cache/torch/NeMo
    $ rmdir temp_cache/huggingface temp_cache/NeMo temp_cache
    

This bunch of commands first creates cache folders if they don't exist 
and moves any existing files to temp directory, Next it creates symlinks 
to your work directory in place of original cache directories, and moves 
all previous files back. This way all downloaded files exist on your work 
instead of eating your home quota. 


Converting audio files
-------------------------------

Whisper should automatically convert your audio file to a correct 
format when you run it. In the case this does not work, you 
can convert it on Triton using ``ffmpeg`` with following commands:

.. code-block:: console
    
    $ module load ffmpeg
    $ ffmpeg -i input_file.audio output.wav

If you want to extract audio from a video, you can instead do: 

.. code-block:: console
    
    $ module load ffmpeg
    $ ffmpeg -i input_file.video -map 0:a output.wav

