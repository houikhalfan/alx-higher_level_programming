#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """Separate text after the delimiter"""
    if isinstance(text, str):
        sentences = text.replace('?', '?-')\
            .replace('.', '.-')\
            .replace(':', ':-')\
            .split('-')
        for i, sentence in enumerate(sentences):
            if sentence:
                if i != len(sentences) - 1:
                    print(sentence.strip() + '\n')
                else:
                    print(sentence.strip(), end='')
    else:
        raise TypeError("text must be a string")
