#!/usr/bin/python3

if __name__ == "__main__":
    import sys

if len(sys.argv) == 2:
    print("1 argument:")
elif len(sys.argv) == 1:
    print("0 arguments.")
    sys.exit()
else:
    print("{:d}".format(len(sys.argv) - 1), "arguments:")

for i in range(1, len(sys.argv)):
    print("{:d}: {:s}".format(i, sys.argv[i]))
