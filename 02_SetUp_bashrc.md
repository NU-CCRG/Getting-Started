# Setting up your .bashrc environment on QUEST

Your .bashrc "environment" does many things, but here we'll discuss how it determines what software is available to you. However, we must first discuss software usage on QUEST:

To use software on QUEST, we take advantage of the [module libraries](https://kb.northwestern.edu/quest-software):
* To see what software is available on QUEST: `module avail`
* To see what software is currently loaded in your environment: `module list`
* To load new software" `module load <software_name>`
* To remove software from your environment: `module unload <software_name>`

Many software packages on QUEST have different versions. You can either load the default verison (D) by typing in the base name of a software packge, or load a specific version by typings its full name. `module load matlab` vs. `module load matlab/2013b`

During active QUEST sessions, you can load and unload software as needed. However, there will likley be bits of software that you use repeatedly. These can be autoloaded upon login, if you set up your .bashrc environmnet to do so. 

On QUEST, your "environment" is determined by the .bashrc file in your home directory. Files that begin with a period "." are hidden. To see them use the following command: `ls -a`

In my environment I autoload the software I use on a regular basis, as well as set up some key stroke and path navigation shortcuts.





Below you'll see a .bashrc that loads [NCO](http://nco.sourceforge.net), [NCVIEW](http://meteora.ucsd.edu/~pierce/ncview_home_page.html), [NCL](https://www.ncl.ucar.edu), and [Netdcf](https://www.unidata.ucar.edu/software/netcdf/docs/). The `module use` command indicates that some software is not available to all QUEST users, but is instead only on the b1045 project space. 

```
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

module use /projects/b1045/modules
module load nco
module load ncview
module load ncl/6.4.0
module load netCDF/4.3.3.1

```

This is just the beginning of .bashrc modification. You can learn additional features [here](http://www.linuxfromscratch.org/blfs/view/7.8/postlfs/profile.html). 
