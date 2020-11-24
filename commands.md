# Helpful one-line commands, etc. for bioinformatics
Commands and resources for filtering and processing FASTQ, FASTA, BAM, VCF, BED, GTF etc files. 
Also contains some useful bashrc aliases. 

### print lines containing the number 5 from a file 
    grep -n 5 file.txt 
    
### sort file numberically on first column 
    sort -g -k 1 file.txt 
    
### extract string in file2 from a list in file 1 
    grep -fwF file1.txt file2.txt

### find most frequent string in a column (-f1)
    cut –f1 file.txt | sort | uniq -c | sort -k1nr | head
    
### count number of reads in a FASTQ 
    cat in.fq | echo $((`wc -l`/4))
    
### extract reads from FASTQ according to read name 
    zcat in.fastq.gz | awk 'BEGIN{RS="@";FS="\n"}; $1~/name/{print $2; exit}'
 
### extract all lines on a chr (A1) between two bp locations from a VCF
    zcat in.vcf.gz | awk '$1=="A1"' | awk '$3>=100000' | awk '$3<=150000'
 
### reverse compliment a sequence 
    echo 'ACTG' | rev | tr 'ACTG' 'TGAC'
 
### add to FASTA header 
    paste <(cat info.txt) <(cat in.fasta | paste - - | cut -c2-) | awk '{printf(">%s_%s\n%s\n",$1,$2,$3);}'
 
### find where reads with coverage >5 from BAM file 
    bedtools genomecov -bg -ibam in.bam | awk '$4>=5'
 
### print location of reads with coverage >5 from bam file 
    bedtools genomecov -bg -ibam test.bam | awk '$4>=5' | bedtools coverage -a stdin -b in.bam
 
### VCF > BED  (sorted and merged)
    zcat in.vcf.gz awk '{ if (!/^#/) print $1"\t"$2"      \t"$2+1}' | sort -k1,1 -k2,2n | bedtools merge -i stdin
 
### VCF > BED with awk/sed 
    zcat in.vcf.gz | sed -e 's/chr//' | awk '{OFS="\t"; if (!/^#/){print $1,$2-1,$2,$4"/"$5,"+"}}'
    
### make consensus fasta from a VCF 
    bcftools consensus –IHA –f ref.fasta in.vcf > consensus.fasta 
 
### sort VCF with header 
    zcat in.vcf.gz | awk '$0~"^#" { print $0; next } { print $0 | "sort -k1,1V -k2,2n" }'
 
### get sample IDs from VCF
    zcat in.vcf.gz | grep "^#CHROM" | tr '\t' '\n' | grep -v -E '#CHROM|POS|ID|REF|ALT|QUAL|FILTER|INFO|FORMAT'
 
 

## useful aliases for bashrc 

### change directory 
    alias ..='cd ..' 
    alias ...='cd ../..'
    alias directory_name='cd /path/to/directory_name'
    
### fix regular typos I make 
    alias la="ls" 
    alias mc="mv -i" 
    
### ask permission before action 
    alias mv="mv -i"
    alias cp="cp -i"  
    alias rm="rm -i"

### shortcuts for regularly used directories/files 
    alias ref="/path/to/reference/fasta.fasta"

### shortcut for opening a bam in tview aligned to reference 
    alias tvsample1='samtools tview /path/to/sample1.final.bam /path/to/reference.fasta'
  
### refresh bashrc
    alias refresh="source ~/.bashrc"
