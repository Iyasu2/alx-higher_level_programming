#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

print("{:d}".format(len(sys.argv)))
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] not in ["+", "-", "*", "/"]:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit()
else:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{:d} {:s} {:d} = {:.0f}".format(a, sys.argv[2], b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{:d} {:s} {:d} = {:.0f}".format(a, sys.argv[2], b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{:d} {:s} {:d} = {:.0f}".format(a, sys.argv[2], b, mul(a, b)))
    else:
        print("{:d} {:s} {:d} = {:.0f}".format(a, sys.argv[2], b, div(a, b)))
