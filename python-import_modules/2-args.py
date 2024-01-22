#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    plural_s = "s" if num_args != 1 else ""

    if num_args == 0:
        print("{} argument{}.".format(num_args, plural_s))
    else:
        print("{} argument{}:".format(num_args, plural_s))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
