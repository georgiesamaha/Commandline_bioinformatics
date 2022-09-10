#!/usr/bin/python

  # Reformat numerical chromosome nomenclature to feline format 
  # PLINK requires autosome input in numerical format, this python script changes format of VCF from A1,A2,A3... to 1,2,3 and outputs as new file.

import sys

VCFPLINK = open(sys.argv[1], "r")
VCF = open(sys.argv[2], "w+")

for i, line in enumerate(VCFPLINK, 0):
                VCF_info=(line.split("\t"))
                chr_id=VCF_info[0]
                if  line.startswith('#'):
                        hash_line = line[0:]
                        VCF.write(hash_line)
                if chr_id=='1':
                        VCF.write(line.replace('1','A1', 1))
                elif chr_id=='2':
                        VCF.write(line.replace('2','A2', 1))
                elif chr_id=='3':
                        VCF.write(line.replace('3','A3', 1))
                elif chr_id=='4':
                        VCF.write(line.replace('4','B1', 1))
                elif chr_id=='5':
                        VCF.write(line.replace('5','B2', 1))
                elif chr_id=='6':
                        VCF.write(line.replace('6','B3', 1))
                elif chr_id=='7':
                        VCF.write(line.replace('7','B4', 1))
                elif chr_id=='8':
                        VCF.write(line.replace('8','C1', 1))
                elif chr_id=='9':
                        VCF.write(line.replace('9','C2', 1))
                elif chr_id=='10':
                        VCF.write(line.replace('10','D1', 1))
                elif chr_id=='11':
                        VCF.write(line.replace('11','D2', 1))
                elif chr_id=='12':
                        VCF.write(line.replace('12','D3', 1))
                elif chr_id=='13':
                        VCF.write(line.replace('13','D4', 1))
                elif chr_id=='14':
                        VCF.write(line.replace('14','E1', 1))
                elif chr_id=='15':
                        VCF.write(line.replace('15','E2', 1))
                elif chr_id=='16':
                        VCF.write(line.replace('16','E3', 1))
                elif chr_id=='17':
                        VCF.write(line.replace('17','F1', 1))
                elif chr_id=='18':
                        VCF.write(line.replace('18','F2', 1))
                elif chr_id=='19':
                        VCF.write(line.replace('19','X', 1))
VCFPLINK.close()
VCF.close()
