# Cheatsheet/shortcuts for HPCs

## Gadi 

### Checking job status 

To print verbose status of running jobs
```
qstat -u gs5517 -Esw 
```
To take a snapshot of the process status of all current processes in the running job 
```
qps <jobid>
```
To display [submission script/STDOUT/STDERR] of a running job
```
qcat [-s/-o/-e] <jobid>
```

To list contents in the folder $PBS_JOBFS 
```
qls <jobid>
```

To copy files and directories from the folder $PBS_JOBFS to the destination folder <dst>
```
qcp <jobid> <dst>
```

### Check stderr, stdout when a job is running 
Written to spool directory. Need to ssh into the node the job is running on, to get to the node. First:
```
qstat -n [jobid] 
ssh [node]
```
Then check:
```
/local/spool/pbs/spool
```

## Artemis 

### Check stderr, stdout when a job is running 
Written to spool directory. Need to ssh into the node the job is running on, to get to the node. First:
```
qstat -n [jobid] 
ssh [node]
```
Then check:
```
/var/spool/pbs/spool
```
