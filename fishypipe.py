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
    print("(y/n)")
    answer = input().lower()

    if answer == 'y':
        return 0
    elif answer == 'n':
        return -1
    else:
         return continue_or_not()


def main(argv):
    opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])

    fastq_html = fastq_to_html(args[0])
    # The .html files are just a way to see if the sequences are of good quality.
    # The .html files are not used for any additional analyses.
    # edited command: (python3 fishypipe.py ../rockfish_data/S_ciliatus_1003050_R1.fastq)

    print("\nRun fastqc? Trim_galore will run no matter what.")
    continue_option = continue_or_not()
    if continue_option == 0:
        fastqc_process = subprocess.run(["fastqc", args[0]])
        subprocess.run(["open", fastq_html])

        print("FastQC finished, would you like to continue?")
        continue_option = continue_or_not()
        if continue_option < 0:
            quit()

    # continuing with program, on to trimgalore
    print("\n===== RUNNING TRIMGALORE =====\n")
    fastqc_process = subprocess.run(["trim_galore", args[0]])

    # TRIMGALORE will give a file in the fish file folder
    




    # piping example
    # ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
    # output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
    # ps.wait()

    print("\n\n===== 100% complete =====")

if __name__ == "__main__":
   main(sys.argv[1:])
