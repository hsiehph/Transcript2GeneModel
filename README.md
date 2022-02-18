# Transcript2GeneModel
This is a simple snakemake pipeline to predict gene models from genomic DNA (FASTA sequences) using transcripts (i.e., this is a transcript-guided approach).

<b> Note, this pipeline will only work on the Eichler lab cluster due to dependencies </b>

First, you will need to clone this repo.

$ git clone 

The config.yaml must contain correct paths to the files for transcripts and FASTA sequences. </br>

To run this pipeline,

$ snakemake --drmaa " -V -cwd -w n -e ./log -o ./log {params.sge_opts} -S /bin/bash"  -j 20 -w 60 -s findORF.snake

The predict gene models are listed in the output BED file. </br>
  ./output/<b><i>haplotypeID</i></b>/<b><i>haplotypeID</i></b>.tsv.ORFs.final.cds.bam.bed

The predict peptide sequences are listed in the output pep file. </br>
  ./output/<b><i>haplotypeID</i></b>/<b><i>haplotypeID</i></b>.tsv.ORFs.final.pep
