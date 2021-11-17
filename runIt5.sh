#!/bin/bash
#***** NOTE: run this using: sg fslg_fish "sbatch thefilename"

#SBATCH --time=00:30:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=12288M   # memory per CPU core

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

#modules necessary for BWA
module load bwa/0.7.17

# bwa <index_path/ref_file_name.fa> <R1> <R2> > <output.sam>
bwa mem /fslgroup/fslg_fish/compute/reference/ref_KX897946.1.fa /fslgroup/fslg_fish/compute/S_ciliatus_1003050_R1.fastq /fslgroup/fslg_fish/compute/S_ciliatus_1003050_R2.fastq > /fslgroup/fslg_fish/compute/output1.sam