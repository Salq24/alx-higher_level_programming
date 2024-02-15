#!/usr/bin/python3
"""This module has a function named text_indentation.
It prints a text with 2 new lines after each of these
characters '.', '?', ':'
"""


def text_indentation(text):
    """This is the function. It takes in an input,
    which is, text. and indents it wth two new lines
    after '.', '?', ':' characters.

    Raises: Typerror if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cnt = 0
    while cnt < len(text) and text[cnt] == " ":
        cnt = cnt + 1

    while cnt < len(text):
        print(text[cnt], end="")
        if text[cnt] == "\n" or text[cnt] in ".?:":
            if text[cnt] in ".?:":
                print("\n")
            cnt = cnt + 1
            while cnt < len(text) and text[cnt] == " ":
                cnt = cnt + 1
            continue
        cnt = cnt + 1
