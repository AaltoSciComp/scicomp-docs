     .. admonition:: Important notes
     
       When using R it is often important to specify the R version used to run. There are multiple versions of R
       installed on triton. to get a list use::
       
         module spider r
         
       then load your preferred version using::
         
         module load r/version_of_your_choice
       
       In addition, when using libraries, you should install them manually before running your script, as R commonly
       requests user confirmation before installing packages from source, and thus can get stuck if the package is not
       already installed. That is run an interactive job ( ``sinteractive`` , load your selected R version and install 
       the package)::
       
         module load r/version_of_your_choice
         R
         > install.packages('packagename')
       
       This will guide you to selecting a download mirror and offer you the option to install the packages in your home directory.
       This normally works fine, but if you need to install a lot of packages, you might run out of home-folder quota. In this case
       move your package directory to your work directory and replace the R directory with a symlink that points to the new location
       of your R package directory::
       
         mv ~/R $WRKDIR/R
         ln -s $WRKDIR/R ~/R
