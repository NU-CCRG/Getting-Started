# How to Back Up your scripts

In the world of HPC bad stuff happens. User error or machine failure can result in the loss of the scripts you created. To prevent this, back up your intellectual creations, i.e., scripts. 

Scripts are files you create to analyze data. This includes everything that is not reproducable. I.e., this does not include Earth System Model (ESM) code or data, or publicly available data downloads. ESM model code can be re-downloaded. Model simulations can be re-run. Model data and observations can be re-downloaded.  

CCRG members back up their scripts in their personal NU Box folder using a version of the below shell script. This script is run from your machine's command line, i.e., it is not run from QUEST. Here's what it does:

* Within your NU Box Sync folder it creates a new directory named after today's date (so you know when the back up occurred)
* Saves only the files you tell it to, using wildcards(*). 
* File types will vary among users, but commonly backed up scripts include .ncl, .m. .sh, .r, and .py files
* Be careful not to back up large code repositories like ESM code, as there is lots of suffix overlap 
  * To prevent this, use a well thought out PATH structure in the shell script

To create a back up shell script on your machine, open a <filename.sh> using **vi** and enter your desired commands. Once the .bashrc is complete, make your script executable using `chmod +x <filename>.sh` and then execute `./<filename>.sh` Depending on the number of files you need to save, it may take some time. 

```
#!/bin/sh

cd ~/Desktop/Box\ Sync/QUEST/    
bkdir=`date +"%Y-%m-%d"`

mkdir $bkdir

cd $bkdir

rsync -e ssh -a --include='*.Rdat' --include='*.ncl' --include='*.R*' --include='*.txt' --include='*.m' --include='*.sh' --include='*/' <netid>@quest.northwestern.edu:/home/<netid>/PROJECTS/ .

# get rid of empty directories in structure
find . -type d -empty -delete
```


