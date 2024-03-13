#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) <= ord('z') and ord(w) >= ord('a'):
            w = chr(ord(w) - 32)
        print("{}".format(w), end="")
    print()
