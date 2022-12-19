FMRIprep
~~~~~~~~

**December 2022**: Note that the previous module we had installed (fmriprep 20.2.0) has been FLAGGED by the developers. Please specify a different version, for example with ``module load singularity-fmriprep/22.1.0``.

::

    module load singularity-fmriprep 

fmriprep is installed as a singularity container. By default it will always run the current latest version. If you need a version that is not currently installed on triton, please open an issue at https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues

Here an example to run fmriprep for one subject, using an interactive session, without free-surfer reconall, using ica-aroma, and with co-registration to the 2mm isotropic MNI template space (MNI152NLin6Asym, FSL bounding box of 91x109x91 voxels). The raw data in BIDS format are in the path ``<path-to-bids>``, then you can create a folder for the derivatives that is different than the BIDS folder ``<path-to-your-derivatives-folder>``. Also create a temporary folder under your scratch/work folders for storing temporary files ``<path-to-your-scratch-temporary-folder>`` for example ``/scratch/work/USERNAME/tmp/``. The content of this folder is removed after fmriprep has finished.


::

    # Example running in an interactive session, this can be at maximum 24 hours
    # You might want to use a tool such as "screen" or "tmux" 
    ssh triton.aalto.fi
    # start screen or tmux
    sinteractive --time=24:00:00 --mem=20G # you might need more or less memory or time depending on the size
    module load singularity-fmriprep
    singularity_wrapper exec fmriprep <path-to-bids> <path-to-your-derivatives-folder> -w <path-to-your-scratch-temporary-folder-for-this-participant> participant --participant-label 01 --output-spaces MNI152NLin6Asym:res-2 --use-aroma --fs-no-reconall --fs-license-file /scratch/shareddata/set1/freesurfer/license.txt


If you want to parallelyze things you can write a script that cycles through each subject labels and queues SBATCH jobs for each subject (it can be an array job or a series of serial jobs). It is important you tune your memory and time requirements before processing many subjects at once. It is important to create a dedicated temporary scratch folder for each subject

===============
POST-processing
===============

Fmriprep does the minimal preprocessing. There is no smoothing, no temporal filtering and in general you need to regress out the estimated confounds. They can be regressed before further analysis (e.g. functional connectivity, intersubject correlation), or they can be included as part of a general linear model The most simple way is then to decide which columns of the "confounds.tsv" matrix you want to use as confounds and use NIlearn image_clean https://nilearn.github.io/dev/modules/generated/nilearn.image.clean_img.html
 



There are also tools for post-processing such as:
    - https://github.com/HBClab/NuisanceRegression
    - https://xcpengine.readthedocs.io/
    - https://fitlins.readthedocs.io/en/latest/
    - https://github.com/arielletambini/denoiser

These are not installed on the singularity image, hence you need to experiment with these on your own.
