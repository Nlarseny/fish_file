# A fishy Script
# example of how to run fastqc "./fastqc somefile.txt"

import subprocess

list_files = subprocess.run(["ls", "-l"])
