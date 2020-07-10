In this assignment we will explore the Array of Things (AoT) dataset. In particular, we will explore the pre-processed reduced dataset in the folder `/projects/b1045/AoT/AoT_reduced_data_10m`

To help us explore the dataset, and learn `pandas` and a little bit of `cartopy` while exploring, let's try to answer the following questions.

1. How many types of sensors are available in the AoT? What are they?
2. How many nodes are there in the AoT? List all the node ids.
3. Do all stations have the same set of sensors?
4. What node is closest to where you live?
5. What sensors are available in that node?
6. What is the time period of the data availability of a sensor in that node?
7. Plot a time series of any available sensor in the node closest to you.
8. Plot the map of locations of 4 sensors.

This assignment is purposely open ended because you must handle the inherent craziness that come with really large datasets that we use -- and this means you gotta get creative. For this exercise in particular, you're dealing with a crazy csv. In your research, you will encounter many datasets that are really poorly and inefficiently organized, so part of the problem is learning figure out what's happening with the dataset and how you can make it meaningful for you.

You can see that the dataset is 1.5G (`ls -lh` in the command line). Will this file be too big to handle by python?

My suggestion?

(a) try to open the file in vim

(b) try to print out the header using the command line (`head -100 data.csv`) (this won't fail)

(c) try to load in the dataset into python


If these things are failing, you know it's too big. But you can learn some info through these failures that can hint you to your next move. So --

(a) Looks like the linux commands work on the data, so why not process the data using linux? To do this, look at the questions, and decide what would work best. Could you chop up the file into smaller more manageable pieces? Could you pull out only the air quality sensor data in hopes that it's smaller (from observations of printing out the header of the data you'll see that there is a lot of unnecessary information that you probably don't care about)? You'll have to google this problem, but that's your new friend.

(b) This is obviously a memory problem, so why not use our supercomputer? You could log into an interactive QUEST session (https://kb.northwestern.edu/page.php?id=69247) and ask for 3G of memory so that you have enough temporary memory to handle all the data and some more in case you duplicate info when processing, then try to load it into python again.

But also you could do something else that I haven't thought of. Are there more efficient ways? TBD ....
