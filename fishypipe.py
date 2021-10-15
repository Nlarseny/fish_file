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


def fastq_to_trimmed(arg):
    num = arg.rfind('.')
    temp = arg[0 : num]
    trimmed_arg = temp + "_trimmed.fq"

    return trimmed_arg


def clean_file_name(arg):
    num = arg.rfind('/')
    if num == -1:
        return arg
    else:
        temp = arg[num + 1 : ]
        return temp


def continue_or_not():
    print("(y/n)")
    answer = input().lower()

    if answer == 'y':
        return 0
    elif answer == 'n':
        return -1
    else:
         return continue_or_not()


def run_trimgalore(file, continue_option):
    # continuing with program, on to trimgalore
    print("\n===== RUNNING TRIMGALORE =====\n")

    fastqc_process = subprocess.run(["trim_galore", file, "-o", "trimgalore_output_folder"])

    #trimmed_file_name = fastq_to_trimmed(args[0])
    # print("\nRun fastqc? Trim_galore will run no matter what.")
    # continue_option = continue_or_not()
    if continue_option == 0:
        print("\n===== RUNNING FASTQC =====\n")
        trimmed_file_name = fastq_to_trimmed(file_name)
        location_of_trimmed_file = "./trimgalore_output_folder/" + trimmed_file_name
        fastqc_process = subprocess.run(["fastqc", location_of_trimmed_file])

    return


def main(argv):
    opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    file_name = clean_file_name(args[0])

    print("\nRun fastqc? Trim_galore will run no matter what.")
    continue_option = continue_or_not()

    run_trimgalore(args[0], continue_option)
    run_trimgalore(args[1], continue_option)


    print("Files prepped for Trinity, would you like to continue?")
    continue_option = continue_or_not()
    if continue_option < 0:
        quit()



    # TRIMGALORE will give a file in the fish file folder
    # Trintiy --seqType <string>

    # Trinity --seqType fq --left reads_1.fq --right reads_2.fq --CPU 6 --max_memory 20G
    # Trinity --seqType [fa|fq] --max_memory <maximum_memory> --left input_reads_pair_1.[fa|fq] --right input_reads_pair_2.[fa|fq] [options]
    # Trinity --seqType fq --max_memory 5G --left input_reads_pair_1.fq --right input_reads_pair_2.fq [options]




    # piping example
    # ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
    # output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
    # ps.wait()

    print("\n\n===== 100% complete =====")

if __name__ == "__main__":
   main(sys.argv[1:])
