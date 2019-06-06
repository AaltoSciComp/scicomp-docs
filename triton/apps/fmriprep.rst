fmriprep
~~~

::

    module load singularity-fmriprep

fmriprep is installed as a singularity container. By default it will always run the current latest version. If you need a version that is not currently installed on triton, please open an issue at https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues

To run fmriprep for one subject, without free-surfer reconall, using ica-aroma

::

singularity_wrapper exec fmriprep <path-to-bids> <your-scratch-folder> participant --participant-label 01 --use-aroma --fs-no-reconall --fs-license-file /scratch/shareddata/set1/freesurfer/license.txt
