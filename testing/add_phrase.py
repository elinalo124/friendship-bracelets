# Imports.
from itertools import groupby
import re
from globals import *

# User input (phrases).
input_phrase = input("Introduce la frase: ").lower()

# Filtering phrase.
input_phrase_filtered = re.sub(SPECIAL_CHARACTERS, "", input_phrase)

# Counting of letters.
sorted_phrase = sorted(input_phrase_filtered)
count_letters = {key: len(list(value)) for key, value in groupby(sorted_phrase)}
