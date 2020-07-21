#!/bin/bash

#MPI_PROCS=2
#THREADS=12
#TIME=12:00:00
#OUTPUT_BASENAME="quop"
#SLURM_FILE_BASE="base.slurm"
#NAME="QuOp_MPI"

MPI_PROCS=$1
TIME=$2
OUTPUT_BASENAME=$3
SLURM_FILE_BASE=$4
NAME=$5

NODES=(1 2 3 4 5 6 7 8 9 10)

mkdir -p ${OUTPUT_BASENAME}/output

for NODE in ${NODES[@]}; do
    SCRIPT_PATHNAME=${OUTPUT_BASENAME}/${NODE}_${OUTPUT_BASENAME}.slurm
    TOTAL_MPI_PROCS=$(($NODE * $MPI_PROCS))
    cp $SLURM_FILE_BASE $SCRIPT_PATHNAME
	  sed -i "s/TIME_PLACEHOLDER/$TIME/g" $SCRIPT_PATHNAME
	  sed -i "s/OUTPUT_PLACEHOLDER/output\/${NODE}_${OUTPUT_BASENAME}.out/g" $SCRIPT_PATHNAME
	  sed -i "s/NODES_PLACEHOLDER/$NODE/g" $SCRIPT_PATHNAME
	  sed -i "s/MPI_PROCS_PLACEHOLDER/$TOTAL_MPI_PROCS/g" $SCRIPT_PATHNAME
done
