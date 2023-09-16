# Imports.
from itertools import groupby
import re
from globals import *
from base_phrases import fbrace_phrases

example_input = {'a': 1, 'e': 4, 'f': 8, 'l': 4, 'o': 0, 'r': 2, 's': 2, 't': 1, 'w': 1}


# Comparison function.
def compare_phrase(dict1: dict, dict2: dict) -> bool:
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    if set(keys1) >= set(keys2):
        validation = []
        for key in keys2:
            validation.append(dict1[key] >= dict2[key])
        return len(keys2) == sum(validation)
    else:
        return False


for phrase in fbrace_phrases:
    print(phrase, compare_phrase(example_input, phrase[1]))
