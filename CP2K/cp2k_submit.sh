#!/bin/bash
#SBATCH --job-name=neutral
#SBATCH --account=prezhdo_176
#SBATCH --partition=prezhdo
#SBATCH --nodes=2
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1
#SBATCH --time=05:00:00
#SBATCH --output=out.log
#SBATCH --error=out.err
#SBATCH --mem=0

module load gcc/13.3.0
module load openmpi/5.0.5-alt
module load cp2k/2024.3

# For single processing with OpenMPI
#srun cp2k.ssmp -i geo_opt.in -o geo_opt_out.log

# For parallel processing with OpenMPI
srun cp2k.psmp -i geo_opt.in -o geo_opt_out.log
