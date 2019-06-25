# How to Back Up your scripts

In the world of HPC bad stuff happens. User error or machine failure can result in the loss of the scripts you created. To prevent this, back up your intellectual creations, i.e., script. 

Scripts are files you create to analyze data. This includes everything that is not reproducable. I.e., this does not include ESM model code or data, or publicly available data downloads. ESM model code can be re-downloaded. Model simulations can be re-run. Model data and observations can be re-downloaded.  

CCRG members back up their scripts in their personal NU Box folder using the below shell script:

'#!/bin/sh

# Create dir w/ today's date and move into it
# I create this dir in my 'Box Sync' folder b/c it is auto-backed up to the web
# I save my "intellectual" content only, i.e., just scripts I've written
# These are usually .ncl, .m, .sh, etc files
# I use wildcards to save these...but you need to be careful, you don't want to save an entire model's code.
# I direct the code into an area I call Projects, where I keep most of my scripts

cd ~/Desktop/Box\ Sync/QUEST/    
bkdir=`date +"%Y-%m-%d"`
mkdir $bkdir
cd $bkdir

# get the the *.ncl and *.sh files within the current structure
#rsync -e ssh -a --include='*.Rdat' --include='*.ncl' --include='*.R*' --include='*.txt' --include='*.m' --include='*.sh' --include='*/' deh224@quest.northwestern.edu:/home/deh224/PROJECTS/ .

rsync -avze ssh --include '*.ncl' --include='*.sh' --include='*.m' --include='*/' --exclude '*' deh224@quest.northwestern.edu:/home/deh224/PROJECTS/ .

# get rid of empty directories in structure
find . -type d -empty -delete


