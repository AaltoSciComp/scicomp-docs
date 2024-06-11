FMRIprep
~~~~~~~~

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

This page describe how to use fmriprep on Triton.

::

    module load apptainer-fmriprep 

fmriprep is installed as an Apptainer container. By default it will always run the newest version installed on triton. If you need a version that is not currently installed on triton, please open an issue at https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues


=============
How to run it
=============

Here an example to run fmriprep for four subject, using an array. The raw data in BIDS format are in the path ``<path-to-bids>``, then you can create a folder for the derivatives that is different than the BIDS folder ``<path-to-your-derivatives-folder>``. Also create a temporary folder under your scratch/work folders for storing temporary files ``<path-to-your-scratch-temporary-folder>`` for example ``/scratch/work/USERNAME/tmp/``. The content of this folder should be removed after fmriprep has finished.

In the example below we prepared a list of subjects from the bids folder structure. E.g.

::

    sub-01
    sub-02
    sub-03
    ...



Here the array script. Note the large amount of memory even though it does not require much on average. ICA-AROMA is not part of fmriprep/23 anymore. You need to use fmriprep/22. In the example below we do not use freesurfer so no-recon-all is set.

::

    #!/bin/bash
    #SBATCH --time=2-00:00:00
    #SBATCH --mem-per-cpu=50G
    #SBATCH --array=1-4 # here one can change
    #SBATCH --output=logs/fmriprep_%A_%a.out
    #SBATCH --cpus-per-task=2

    n=$SLURM_ARRAY_TASK_ID
    iteration=`sed -n "${n} p" subjects_list.txt`     # Get n-th line (1-indexed) of the file

    mkdir -p /scratch/work/USERNAME/tmp/${iteration}
    echo ${iteration}

    module load apptainer-fmriprep/23.1.4
    
    apptainer_wrapper exec fmriprep <path-to-bids>  <path-to-derivatives-folder> -w /scratch/work/USERNAME/tmp/${iteration} participant --participant-label ${iteration} --n_cpus 2 --output-spaces MNI152NLin6Asym:res-2  --fd-spike-threshold 0.2 --fs-license-file /scratch/shareddata/set1/freesurfer/license.txt --write-graph --fs-no-reconall
    



It is important you tune your memory and time requirements before processing many subjects at once. It is important to create a dedicated temporary scratch folder for each subject. Do not use the option "--clean-workdir" if you are processing more than one subject at once.

===============
POST-processing
===============

Fmriprep does the minimal preprocessing. There is no smoothing, no temporal filtering and in general you need to regress out the estimated confounds. They can be regressed before further analysis (e.g. functional connectivity, intersubject correlation), or they can be included as part of a general linear model (it is always the best to have them as close as possible to the model if this is what you are doing). If you plan to regress the confoudns without being part of a general linear model, the most simple way is then to decide which columns of the "confounds.tsv" matrix you want to use as confounds and use NIlearn image_clean https://nilearn.github.io/dev/modules/generated/nilearn.image.clean_img.html 
 


There are also tools for post-processing such as:
    - https://github.com/HBClab/NuisanceRegression
    - https://xcpengine.readthedocs.io/
    - https://fitlins.readthedocs.io/en/latest/
    - https://github.com/arielletambini/denoiser

These are not installed on the singularity image, hence you need to experiment with these on your own.
