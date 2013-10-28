intent of this tutorial (2-stage WORM pattern):

The script launcher_from_local_machine.py .py is to be run on the local host. It transfers all the files mentioned in the artifacts except itself to Sierra.   At sierra the file_breaker_result_holder_at_sierra.py is launched and it breaks the Data file (Data.txt) which contains 10000 numbers into 2 files, Data_part_1.txt, Data_part_2.txt.   2 jobs are launched , first one is launched to be executed at india that sorts Data_part_1.txt and returns  back to to the /tmp directory of Sierra the 1st part of the input, Sorted_Data1.txt .    The second job is a local job launched at sierra itself,  the sorts the file Data_part_2.txt and returns the file Sorted_Data2.txt.  Finally both the output files, Sorted_Data1.txt and Sorted_Data2.txt are staged to the /tmp directory of Sierra's login node.

Artifacts:  (place them all in the home directory of the local host)

Data.txt     (Datafile with 10,000 numbers which is to be broken into 2 files at Sierra,  Data_part_1 is sorted at Sierra and the Data_part_2 is sent to india to be sorted )
insertion_sort.py  (Simple python script that implements the insertion sort algorithm. First Sent to     			       Sierra and then to India via the Saga Job Api)
insertion_sort_sierra.py ( Almost same as above, except for a small changes to make it run locally
                                        at Sierra.  This is not sent to India)

execute_at_sierra.sh  : (shell scripts to run the file_breaker_result_holder_at_sierra.py  on sierra)  
launcher_from_local_machine.py
file_breaker_result_holder_at_sierra.py  (controlling script that runs on sierra launches the jobs on sierra and india and brings back the sorted data and stores them on /tmp diretory of sierra's login node)

Before you decide to run the tutorial note that:
1. Make sure you have access to the future grid machines. (your ssh public key must be added to the known list on Futuregrid.)
2. I am using the the Saga-python 0.9.12 version
3. Create a virtual environment sierra_tut on Sierra
virtualenv $HOME/sierra_tut
source $HOME/sierra_tut/bin/activate
      pip install saga-python
Open the .bashrc file on Sierra and add the following lines :
module load python/2.7

source $HOME/din_env/bin/activate
** (we are creating a virtual environment make sure that it is automatically activated when we log in to the node.)
4. Repeat step 3 for India as well


Instructions to run the tutorial:

1. keep all the artifacts in the home directory
2. Make sure u create a directory sort_related in home directory of each, India, Sierra and Alamo.
3. virtualenv $HOME/tutorial

4. source $HOME/tutorial/bin/activate
5. pip install saga-python
6. python launcher_from_local_machine.py

Output: 

Sorted_Data1.txt and Sorted_Data2.txt  are staged to /tmp
 directory of Sierra's login node. 
