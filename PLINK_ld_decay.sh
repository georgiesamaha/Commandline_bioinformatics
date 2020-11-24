#!/bin/bash 

# Runs r2 calculations across SNP pairs binned across each autosome
# Calculates the average r2 value between SNP pairs on each autosome 
# Input files are PLINK format 
# Prints to output in format bin_size/chromosome/average_r2

io=/path/to/work/dir
temp=${io}/LD_chr.tmp
output=${io}/LD_chr.results

mkdir ${temp}

echo -e "KB\tchr\tavg_r2">>${output}

kb=(1 5 10 20 30 40 50 100 200 500 700 1000 1500 2000 2500 3000 3500 4000 5000) #bin size 
chr={1..18}

for c in ${chr[@]};
	do

	for i in ${kb[@]};
		do

      plink --allow-no-sex --bfile ${cohort} \
            --maf 0.1 \
            --geno 0.1 \
            --r2 \
            --chr $c \
            --ld-window-kb ${i} \
            --ld-window-r2 0 \
            --ld-window 99999\
            --out ${temp}/cheetah.LD.${c}.${i}kb

		avg_r2=$(awk '{ total += $7; count++ } END { print total/count }' ${temp}/out.LD.${c}.${i}kb.ld)

		echo -e "${i}\t${c}\t${avg_r2}">>${output}

	done

done
