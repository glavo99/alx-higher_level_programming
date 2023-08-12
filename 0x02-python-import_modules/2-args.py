#!/usr/bin/python3
if __name__ == "__main__":
    import sys

length = len(sys.argv)
if length == 2:
    print("1 argument:")
elif length == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(length))
for i in range(length - 1):
    print("{}: {}".format(i + 1, sys.argv[i + 1])
