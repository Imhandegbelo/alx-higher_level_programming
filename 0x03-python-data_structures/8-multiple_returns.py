#!/usr/bin/python3
'''
function that returns a tuple with the length of a string and its first char
@sentence: the sentence to performed
'''


def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        char1 = sentence[0]
        return (length, char1)
    else:
        return "None"
