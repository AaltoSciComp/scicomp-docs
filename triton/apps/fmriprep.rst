FMRIprep
~~~~~~~~

::

    module load singularity-fmriprep

fmriprep is installed as a singularity container. By default it will always run the current latest version. If you need a version that is not currently installed on triton, please open an issue at https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues

To run fmriprep for one subject, without free-surfer reconall, using ica-aroma


::

    singularity_wrapper exec fmriprep <path-to-bids> <your-scratch-folder> participant --participant-label 01 --use-aroma --fs-no-reconall --fs-license-file /scratch/shareddata/set1/freesurfer/license.txt


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
