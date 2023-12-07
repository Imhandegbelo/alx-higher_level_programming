#!/usr/bin/python3
'''
function thath converts roman numerals to integer
'''


def roman_to_int(roman_string):
    roman_char = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
            }

    if type(roman_string) == str:
        num_arr = []

        for ch in roman_string:
            if ch in roman_char:
                num_arr.append(roman_char[ch])
        if len(num_arr) == 1:
            return num_arr[0]
        else:
            num = num_arr[0]
            for i in range(1, len(num_arr)):
                if num_arr[i] > num_arr[i - 1]:
                    num -= num_arr[i]
                else:
                    num += num_arr[i]
        return abs(num)
    else:
        return 0
