#!/usr/bin/python3
for w in range(ord('a'), ord('z') + 1):
    if w != ord('q') and w != ord('e'):
        print("{}".format(chr(w)), end="")
