'''
82. Write a function that counts the number of occurrences of each word in a given string
(Use re module). The function should ignore case and punctuation.

'''

import re
from collections import Counter

def count_word_occurrences(text):
    words=re.findall(r'\b\w+\b',text.lower())

    word_counts=Counter(words)

    return word_counts

text="The quick brown fox jumps over the lazy dog.The dog barks loudly,but the fox ignores it."
word_occurrences=count_word_occurrences(text)
print("word occurrences:",word_occurrences)