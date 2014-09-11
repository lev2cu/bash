#!/usr/bin/python

import sys


def count_ftn(file):
    total=[]
    with open(file) as f:
        for i in f.read().split():
            total += [int(i)]
    return sum(total)



def main():

    for file in sys.argv[1:]:
        intlist = count_ftn(file)
    print intlist





if __name__ == "__main__":
    main()

