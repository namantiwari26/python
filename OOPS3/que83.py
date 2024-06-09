'''
83. Write a function that uses regular expressions to find all words starting with a specific
letter (case-insensitive) in a given string

'''
import re

def find_words_starting_with_letter(text,letter):
    pattern=r'\b'+re.escape(letter)+r'\w*'

    matches=re.findall(pattern,text,re.IGNORECASE)

    return matches

text="The quick brown fox jumps over the lazy dog"
letter="b"
result=find_words_starting_with_letter(text,letter)

print("Words starting with'{}' in the text:{}".format(letter,result))
