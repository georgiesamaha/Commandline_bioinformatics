#!/bin/python/3.8.2

################################################################################################
#
# Platform: Artemis HPC, University of Sydney
# Description: finds and replaces sequence ids in a header of fasta file
# with genus and family ids
# Usage: python find_replace.py <taxa.txt> <in.fasta> <out.fasta>
# Details: this script matches sequence ids from fasta and taxa files and
# replaces sequence ids in fasta headers with corresponding family and genus
# ids from the taxa file
#
# Taxa file format: 651103371       k_Bacteria; p_Firmicutes; c_Bacilli; o_Bacillales; f_Bacillaceae; g_Bacillus; s_Bacillus thuringiensis sv. chinensis CT-43
#
# Author: Georgina Samaha
# georgina.samaha@sydney.edu.au
# Date last modified: 11/03/2021
#
# If you use this script towards a publication, please acknowledge the
# Sydney Informatics Hub (or co-authorship, where appropriate).
#
# Suggested acknowledgement:
# The authors acknowledge the scientific and technical assistance
# <or e.g. bioinformatics assistance of <PERSON>> of Sydney Informatics
# Hub and resources and services from the University of Sydney High
# Performance Computing Cluster, Artemis.
#
##################################################################################################

import sys

replace_ids = {} # creates empty dictionary ready for strings to replace and what to replace them with

with open(sys.argv[1], "r") as taxa, open("replace_ids.txt", "w+") as replace_file:
        for line in taxa: #loops over the lines in taxa_file
                if not line.strip():    #skips over the empty lines
                        continue
                else:
                        clean_line=line.replace("; ", "\t") #make one delim type
                        split_line=clean_line.split("\t")
                        sequence_id=(split_line[0])
                        family_genus=(split_line[6]+"_"+split_line[7])
                        replace_file.write(sequence_id+"\t"+family_genus+"\n")

with open("replace_ids.txt", "r") as replace_file:
        for line in replace_file:
                ids = line.strip().split("\t") #defines file delimiter as tab
                sequence_id = ids[0] #reads first column as sequence_id
                family_genus_id = ids[1]
                replace_ids[sequence_id] = family_genus_id #add both to dictionary

with open(sys.argv[2], "r") as fasta_file: #reading fasta file
        content = fasta_file.readlines() #reads lines of the fasta into a list
        new_content = [] #keeps a list of the lines with replaced strings

        for line in content:
                new_line = line
                for sequence_id, family_genus_id in replace_ids.items():
                        new_line = new_line.replace(sequence_id, family_genus_id)
                new_content.append(new_line)

# Write replaced content to a new file called "outfile.txt"
with open(sys.argv[3], "w") as outfile:
        for line in new_content:
                outfile.write(line)
