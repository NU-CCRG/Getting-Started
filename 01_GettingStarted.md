Contents:

* [Introduction to QUEST use](#introduction-to-quest-use)
* [vi text editor](#vi-text-editor)
* [Conda Environments](#conda-environments)
* [Jupyter Notebook](#jupyter-notebook)
* [GIT on QUEST](#git-on-quest)


# Introduction to QUEST use

Explanation in this font.

Actual code in `THIS FONT AND COLOR`.

Names of things are in \<brackets>\, which means it can be replaced with the name of your target, no need to include brackets.

QUEST is Northwestern's High Perfomance Computing (HPC) cluster. This is where the CCRG runs all its simulations and analyzes data. You can read all about QUEST [here](https://www.it.northwestern.edu/research/user-services/quest/). 

### Logging into QUEST

`ssh -X <netid>@quest.northwestern.edu` or `ssh -Y <netid>@quest.northwestern.edu`

The -X and -Y here in the above commands allow you to view image files (e.g., .pdf, .eps, netcdf, etc.) from the command line. To take advantage of this you will need to download and install [XQUARTZ](https://www.xquartz.org) (if you have a mac) or [FastX](https://kb.northwestern.edu/quest-fastx) (if you have Windows). After downloading and installing these files, you will need to begin a new session on QUEST to enable viewing capabilities. 

### Organizational structure on QUEST 
QUEST (and other HPC) machines organize their files within "directories," which are essentially folders. You can navigate to folders or particular files in directories using the "path" aka address. For example, /projects/b1045/ is the path to the CCRG “storage space”, while /home/<netid>/ is your home directory.

* Find your current directory:

    `pwd`
    
* Get to your home directory (your “desktop”):

    `cd ~`
    
* Get to the CCRG project space:

    `cd /projects/b1045/`

* Go to last visited directory

    `cd -`

In general, we store intellectual creations (scripts we create) in our home directories and data in the b1045 project space. Home directory content should be backed up to your NU BOX folder. A script to do so can be found [here]().  

### Helpful commands on HPCs

* list the contents of the directory you are in (see all the files within the folder):

    `ls` 

* See what file/directory was most recently modified with the current directory:

    `ls -ltr`
 
* Make a file executable (able to be run):

`chmod +x <name>.py`

* Run a python script:

`python <name>.py`

* hit **ctrl-c** to cancel your accidental runs

### Copying files

* Copy file from one directory to another:

    `cp /dir/to/file/<file.txt> /dir/to/newdir/<rename.txt>` 

* make backup copy:

    `cp /dir/to/file/<file.txt> /dir/to/file/<file.txt.bak>` 

* move file or rename file (aka take it away from dir/to/file):

    `mv /dir/to/file/<file.txt> /dir/to/newdir/<rename.txt>`  

    (to rename keep original directory)

### Random

* use to downloads files from websites
`wget <url>`
* zip a file
`gzip <file>`
* unzip a file
`gunzip <file>`
* untar a file
`tar -xvf <file>`

There's loads more HPC commands. Google away!

# vi text editor

vi is a bit like a word processing program. With vi you can open pre-existing text files to read and/or modify, or you can create a new <filename.xx>. vi is a language unto itself, and it will require some effort to familiarize yourself with its key strokes. A graphic of shortcuts can be found [here](http://www.viemu.com/vi-vim-cheat-sheet.gif). If you have desk space, it would be good to print that cheat sheet out to place above your work station. However, here's so basics:  

* Open a pre-exiting or new file:
 
    `vi <filename>`

* to modify the file, enact "insert" mode:

    `i` 

* to get out of a mode (e.g., insert): hit the **Esc** button

* to exit vi – :

    `:q!` (if you dont want to add changes,) 

    `:wq` (if you want to write a new file)

    `:q` (if you just opened the file and did nothing)



# Conda Environments
Conda allows us to use Python on QUEST. Below you'll find instructions on how to set it up initially, as well as subsequent ussage. 

### Making a new Conda environment

1. Load in python into QUEST

    `module load python/anaconda3`

2. Create conda environment, change <>

    `conda create -n <my-env> python=3.6 anaconda`

3. Load in environment. Once environment is set up, every time you log into quest put `source activate <env>`.

    `source activate <my-env>`

4. Load in libraries to your environment. Make sure you’ve activated your environment before you begin loading.

    `conda install <library>`

    * For the exercises, here are the suggested libraries:

    `conda install -c conda-forge netCDF4 xarray cartopy ipykernel nc-time-axis`

5. Start an active python session

    `python`

### Starting python in your environment

1. Load in python into QUEST

    `module load python/anaconda3`

2. Load in environment. 

    `source activate <my-env>`

3. Start an active python session

    `python`


# Jupyter Notebook

https://kb.northwestern.edu/running-jupyter-notebook-on-quest

* Log into quest and do the following steps.

>Reminder: 
>
>Explanation in this font. Actual code in `THIS FONT AND COLOR`.
>
>Names of things are in \<brackets\>, which means it can be replaced with the name of your target, do NOT include brackets

### Setting up Jupyter notebook for the first time 

(if you have done this, skip to [Running Jupyter notebook](#running-jupyter-notebook))

1. Load python

    `module load python/anaconda3`

2. Activate environment (setup one if you dont have one yet, [see here](#conda-environments)

    `source activate <my-env>`

3. Install the environment within Jupyter

    `python -m ipykernel install --user --name <my-env> --display-name "my-env"`

4. Start a session:

    `srun -A b1045 -p b1045 -N 1 --tasks-per-node=1 --mem-per-cpu=4G --time=04:00:00 --pty bash -l`

5. Check session name:

    `hostname`

(remember this output, will look something like qnode6020)

6. Run jupyter notebook on quest:

    `jupyter notebook --port=<8622> --no-browser`

(port number can be any 4 digits, choose a random set of 4 digits)

7. **OPEN NEW TERMINAL WINDOW**. Log into your “tunnel” to the node so you can get to Jupyter notebook.

    `ssh -L <8622>:localhost:<8622> <netid>@quest.northwestern.edu ssh -N -L <8622>:localhost:<8622> <qnode6026>`

8. Go to first terminal window, copy and paste the given webpage into your internet browser (i.e. Chrome).

### Running Jupyter notebook 

1. Load python

    `module load python/anaconda3`

2. Activate environment (setup one if you dont have one yet, [see here](#conda-environments)

    `source activate <my-env>`

3. Start a session:

    `srun -A b1045 -p b1045 -N 1 --tasks-per-node=1 --mem-per-cpu=4G --time=04:00:00 --pty bash -l`

4. Check session name:
    `hostname`

    * (remember this output, will look something like qnode6020)

5. Run jupyter notebook on quest:

    `jupyter notebook --port=<8622> --no-browser`

    * (port number can be any 4 digits, choose a random set of 4 digits)

6. **OPEN NEW TERMINAL WINDOW**. Log into your “tunnel” to the node so you can get to Jupyter notebook.

    `ssh -L <8622>:localhost:<8622> i <netid>@quest.northwestern.edu ssh -N -L <8622>:localhost:<8622> <qnode6026>`

7. Go to first terminal window, copy and paste the given webpage into your internet browser (i.e. Chrome).

# GIT on QUEST

To be continued ...
