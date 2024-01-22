#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = tuple(sentence.split())
    return length, first[0][0]
