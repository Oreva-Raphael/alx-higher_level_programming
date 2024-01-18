#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = 1
    sum = 0
    for w in range(count, len(argv)):
        sum += int(argv[w])
    print("{:d}".format(sum))
