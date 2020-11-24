#!/usr/bin/python

# This script checks SCRIPT.o1234_usage logs from Artemis PBS jobs
# Collects runtime info and prints as tab delimited summary

# Run script as pbs_usage_report.py <PREFIX FOR JOB LOG> from directory housing log files

import os
import sys

#Finds logs, if can't then print error
prefix=sys.argv[1]
suffix="usage"

path=os.getcwd() #defines current working directory

#collect usage files in a list and collect relevant fields
output=open("pbs_summary_output.txt", "w+")
output.write("job_name\texit_status\twalltime_requested\twalltime_used\tCPUs_requested\tCPUs_used\tCPUs_time\tCPU_%\tmem_requested\tmem_used\tmem_%\n")

for file in os.listdir(path):
	if file.startswith(prefix) and file.endswith(suffix):
		#print(file)
		fileopen=open(file)
		for i, line in enumerate(fileopen, 0):
			if line.startswith("Job Name"):
				jobstrip=(line.strip("\n"))
				job_name=(jobstrip.split(": "))
				#output.write(job_name[1])
			if line.startswith("Exit Status"):
				exitstrip=(line.strip("\n"))
				exit_info=(exitstrip.split(":"))
				#output.write(exit_info[1])
			if line.startswith("Walltime"):
				wall_req=(line.split(" "))
				#output.write(wall_req[4])
			if line.startswith("Walltime"):
				wallstrip=(line.strip("\n"))
				wall_used=(wallstrip.split(" "))
				#output.write(wall_used[15])
			if line.startswith("    Cpus"):
				cpu_req=(line.split(": "))
				#output.write(cpu_req[1])
			if line.startswith("    Cpus"):
				cpu_usedstrip=(line.strip("\n"))
				cpu_used=(cpu_usedstrip.split(": "))
				#output.write(cpu_used[3])
			if line.startswith("          Cpu Time"):
				cputime=(line.split(": "))
				#output.write(cputime[1])
			if line.startswith("          Cpu"):
				cpu_percentstrip=(line.strip("\n"))
				cpupercent=(cpu_percentstrip.split(": "))
				#output.write(cpupercent[3])
			if line.startswith("     Mem requested"):
				mem_reqstrip=(line.strip("\n"))
				mem_req=(mem_reqstrip.split(": "))
				#output.write(mem_req[1])
			if line.startswith("     Mem requested"):
				mem_reqstrip=(line.strip("\n"))
				mem_used=(mem_reqstrip.split(": "))
				#output.write(mem_used[3])
			if line.startswith("                               :        Mem percent"):
				mem_percentstrip=(line.strip("\n"))
				mem_percent=(mem_percentstrip.split(": "))
				#print(mem_percent[2])

				output.write(job_name[1]+'\t'+exit_info[1]+'\t'+wall_req[4]+'\t'+wall_used[15]+'\t'+cpu_req[1]+'\t'+cpu_used[3]+'\t'+cputime[1]+'\t'+cpupercent[3]+'\t'+mem_req[1]+'\t'+mem_used[3]+'\t'+mem_percent[2]+'\n')

output.close()
