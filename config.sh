unset PYTHONPATH
# unsetting your current running env is important
module purge
. /etc/profile.d/modules.sh
module load modules modules-init modules-gs/prod modules-eichler
module load picard/2.26.4
