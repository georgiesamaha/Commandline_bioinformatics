#!/usr/bin/python

  # Reformat feline chromosome nomenclature to numerical format for use in PLINK 
  # PLINK requires autosome input in numerical format, this python script changes format of VCF from A1,A2,A3... to 1,2,3 and outputs as new file. 
  # Run as felineplink.py <input.vcf> <output.vcf>
  # Run from directory containing VCF, will output new vcf in same location
    
import sys 

VCF = open(sys.argv[1], "r")
VCFPLINK = open(sys.argv[2], "w+")

for i, line in enumerate(VCF, 0):
		VCF_info=(line.split("\t")) 
		chr_id=VCF_info[0]
		if  line.startswith('#'):
                        hash_line = line[0:]
                        VCFPLINK.write(hash_line)
		if chr_id=='A1':
			VCFPLINK.write(line.replace('A1','1', 1))
		elif chr_id=='A2':
			VCFPLINK.write(line.replace('A2','2', 1))
		elif chr_id=='A3':
			VCFPLINK.write(line.replace('A3','3', 1))
		elif chr_id=='B1':
			VCFPLINK.write(line.replace('B1','4', 1))
		elif chr_id=='B2':
			VCFPLINK.write(line.replace('B2','5', 1))
		elif chr_id=='B3':
			VCFPLINK.write(line.replace('B3','6', 1))
		elif chr_id=='B4':
			VCFPLINK.write(line.replace('B4','7', 1))
		elif chr_id=='C1':
			VCFPLINK.write(line.replace('C1','8', 1))
		elif chr_id=='C2':
			VCFPLINK.write(line.replace('C2','9', 1))
		elif chr_id=='D1':
			VCFPLINK.write(line.replace('D1','10', 1))
		elif chr_id=='D2':
			VCFPLINK.write(line.replace('D2','11', 1))
		elif chr_id=='D3':
			VCFPLINK.write(line.replace('D3','12', 1))
		elif chr_id=='D4':
			VCFPLINK.write(line.replace('D4','13', 1))
		elif chr_id=='E1':
			VCFPLINK.write(line.replace('E1','14', 1))
		elif chr_id=='E2':
			VCFPLINK.write(line.replace('E2','15', 1))
		elif chr_id=='E3':
			VCFPLINK.write(line.replace('E3','16', 1))
		elif chr_id=='F1':
			VCFPLINK.write(line.replace('F1','17', 1))
		elif chr_id=='F2':
			VCFPLINK.write(line.replace('F2','18', 1))
		elif chr_id=='X':
			VCFPLINK.write(line.replace('X','19', 1))
VCFPLINK.close()
