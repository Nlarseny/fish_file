# A fishy Script
# example of how to run fastqc "./fastqc somefile.txt"

# This allows us to run terminal commands
import subprocess
import sys, getopt

def fastq_to_html(arg):
    num = arg.rfind('.')
    temp = arg[0 : num]
    html_arg = temp + "_fastqc.html"

    return html_arg

def continue_or_not():
    print("FastQC finished, would you like to continue? (y/n)")
    answer = input().lower()

    if answer == 'y':
        return 0
    elif answer == 'n':
        return -1
    else:
         return continue_or_not()


def main(argv):
    opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    fastq_html = fastq_to_html(args[1])

    # The .html files are just a way to see if the sequences are of good quality.
    # The .html files are not used for any additional analyses.
    # FIXED: hardcode issue (python3 fishypipe.py ../FastQC/fastqc ../rockfish_data/S_ciliatus_1003050_R1.fastq)
    fastqc_process = subprocess.run([args[0], args[1]])

    # NOTE: I'm thinking we create an option to show the quality via html and then
    # the user can choose to continue or not
    subprocess.run(["open", fastq_html])


    continue_option = continue_or_not()
    if continue_option < 0:
        quit()

    # piping example
    # ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
    # output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
    # ps.wait()

    print("100% complete")

if __name__ == "__main__":
   main(sys.argv[1:])
