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

2. Activate environment (setup one if you dont have one yet, [see here](https://github.com/NU-CCRG/Getting-Started/blob/master/01_Using%20QUEST.md#conda-environments)

    `source activate <my-env>`
    
    To see the list of environments you have: `conda env list` 

3. Install the environment within Jupyter

    `python -m ipykernel install --user --name <my-env> --display-name "my-env"`

4. Start a session:

    `srun -A b1045 -p b1045 -N 1 --tasks-per-node=1 --mem-per-cpu=4G --time=04:00:00 --pty bash -l`

5. Check session name:

    `hostname`

(remember this output, will look something like qnode6020)

6. Run jupyter notebook on quest:

    `jupyter notebook --port=<8622> --no-browser`
    
    * (port number can be any 4 or 5 digits from 0000 to 65535. If the port is already in use, try another set of digits.)

(port number can be any 4 digits, choose a random set of 4 digits)

7. **OPEN NEW TERMINAL WINDOW**. Log into your “tunnel” to the node so you can get to Jupyter notebook.

    `ssh -L <8622>:localhost:<8622> <netid>@quest.northwestern.edu ssh -N -L <8622>:localhost:<8622> <qnode6026>`

8. Go to first terminal window, copy and paste the given webpage into your internet browser (i.e. Chrome).

### Running Jupyter notebook 

1. Load python

    `module load python/anaconda3`

2. Activate environment (setup one if you dont have one yet, [see here](#conda-environments) )

    `source activate <my-env>`
    
    To see the list of environments you have: `conda env list`

3. Start a session:

    `srun -A b1045 -p b1045 -N 1 --tasks-per-node=1 --mem-per-cpu=4G --time=04:00:00 --pty bash -l`

4. Check session name:
    `hostname`

    * (remember this output, will look something like qnode6020)

5. Run jupyter notebook on quest:

    `jupyter notebook --port=<8622> --no-browser`

    * (port number can be any 4 or 5 digits from 0000 to 65535. If the port is already in use, try another set of digits.)

6. **OPEN NEW TERMINAL WINDOW**. Log into your “tunnel” to the node so you can get to Jupyter notebook.

    `ssh -L <8622>:localhost:<8622> <netid>@quest.northwestern.edu ssh -N -L <8622>:localhost:<8622> <qnode6026>`
    
    Note that there are FOUR instances of the port number in the command above. Make sure to replace them all, and remove the brackets.

7. Go to first terminal window, copy and paste the given webpage into your internet browser (e.g. Chrome).
