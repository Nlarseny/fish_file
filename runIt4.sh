#!/bin/bash
#***** NOTE: run this using: sg fslg_fish "sbatch thefilename"

#SBATCH --time=72:00:00   # walltime
#SBATCH --ntasks=8   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=49512M   # memory per CPU core

if [ "$(id -gn)" != "fslg_fish" ]; then
    echo '*!*!*' This job is not running as the intended group. If you want to run it as fslg_fish, run sbatch as follows:  sg fslg_fish '"'sbatch thefilename'"'
    exit 1
fi


# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE

#modules necessary for fastqc
#module load jdk/1.8
#module load fastqc

#fastqc /fslgroup/fslg_fish/compute/data/dna/rockfish/S_ciliatus_1003050_R1.fastq.gz -o /fslgroup/fslg_fish/compute/jobs/
#python3 /fslgroup/fslg_fish/compute/jobs/fishypipe.py fastqc /fslgroup/fslg_fish/compute/data/dna/rockfish/S_ciliatus_1003050_R1.fastq.gz

#unload no longer used modules
module purge

#modules necessary for trinity
module load jdk/1.8 # Redundant as also used in fastqc, but this call shouldn't cause any issues
module load samtools bowtie2 jellyfish salmon python
module load trinity

Trinity --seqType fq --max_memory 40G --left /fslgroup/fslg_fish/compute/S_ciliatus_1003050_R1.fastq --right /fslgroup/fslg_fish/compute/S_ciliatus_1003050_R2.fastq --CPU 8