import sys

def reverse (inputpath, outputpath):
    with open(inputpath, 'r') as inputfile:
        with open(outputpath, 'w') as outputfile:
            for line in inputfile:
                outputfile.write(line[::-1])

def copy(inputpath, outputpath):
    with open(inputpath, 'r') as inputfile:
        with open(outputpath, 'w') as outputfile:
            for line in inputfile:
                outputfile.write(line)

def duplicate_contents(inputpath, n):
    with open(inputpath, "r") as inputfile:
        tehon = inputfile.read()
        with open(inputpath,"a") as inputfile:
            for i in range(n):
                inputfile.write(tehon)

def replace_string (inputpath,needle,newstring):
    with open(inputpath, "r") as inputfile:
        lines=inputfile.readlines()
        with open(inputpath, "w") as inputfile:
            for line in lines:
                inputfile.write(line.replace(needle,newstring))
            

if __name__ == "__main__":
    order = sys.argv[1]
    if order == "reverse":
        reverse(sys.argv[2], sys.argv[3])
    elif order == "copy":
        copy(sys.argv[2], sys.argv[3])
    elif order == "duplicate":
        duplicate_contents(sys.argv[2], int(sys.argv[3]))
    elif order == "replace":
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("error")

    