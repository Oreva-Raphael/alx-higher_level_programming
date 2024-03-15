#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    counter = 1
    arg_no = len(argv)
    if arg_no == 1:
        print("0 arguments.")
    elif arg_no == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(counter, argv[counter]))
    elif arg_no > 2:
        print("{:d} arguments:".format(arg_no-1))
        while counter < arg_no:
            print("{:d}: {:s}".format(counter, argv[counter]))
            counter += 1
