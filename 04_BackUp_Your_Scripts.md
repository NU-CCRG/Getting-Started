# How to Back Up your scripts

In the world of HPC bad stuff happens. User error or machine failure can result in the loss of the scripts you created. To prevent this, back up your intellectual creations, i.e., scripts. 

Scripts are files you create to analyze data. This includes everything that is not reproducable. I.e., this does not include Earth System Model (ESM) code or data, or publicly available data downloads. ESM model code can be re-downloaded. Model simulations can be re-run. Model data and observations can be re-downloaded.  

CCRG members back up their scripts in their personal NU Box folder using a version of the below shell script. This script is run from your machine's command line, i.e., it is not run from QUEST. Here's what it does:

* Within your NU Box Sync folder it creates a new directory named after today's date (so you know when the back up occurred)
* Saves only the files you tell it to, using wildcards(*). 
* File types will vary among users, but commonly backed up scripts include .ncl, .m. .sh, .R, and .py files
* Be careful not to back up large code repositories like ESM code, as there is lots of suffix overlap 
  * To prevent this, use a well thought out PATH structure in the shell script

To create a back up shell script on your machine, open a <filename.sh> using **vi** and enter your desired commands. See how to use vi [here](https://github.com/NU-CCRG/Getting-Started/blob/master/01_Using%20QUEST.md#vi-text-editor). Once the .bashrc is complete, make your script executable using `chmod +x <filename>.sh` and then execute from the command line `./<filename>.sh`. Depending on the number of files you need to save, it may take some time. 

```
#!/bin/sh

# Move into the location you want to keep your backup files, e.g., your NU Box folder
cd ~/Desktop/Box\ Sync/QUEST/   

# Choose a name for the folder where you'll store your BU files, e.g., today's date
bkdir=`date +"%Y-%m-%d"`

# Make the directory
mkdir $bkdir

# Move into the directory
cd $bkdir

# Set the files types to BU (using wildcards (*) and suffix or whatever you like), as well as the PATH to their location on QUEST
# The 'rsync' command will copy these files to the NU Box dolder you created
# Because you are ssh-ing into QUEST, this code will ask for your password

rsync -e ssh -a --include='*.py' --include='*.ncl' --include='*.R*' --include='*.txt' --include='*.m' --include='*.sh' --include='*/' <netid>@quest.northwestern.edu:/home/<netid>/Scripts/ .

# Get rid of empty directories in structure
find . -type d -empty -delete
```


