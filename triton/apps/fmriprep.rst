FMRIprep
~~~~~~~~

::

    module load singularity-fmriprep/latest  # stick to the latest!

fmriprep is installed as a singularity container. By default it will always run the current latest version. If you need a version that is not currently installed on triton, please open an issue at https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues

Here an example to run fmriprep for one subject, using an interactive session, without free-surfer reconall, using ica-aroma. The raw data in BIDS format are in the path ``<path-to-bids>``, then you can create a folder for the derivatives that is different than the BIDS folder ``<path-to-your-derivatives-folder>``. Also create a temporary folder under your scratch/work folders for storing temporary files ``<path-to-your-scratch-temporary-folder>`` for example ``/scratch/work/USERNAME/tmp/``. The content of this folder is removed after fmriprep has finished.


::

    # Example running in an interactive session
    ssh triton.aalto.fi
    sinteractive --time=24:00:00 --mem=20G # you might need more memory or time depending on the size
    module load singularity-fmriprep/latest
    singularity_wrapper exec fmriprep <path-to-bids> <path-to-your-derivatives-folder> -w <path-to-your-scratch-temporary-folder> participant --participant-label 01 --use-aroma --fs-no-reconall --fs-license-file /scratch/shareddata/set1/freesurfer/license.txt


This might give the exit error *"OSError: handle is closed"*, this is a python thing, see https://neurostars.org/t/fmriprep-error-oserror-handle-is-closed/4030. The general rule is that if the reports are generated, then everything is done with the preprocessing.

If you want to parallelyze things you can write a script that cycles through each subject labels and queues SBATCH jobs for each subject (it can be an array job or a series of serial jobs). It is important you tune your memory and time requirements before processing many subjects at once.

===============
POST-processing
===============

Fmriprep does the minimal preprocessing. There is no smoothing, no temporal filtering and in general you need to regress out the estimated confounds. The most simple way is:


::

    module load fsl
    fsl_regfilt -i $inputniifile -d "$file_with_bold_confounds.tsv" -o $outputniifile -f 1,2,3,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31



There are also tools for post-processing such as:
    - https://github.com/HBClab/NuisanceRegression
    - https://xcpengine.readthedocs.io/
    - https://fitlins.readthedocs.io/en/latest/
    - https://github.com/arielletambini/denoiser

These are not installed on the singularity image, hence you need to experiment with these on your own.
