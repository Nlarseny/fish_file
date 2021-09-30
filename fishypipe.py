# A fishy Script
# example of how to run fastqc "./fastqc somefile.txt"

import subprocess

fastqc_process = subprocess.run(["../FastQC/fastqc", "../rockfish_data/S_ciliatus_1003050_R1.fastq"])

# piping example
# ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
# output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
# ps.wait()

print("100% complete")
