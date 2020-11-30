#!/bin/python/3.8.2 

# finds strings shared across three SNP lists 
# run as intersect_lists.py <list1> <list 2> <list3>  
# prints output to new file titled 'snp_overlap.txt' 
# to run on <3 or >3 lists add or remove list variables from script and command run

import sys 

list1=open(sys.argv[1])
list2=open(sys.argv[2])
list3=open(sys.argv[3])


overlap= list(set.intersection(*map(set, [list1, list2, list3])))
with open("snp_overlap.txt", "w+") as output:
	sys.stdout= output
	print(*overlap, file=output)

output.close()
