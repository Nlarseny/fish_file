# fish_file
# SCP sample to get files from mary lou -> scp username@ssh.rc.byu.edu:fsl_groups/fslg_fish/compute/data/dna/rockfish/S_ciliatus_1003050_R1.fastq.gz Documents/494R/rockfish_data

# trim_galore requires cutadapt, to run on your own machine proceed to this link and follow the instructions: https://cutadapt.readthedocs.io/en/stable/installation.html

# I renamed the enviroment to be fishenv (conda create --name fishenv --clone cutadaptenv), make sure you deactivate the environment before you clone it.
# the biconda install worked the best for me, I then installed fastqc into the environment with conda install -y fastqc 
# I also installed trim_galore and trinity this way (conda install -y trim-galore and then conda install -c bioconda trinity)
# once set up, remember to always run -> [  conda activate fishenv  ]  in order to run the environment, so the correct paths are set
