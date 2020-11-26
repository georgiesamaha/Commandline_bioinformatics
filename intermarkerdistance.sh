#!/bin/bash 

# calculates intermarker distance and maximum distance for a list of snps.
# input is bim format, for vcf change $4 to $2 in awk  
# where C= chr/contig, P=previous marker position, M= max distance, T= total length, N= number variants, L=current distance
# run as intermarkerdistance.sh <filename>
# output as chr/marker_count/avg_intermarker_dist/maximum_dist per chromosome

function input(){
for chr in {1..18};
	do
	
	awk -v chr=$chr '$1==chr {print}' $@ | awk 'BEGIN{C="";P=-1;M=0;T=0.0;N=0;} /^#/{next} {if(C==$1) {L=int($4)-P;T+=L;N++;M=(M>L?M:L);}C=$1;P=int($4);}END{if(N>0) printf(C" count=%d avg=%f max=%d\n",N,T/N,M);}'

done;
}

input $@
