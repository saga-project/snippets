#this script copies a file from the localhost to india

import os
import sys
import saga
import time 

REMOTE_HOST_1 = "india.futuregrid.org"
REMOTE_HOST_2 = "sierra.futuregrid.org"
REMOTE_HOST_3 = "alamo.futuregrid.org"
def main():
    try:
	ctx = saga.Context("ssh")
	ctx.user_id = "dino24"
	
        sessionx = saga.Session()
	sessionx.add_context(ctx)
	
	
	# list that holds the jobs
        jobs = []

        # create a working directory in /scratch
        dirname_x = '%s/%s/sort_related/' % ("sftp://dino24@sierra.futuregrid.org/", '/N/u/dino24/')
        workdir_x = saga.filesystem.Directory(dirname_x, saga.filesystem.CREATE,
                                            session=sessionx)

                  
                                            
        # copy the data,executable and warpper script to the remote host
        going_to_india_wrapper = saga.filesystem.File('file://localhost/%s/file_breaker_result_holder_at_sierra.py' % os.getcwd())
        going_to_india_wrapper.copy(workdir_x.get_url())
        
        wrapper2 = saga.filesystem.File('file://localhost/%s/insertion_sort.py' % os.getcwd())
        wrapper2.copy(workdir_x.get_url()) 

        wrapper3 = saga.filesystem.File('file://localhost/%s/insertion_sort_sierra.py' % os.getcwd())
        wrapper3.copy(workdir_x.get_url())         
        
        
        wrapper = saga.filesystem.File('file://localhost/%s/execute_at_sierra.sh' % os.getcwd())
        wrapper.copy(workdir_x.get_url()) 
        wrapper1 = saga.filesystem.File('file://localhost/%s/Data.txt' % os.getcwd())
        wrapper1.copy(workdir_x.get_url())     
        # the saga job services connects to and provides a handle
        # to a remote machine. In this case, it's your machine.
        # fork can be replaced with ssh here:
        jobservice_x = saga.job.Service("pbs+ssh://%s" % REMOTE_HOST_2, session=sessionx)
        
  	# describe our job
        jd_x = saga.job.Description()
       # outputfile='data_x.txt'

        # Next, we describe the job we want to run. A complete set of job
        # description attributes can be found in the API documentation.
        
       # jd.environment     = {'MYOUTPUT':'"Hello from SAGA"'}
        jd_x.total_cpu_count =1
        jd_x.wall_time_limit = 10     
        jd_x.working_directory = workdir_x.get_url().path
        jd_x.executable      = 'sh'
        jd_x.arguments       = ['execute_at_sierra.sh']
        jd_x.output          = "mysagajob1.stdout"
        jd_x.error           = "mysagajob1.stderr"

        # Create a new job from the job description. The initial state of
        # the job is 'New'.
	job_x = jobservice_x.create_job(jd_x)


		
	
	
        # Check our job's id and state
        print "Job ID    : %s" % (job_x.id)
        print "Job State : %s" % (job_x.state)

        print "\n...starting job...\n"
  
        # Now we can start our job.
        job_x.run()
        print "Job ID    : %s" % (job_x.id)
        print "Job State : %s" % (job_x.state)        
 
        print "\n...waiting for job...\n"
        # wait for the job to either finish or fail
        job_x.wait()
        print "Job State : %s" % (job_x.state)
        print "Exitcode  : %s" % (job_x.exit_code)        
   

    except saga.SagaException, ex:
        # Catch all saga exceptions
        print "An exception occured: (%s) %s " % (ex.type, (str(ex)))
        # Trace back the exception. That can be helpful for debugging.
        print " \n*** Backtrace:\n %s" % ex.traceback
        return -1


if __name__ == "__main__":
    sys.exit(main())
