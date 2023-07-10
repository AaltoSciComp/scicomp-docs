Whisper
==========

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

This example shows you a sample script to run Whisper.::

    module load whisper
    srun --mem=4G singularity_wrapper run your_audio_file.wav --model_directory $medium_en --local_files_only True --language en

Option ``--model_directory $medium_en`` Tells whisper to use a local model, in 
this case the model ``medium.en`` with the path to the model given through 
the environment variable ``$medium_en``. For list of all local models, you can 
run ``echo $model_names`` as long as the module is loaded. You can also give it 
a path to your own model if you have one. The other imporant option here is 
``--local_file_only True``. This stops Whisper from checking 
if there are newer versions of the model online. The option ``--language <lang>`` 
is not necessary, but whisper's language detection is sometimes weird. 

If you are transcribing language different 
from English, use a general model e.g. ``$medium``. If your source 
audio is in English, using English-specific models is usually a 
performance gain.

For full list of options, run: ::

   singularity_wrapper run --help

Running on GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~

Singularity-wrapper takes care of making GPUs available for the container, 
so all you need to do to run Whisper on a GPU is use the previous 
command and add additional flag: ``--device cuda``. 
Without this, Whisper will only run on a CPU even if a GPU is availabe.

Usage (Whisper-diarization)
------------------------------------

This example shows you a sample script to run whisper-diarization.::

    module load whisper_diarization
    srun --mem=6G singularity_wrapper run -a your_audio_file.wav --whisper-model $medium_en

Option ``--whisper-model $medium_en`` Tells whisper which model to use, in this case 
``medium.en``. If you use environment variables that come with the module to specify the 
model, whisper will run using a local model. Otherwise it will download the model to 
your home directory. For list of all local models, run ``echo $model_names`` with 
whisper-diarization loaded.

Note that syntax is unfortunately somewhat different compared to plain whisper. You 
need to specify the audio file to use with the argument ``-a audio_file.wav`` and 
similarily the syntax to specificy the model is different.

For full list of options, run: ::

   singularity_wrapper run --help

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

.. code-block:: bash
    
    mkdir -p ~/.cache/huggingface/
    mkdir -p ~/.cache/torch/
    rm -rf ~/.cache/huggingface/hub
    rm -rf ~/.cache/torch/NeMo
    mkdir -p $WRKDIR/whisper_cache/hub
    mkdir $WRKDIR/whisper_cache/NeMo
    ln -s $WRKDIR/whisper_cache/hub ~/.cache/huggingface/hub
    ln -s $WRKDIR/whisper_cache/NeMo ~/.cache/torch/NeMo
    

This bunch of commands first creates cache folders if they don't exist, 
then removes any existing ones and replaces them with symlinks to your 
work directory. This way all downloaded files exist on your work 
instead of home. 

Note that if you have downloaded other models from 
huggingface they might get deleted as well. In this case you might 
want to check ``.cache/huggingface/hub`` and move any relevant files 
elsewhere.


Converting audio files
-------------------------------

Whisper should automatically convert your audio file to a correct 
format when you run it. In the case this does not work, you 
can convert it on Triton using ``ffmpeg`` with following commands::
    
    $ module load ffmpeg
    $ ffmpeg -i input_file.audio output.wav

If you want to extract audio from a video, you can instead do: 

.. code-block:: bash
    
    module load ffmpeg
    ffmpeg -i input_file.video -map 0:a output.wav

