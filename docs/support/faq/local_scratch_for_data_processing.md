# Why Interactive batch jobs are good for processing large numbers of small files?
                   
An interactive batch job Puhti allows you to have a Puhti session that can have up to:
*   4 cores
*   64 GB of memory
*   7 days of run time
*   640 GB of fast local scratch disk

To launch an interactive session in Puhti, execute command:
```text
sinteractive -i
```
One of the useful features of interactive batch jobs is the *fast local scratch area*. The “normal” Lustre based project specific directories, *scratch* and *projappl*, can store large amounts of data and make it accessible to all the nodes of Puhti. However these directories are not good for managing a large number of files. 

Generally you should avoid work flows that require creating thousands of small files. If you anyhow need to work with a huge number of files, 
you should consider using the NVME based local temporary scratch directories, either through normal or interactive batch jobs.
The local scratch area is visible only for the specific batch job and it is erased when the batch job ends. 
Because of that you always first need to import your data set to the local scratch and when you finish, copy the data you want to preserve back to some more 
permanent storage place like scratch or Allas.

To demonstrate the effectivity of local scratch area let’s study a sample directory called *big_data*. The directory contains about 100 GiB of data in 120 000 files. In the beginning the data is peaked one data tar-archive file in the scratch directory of project 2001234 (/scratch/project_2001234/big_data.tar)

First we launch an interactive batch job with 2 cores, 4 GB of memory and 250 GB of fast temporary scratch disk.
```text
interactive -c 2 -m 4G -d 250
```
The analysis is then done in three steps:
*Step 1*. Move to the local scratch area using environment variable $LOCAL_SCRATCH and open the tar package to the fast local disk.
```
cd $LOCAL_SCRATCH
tar xvf /scratch/project_2001234/big_data.tar ./
```

*Step 2*. Run the analysis. This time we run a for loop that uses command "transeq" to translate all the fasta files, found in the big_data directory, 
into new protein sequence files:
```text
for ffile in $(find ./ | grep fasta$ )
do
     transeq $ffile ${ffile}.pep
done 
```
In this example about 52000 fasta files where found so after the processing the big_data directory contains 52000 more small files. 
The actual translation is a simple task so relatively much time is consumed to just open and close files.

*Step 3*. When the processing is finished we store the results back to scratch directory into a new tar file to the normal scratch directory
```text
tar cvf /scratch/project_2001234/big_data.pep.tar ./
```
Now the results are in safe in one file in scratch directory and we can exit from the interactive session.

We could do the same analysis procedure in the scratch directory too.  Below is execution time comparison for running the three steps 
above in LOCAL_SCRATCH and in normal scratch.  The response times of LOCAL_SCRATCH are be rather stable, but in the scratch directory 
the execution times will vary much, due to changes in the total load of the Lustre file system.

|                               | LOCAL_SCRATCH |         scratch|
|-------------------------------|---------------|----------------|    
|Step 1. Opening tar file       | 2m 8s         |   4m 12s       |
|Step 2. Analysis               | 9m 42s        |   21m 58s      |
|Step 3. Creating new tar file  | 2m 25s        |   42m 21s      | 
|Total                          | 14m 15s       |   1h 8m 31s  |

More detailed information about batch job specific local storages:
[https://docs.csc.fi/computing/disk/](https://docs.csc.fi/computing/disk/)                 
 
