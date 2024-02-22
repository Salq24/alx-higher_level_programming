#!/usr/bin/python3
"""Thsi module contains a function, read_file,
that reads a text file(UTF8) and prints it to
stdout"""


def read_file(filename=""):
    """This is the function, we are not handling errors
    here. The arg @filename is the name of the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
