#!/usr/bin/python

import re


def sort_string(my_str):
    chunks = my_str.split(' ')
    return sorted(chunks, key=str.lower)


if __name__ == '__main__':
    print('Enter your string:')
    str_input = input()
    my_str = ''

    # removing special characters
    for k in str_input.split("\n"):
        my_str += (re.sub(r"[^a-zA-Z]+", ' ', k))

    print(sort_string(my_str))
