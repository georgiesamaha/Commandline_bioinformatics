#!/bin/bash 

# Calculates average read depth of a bam using samtools and prints to screen

samtools depth -a final.bam  |  awk '{sum+=$3; sumsq+=$3*$3} END { print "Average = ",sum/NR; print "Stdev = ",sqrt(sumsq/NR - (sum/NR)**2)}'
