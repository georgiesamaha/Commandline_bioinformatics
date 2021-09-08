# Cheatsheet/shortcuts for HPCs

## Gadi 

### Checking job status 

Set permissions 
```
alias setfacl='setfacl -Rm u::rwX,g::rwX,o::-'
```

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
  
  ## Transfer rsync/sftp between Artemis and Gadi 
  
  ### From Gadi to RDS, submitted from Artemis 
  
To set up ssh-keys if you’ve never done it before:
	
`cd ~`   
`mkdir .ssh`  
`chmod 700 .ssh`   
`ssh-keygen`  
  
Just press enter when prompted, saving the key in ~/.ssh/id_rsa and enter for no passphrase 
	
`cd .ssh`   
You will now see two files, id_rsa (private key) and id_rsa.pub (your public key)   
Run `chmod 700 id_rsa*` to set permissions   
You will need to get contents of ~/.ssh/id_rsa.pub onto the remote server (i.e. RDS) in the file ~/.ssh/authorized_keys  
Normally with ssh access to a server it’s a lot easier (use ssh-copy-id command) but this won’t work because RDS uses sftp. So my workaround is:  

On local server, create the authorized_keys file that will go on RDS (be careful no to overwrite an existing authorized_keys file if you have one). To do this: 
`cat ~/.ssh/id_rsa.pub >> authorized_keys`    
`chmod 700 authorized_keys`   
	 
Now get that file on the local server. Sftp into Artemis RDS:    
`sftp <unikey>@research-data-ext.sydney.edu.au`   
`cd .ssh`   (mkdir .ssh if necessary)    
  
Put authorized_keys (this will transfer authorized_keys on Gadi to your current directory. With sftp, it will look for the file relative to where you launched sftp. You can check where you are on Gadi using lls)  

Logout using `ctrl+z` and test the sftp connection. You should not need to use a password  
