# Setting up your .bashrc environmnet on QUEST

Your .bashrc "environment" does many things, but here we'll discuss how it determines what software is available to you. However, we must first discuss software usage on QUEST:

To use software on QUEST, we take advantage of the module library:
* To see what software is available on QUEST: `module avail`
* To see what software is currently loaded in your environment: `module list`
* To load new software" `module load <software_name>`
* To remove software from your environment: `module unload <software_name>`

Many software packages on QUEST have different versions. You can either load the default verison (D) by typing in the base name of a software packge, or load a specific version by typings its full name. `module load matlab` vs. `module load matlab/2013b`

During active QUEST sessions, you can load and unload software as needed. However, there will likley be bits of software that you use repeatedly. These can be autoloaded upon login, if you set up your .bashrc environmnet to do so. 

On QUEST, your "environment" is determined by the .bashrc file in your home directory. Files that begin with a period "." are hidden. To see them use the following command: `ls -a`

In my environment I autoload the software I use on a regular basis, as well as set up some key stroke and path navigation shortcuts.





Here's what my .bashrc looks like: 
```
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

module use /projects/b1045/modules
module load ncview
module load ncl/6.4.0
module load netCDF/4.3.3.1
module load nco

# 
export GREP_OPTIONS='--color=auto'
export PS1="[\d\t]\u@W$ "
export TMPDIR=/projects/b1045/tmp/

# User specific aliases and functions
alias rm='rm -f'
alias cp='cp -f'
alias mv='mv -f'
#alias q='qstat -a'
alias q='squeue'
alias ll='ls -lrt'
#alias Q='showq -w acct=b1045'
alias Q='squeue -A b1045'
#alias cd='set old=$cwd ; chdir \!*'
alias back='set oldb = $cwd ; chdir $old ; set old = $oldb ; pwd'
alias b='back'
alias num='ls -l ./ | wc -l'
alias ls='ls --color=force'
#alias ll='ls -l --color=force'
alias l.='ls -d .[a-zA-Z]* --color=force'
alias la='ls -a --color=force'
alias pro='cd /projects/b1045/'
alias 343='cd /projects/e30741/'
