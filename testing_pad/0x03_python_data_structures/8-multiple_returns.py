#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = tuple(sentence.split())
    if length == 0:
        return length, None
    else:
        return length, first[0][0]
