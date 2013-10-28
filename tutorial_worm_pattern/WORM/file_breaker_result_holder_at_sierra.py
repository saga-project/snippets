import os
import sys
import saga
import time 

import getopt
import random  # for generating random numbers
#import time    # for timing each sort function with time.clock()
from decimal import *


def data_reader(filename):
    data_list_char =[];
    data_list_int_1=[]; # list to store first part of input file
   # data_list_int_2=[]; # list to store second part of input file
    data_list_int_3=[]; # list to store third part of input file
    data_list_char = open(filename, 'r').read().split(" ")
    list_length =len(data_list_char)
    print(list_length);
    r=0;
    list_counter=0;
    for info in data_list_char:
        k=int(info);
        #print(k);(list_length/3)
        if list_counter<=(list_length/2):
          data_list_int_1.append(k);
          list_counter=list_counter+1;
          
        #CONVERTING 3 file break to 2 file break
        #elif (( (list_counter>(list_length/3)) or(list_counter==(list_length/3)))  and (list_counter<((list_length*2)/3) ) ):
        #   data_list_int_2.append(k);
        #   #print(list_counter) #test probe
        #   list_counter=list_counter+1;
         
        else:
           data_list_int_3.append(k);      
           list_counter=list_counter+1
           
        #print(data_list_int_1,"  ",data_list_int_2,"   ",data_list_int_3) #test probe
          

    return (data_list_int_1,data_list_int_3);

def output_writer(filename,data_set,N):
    fptr1=   open('Data_part_1.txt', "w");
 #   fptr2=   open('Data_part_2.txt', "w")   
    fptr3=   open('Data_part_2.txt', "w")
    count=0;
    for i in data_set[0]:
        fptr1.write(str(i));
        if(count==(N-1)):
            break;
        fptr1.write(" ");
        count=count+1;
        
    count=0;
   # for i in data_set[1]:
   #     fptr2.write(str(i));
   #     if(count==(N-1)):
   #         break;
   #     fptr2.write(" ");
   #     count=count+1;
        
    count=0;
    for i in data_set[1]:
        fptr3.write(str(i));
        if(count==(N-1)):
            break;
        fptr3.write(" ");
        count=count+1;






REMOTE_HOST_1 = "india.futuregrid.org"
REMOTE_HOST_2 = "sierra.futuregrid.org"
REMOTE_HOST_3 = "alamo.futuregrid.org"
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
    print(inputfile);      
    data_set=data_reader(inputfile);
    no_of_elements=len(data_set[0]);  # no of elements in one of the file  (total/2)
   #sorted_data_ins_sort=insertion_sort(data_set);
    output_writer(outputfile,data_set,no_of_elements)    
    try:
        ctx = saga.Context("ssh")
        ctx.user_id = "dino24"
        
        session1 = saga.Session()
        session1.add_context(ctx)
        
        session2 = saga.Session()
        session2.add_context(ctx)       

       # session3 = saga.Session()
       # session3.add_context(ctx)
        
        # list that holds the jobs
        jobs = []

        # create a working directory in /scratch
        dirname_1 = '%s/%s/sort_related/' % ("sftp://dino24@india.futuregrid.org/", '/N/u/dino24/')
        workdir_1 = saga.filesystem.Directory(dirname_1, saga.filesystem.CREATE,
                                            session=session1)

        dirname_2 = '%s/%s/sort_related/' % ("sftp://dino24@sierra.futuregrid.org/", '/N/u/dino24/')
        workdir_2 = saga.filesystem.Directory(dirname_2, saga.filesystem.CREATE,
                                            session=session2)      
                                            
      #  dirname_3 = '%s/%s/sort_related/' % ("sftp://dino24@alamo.futuregrid.org/", '/N/u/dino24/')
      #  workdir_3 = saga.filesystem.Directory(dirname_3, saga.filesystem.CREATE,
               #                             session=session3)      
                                                                                        
                                            
        # copy the data,executable and warpper script to the remote host

        sort_exe = saga.filesystem.File('file://localhost/%s/insertion_sort.py' % os.getcwd())
        sort_exe.copy(workdir_1.get_url())
        sort_datafile1= saga.filesystem.File('file://localhost/%s/Data_part_1.txt' % os.getcwd())
        sort_datafile1.copy(workdir_1.get_url())

#        sort_sierra_exe = saga.filesystem.File('file://localhost/%s/insertion_sort_sierra.py' % os.getcwd())
#        sort_sierra_exe.copy(workdir_2.get_url())
#        sort_datafile2=saga.filesystem.File('file://localhost/%s/Data_part_2.txt' % os.getcwd())
#        sort_datafile2.copy(workdir_2.get_url())

    #    sort_alamo_wrapper = saga.filesystem.File('file://localhost/%s/scatter_alamo.sh' % os.getcwd())
    #    sort_alamo_wrapper.copy(workdir_3.get_url())
    #    sort_alamo_exe = saga.filesystem.File('file://localhost/%s/insertion_sort.py' % os.getcwd())
    #    sort_alamo_exe.copy(workdir_3.get_url())        
    #    sort_alamo_datafile3=saga.filesystem.File('file://localhost/%s/Data_part_3.txt' % os.getcwd())
    #    sort_alamo_datafile3.copy(workdir_3.get_url())

        # the saga job services connects to and provides a handle
        # to a remote machine. In this case, it's your machine.
        # fork can be replaced with ssh here:
        jobservice_1 = saga.job.Service("pbs+ssh://%s" % REMOTE_HOST_1, session=session1)
        
        jobservice_2 = saga.job.Service("pbs+ssh://%s" % REMOTE_HOST_2, session=session2)
        
    #    jobservice_3 = saga.job.Service("pbs+ssh://%s" % REMOTE_HOST_3, session=session3)
             
        # describe our job
        jd_1 = saga.job.Description()
        outputfile='Sorted_Data1.txt'

        # Next, we describe the job we want to run. A complete set of job
        # description attributes can be found in the API documentation.
        
       # jd.environment     = {'MYOUTPUT':'"Hello from SAGA"'}
        jd_1.total_cpu_count =1
        jd_1.wall_time_limit = 10
        jd_1.working_directory = workdir_1.get_url().path
        jd_1.executable      = 'python'
        jd_1.arguments       = ['insertion_sort.py']
        jd_1.output          = "mysagajob.stdout"
        jd_1.error           = "mysagajob.stderr"

        # Create a new job from the job description. The initial state of
        # the job is 'New'.
        job_1 = jobservice_1.create_job(jd_1)

# describe our job
        jd_2 = saga.job.Description()
        outputfile='Sorted_Data2.txt'

        # Next, we describe the job we want to run. A complete set of job
        # description attributes can be found in the API documentation.
        
       # jd.environment     = {'MYOUTPUT':'"Hello from SAGA"'}
        jd_2.total_cpu_count =1
        jd_2.wall_time_limit = 10
        jd_2.working_directory = workdir_2.get_url().path
        jd_2.executable      = 'python'
        jd_2.arguments       = ['insertion_sort_sierra.py']
        jd_2.output          = "mysagajob.stdout"
        jd_2.error           = "mysagajob.stderr"

        # Create a new job from the job description. The initial state of
        # the job is 'New'.
        job_2 = jobservice_2.create_job(jd_2)   

     
        job_1.run();
        job_2.run();    
        print "\n...waiting for job...\n"
        # wait for the job to either finish or fail
        job_1.wait()
        job_2.wait()
       
        print "Job State : %s" % (job_1.state)
        print "Exitcode  : %s" % (job_1.exit_code)
        print "Job State : %s" % (job_2.state)
        print "Exitcode  : %s" % (job_2.exit_code)
        

        
        outfilesource = 'sftp://dino24@india.futuregrid.org/N/u/dino24/sort_related/Sorted_Data1.txt' #sftp://
        outfiletarget = 'file://localhost/tmp/'
        out = saga.filesystem.File(outfilesource, session=session1)
        out.copy(outfiletarget)
         
        print "Staged out %s to %s (size: %s bytes)" % (outfilesource, outfiletarget, out.get_size())
        
        outfilesource2 = 'sftp://dino24@sierra.futuregrid.org/N/u/dino24/sort_related/Sorted_Data2.txt' #sftp://
        outfiletarget2 = 'file://localhost/tmp/'
        out2 = saga.filesystem.File(outfilesource2, session=session2)
        out2.copy(outfiletarget2)
         
        print "Staged out %s to %s (size: %s bytes)" % (outfilesource2, outfiletarget2, out2.get_size())


        
    except saga.SagaException, ex:
        # Catch all saga exceptions
        print "An exception occured: (%s) %s " % (ex.type, (str(ex)))
        # Trace back the exception. That can be helpful for debugging.
        print " \n*** Backtrace:\n %s" % ex.traceback
        return -1


if __name__ == "__main__":
    main(sys.argv[1:])

