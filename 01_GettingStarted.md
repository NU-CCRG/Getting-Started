Contents:

* [Introductory Linux Scripts to get around QUEST](#introductory-linux-scripts-to-get-around-quest)
* [Conda Environments](#conda-environments)
* [GIT on QUEST](#git-on-quest)
* [Jupyter Notebook](#jupyter-notebook)



# Introductory Linux Scripts to get around QUEST

Explanation in this font.

Actual code in `THIS FONT AND COLOR`.

Names of things are in \<brackets>\, which means it can be replaced with the name of your target, no need to include brackets.

### Log into QUEST

`ssh -X <netid>@quest.northwestern.edu` or `ssh -Y <netid>@quest.northwestern.edu`

You need [XQUARTZ](https://www.xquartz.org) (if you have a mac) or [FastX](https://kb.northwestern.edu/quest-fastx) (if you have Windows) to get images to display.

### Directories
“Directory” – essentially the name of a folder. You use a “path” to get to the directory – i.e. a list of folders to get to your place. For example, /projects/b1045/ is the directory to our group’s “workspace”.

* Get to our project space on QUEST:

    `cd /projects/b1045/`

* Get to your home directory (your “desktop”):

    `cd ~`

* Find your current directory:

    `pwd`

* Get to last directory

    `cd -`

### Lists

* list the contents of the directory (see all the files within the folder):

    `ls` 

* See what file/directory was most recently modified with the current directory:

    `ls -ltr`
 
### Open files

* Open the file:
 
    `vi <filename>`

* to exit vi – :

    `:q!` (if you dont want to add changes,) 

    `:wq` (if you want to write a new file)

    `:q` (if you just opened the file and did nothing)

* to modify the file:

    `i` 

* to get out of writing: hit **Esc** button

**Note: vi also has tricks, like searching for keywords or line numbers, so look that up!**

* Running file to make executable:

`chmod +x <name>.py`

* Run a python script:

`python <name>.py`

* hit **ctrl-c** to cancel your accidental runs

### Copy files

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



# Conda Environments

### Make a Conda environment

1. Load in python into QUEST

    `module load python/anaconda3`

2. Create conda environment, change <>

    `conda create -n <my-env> python=3.6 anaconda`

3. Load in environment. Once environment is set up, every time you log into quest put source activate <env>.

    `source activate <my-env>`

4. Load in libraries to your environment. Make sure you’ve activated your environment before you begin loading.

    `conda install <library>`

    * For the exercises, here are the suggested libraries:

    `conda install -c conda-forge netCDF4 xarray cartopy ipykernel nc-time-axis`

5. Get into environment

    `module load python/anaconda3`
    `source activate <my-env>`

6. Start an active python session

    `python`

# GIT on QUEST

To be continued ...


# Jupyter Notebook

https://kb.northwestern.edu/running-jupyter-notebook-on-quest

* Log into quest and do the following steps.

Reminder: 

Explanation in this font. Actual code in `THIS FONT AND COLOR`.

Names of things are in \<brackets\>, which means it can be replaced with the name of your target, do NOT include brackets

### Setting up Jupyter notebook

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

 `ssh -L <8622>:localhost:<8622> i <netid>@quest.northwestern.edu ssh -N -L <8622>:localhost:<8622> <qnode6026>`

8. Go to first terminal window, copy and paste the given webpage into your internet browser (i.e. Chrome).

