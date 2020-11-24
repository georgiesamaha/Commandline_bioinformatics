#!/usr/bin/python 

# Takes SNPs from VCF and creates L and R flanking sequence of 200bp for each 
# Run as python flanks.py <in.vcf> <in.fasta>
# Prints output to flanks.txt
import sys 

# open vcf and output file
vcf = open(sys.argv[1],"r")
flanksout = open("flanks.txt", "w+")

# open fasta file
fasta =open(sys.argv[2],"r")
sequence=fasta.read()
sequence_concat=sequence.replace('\n','')

# define by how many bases the variant should be flanked
flanksize = 200

#loop for collecting first 10 SNPs
for i, line in enumerate(vcf, 1): 
	if i>29 and i<40: 
		data=(line.split("\t")) 
		snp_pos=int(data[1]) 
		new_snp_pos=snp_pos-1 
		ref_al=data[3] 
		alt_al=data[4] 

		left=sequence_concat[new_snp_pos-flanksize:new_snp_pos] 

		right=sequence_concat[new_snp_pos+1:new_snp_pos+flanksize+1] 
 
		flanksout.write(">SNPPOS_"+str(snp_pos)+"\t"+left+"["+ref_al+"/"+alt_al+"]"+right+"\n")

fasta.close()
vcf.close()
flanksout.close()
