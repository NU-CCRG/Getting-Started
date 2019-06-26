Contents:

* [Introduction to QUEST use](#introduction-to-quest-use)
* [Connecting to QUEST outside Northwestern network](#connecting-to-quest-outside-northwestern-network)
* [.bashrc environment set up](https://github.com/NU-CCRG/Getting-Started/blob/master/02_SetUp_bashrc.md)
* [vi text editor](#vi-text-editor)
* [Conda Environments](#conda-environments)
* [Jupyter Notebook](Jupyter_Use_Guide/01_jupyter_setup.md)
* [Transfering Files to/from QUEST](#transfer-files)
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

In general, we store intellectual creations (scripts we create) in our home directories and data in the b1045 project space. Home directory content should be backed up to your NU BOX folder. A script to do so can be found [here](https://github.com/NU-CCRG/python_intro/blob/master/03_BackUp_Scripts.md).  

### Helpful commands on HPCs

* list the contents of the directory you are in (see all the files within the folder):

    `ls` 

* See what file/directory was most recently modified with the current directory:

    `ls -ltr`
 
* Make a file executable (able to be run):

    `chmod +x <name>.py`

* Run a python script:

    `python <name>.py`

* See your command history:
    `history`
    
* To autocomplete names of files...begin typing them and then strike the **Tab** key

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

# Connecting to QUEST outside Northwestern network

If you are connecting to QUEST from outside the Nortwestern Network, you might need to setup a VPN connection. Northwestern Knowledgebase has a good step-by-step [tutorial](https://www.it.northwestern.edu/oncampus/vpn/) on this:

* [Setting up VPN on a Windows computer](https://kb.northwestern.edu/62248)
* [Setting up VPN on a macOS computer](https://kb.northwestern.edu/62249)

# .bashrc environment set up 

* Learn how to use software on QUEST [here](https://github.com/NU-CCRG/Getting-Started/blob/master/02_SetUp_bashrc.md)

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

2. Create conda environment. You can choose any environment name you want, simply replace `<my-env>` with any name you wish.

    `conda create -n <my-env> python=3.6 anaconda`
    
    If you are prompted to proceed (y/n), type `y` and press Enter.

3. Load in environment.

    `source activate <my-env>`
    
    To see the list of environments you have: `conda env list`

4. Load in libraries to your environment. Make sure you’ve activated your environment before you begin loading.

    `conda install -c conda-forge <library>`

    * For the exercises, here are the suggested libraries:

    `conda install -c conda-forge netCDF4 xarray cartopy ipykernel nc-time-axis`
    
    If you are prompted to proceed (y/n), type `y` and press Enter.

Now you have the conda environment setup. 

### Starting python in your environment

1. Load in python into QUEST

    `module load python/anaconda3`

2. Load in environment. To see the list of environments you have: `conda env list`

    `source activate <my-env>`

3. Start an active python session.

    You can choose to have your python session within the command line, in which case just type:

    `python`
    
    Or you can use the interactive Jupyter notebook interface.

# Jupyter Notebooks

* Learn about jupuyter notebooks [here](https://github.com/NU-CCRG/Getting-Started/tree/master/Jupyter_Use_Guide)

# Transfer Files

* Moving files onto and off of QUEST can be done in a myriad of ways that you can read about [here](https://kb.northwestern.edu/quest-filetransfer). We reccommend downloading [Cyber Duck](https://cyberduck.io) as its "window-based" interface is likely to be familiar. 

# GIT on QUEST

To be continued ...
