#!/bin/bash -l
#PBS -N new
#PBS -l walltime=8:00:00
#PBS -l select=48:ncpus=1:mem=64gb:mpiprocs=1
#PBS -l place=group=cputype
# #PBS -m abe
#PBS -M studentnumber@qut.edu.au

JOU=/home/n11538554/cfd/qev4evo/v2.20.8.2/halfcar.jou
GEOM=/home/n11538554/cfd/qev4evo/v2.20.8.2/geom.agdb
MESH=/home/n11538554/cfd/qev4evo/v2.20.8.2/mesh.msh
FLUENT_VERSION=3ddp

CUR_DATE=$(date +%Y%m%d_%H%M%S)

nprocs=`wc -l $PBS_NODEFILE | awk '{ print $1 }'`
echo $nprocs

echo $PBS_NODEFILE
cat $PBS_NODEFILE

WORKDIR=/home/n11538554/cfd/qev4evo/v2.20.8.2
OUTPUTDIR=$WORKDIR/$CUR_DATE

mkdir $OUTPUTDIR

cp $JOU $OUTPUTDIR/halfcar.jou
cp $GEOM $OUTPUTDIR/geom.agdb
cp $MESH $OUTPUTDIR/mesh.msh
module load ansys/2024r1

cd $OUTPUTDIR

cat $PBS_NODEFILE | uniq -c | awk '{print $2":"$1}' > ${PBS_JOBID}.flhosts

/pkg/suse12/software/ANSYS/2024R1/v241/fluent/bin/fluent $FLUENT_VERSION -r24.1.0 -meshing -t$nprocs -pib -cnf=${PBS_JOBID}.flhosts -i $OUTPUTDIR/halfcar.jou -g 2>&1 | tee output.log
