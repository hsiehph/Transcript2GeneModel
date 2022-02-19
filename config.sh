unset PYTHONPATH
# unsetting your current running env is important
conda deactivate
module purge
. /etc/profile.d/modules.sh
module load modules modules-init modules-gs/prod modules-eichler
module load picard/2.26.4
module load minimap2/2.24
module load samtools/1.9
module load bedtools/2.29.2
