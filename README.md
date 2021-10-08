# fish_file
# SCP sample to get files from mary lou -> scp username@ssh.rc.byu.edu:fsl_groups/fslg_fish/compute/data/dna/rockfish/S_ciliatus_1003050_R1.fastq.gz Documents/494R/rockfish_data

# trim_galore requires cutadapt, to run on your own machine proceed to this link and follow the instructions: https://cutadapt.readthedocs.io/en/stable/installation.html

# the biconda install worked the best for me, I then installed fastqc into the environment with conda install -y fastqc 
# I also installed trim_galore this way (conda install -y trim-galore)
# once set up, remember to always run -> [  conda activate cutadaptenv  ]  in order to run the environment, so the correct paths are set
