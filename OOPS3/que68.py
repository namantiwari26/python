'''
68. Illustrate with example re module along with its functions: findall(),match(),search()
'''

#ANSWER

import re

# Sample text
text = "The quick brown fox jumps over the lazy dog. The rain in Spain stays mainly in the plain."

# Using findall() to find all occurrences of the word "the" (case-insensitive)
pattern = r"the"
matches = re.findall(pattern, text, re.IGNORECASE)
print(f"findall() found {len(matches)} matches:", matches)
# Output: findall() found 4 matches: ['The', 'the', 'The', 'the']

# Using match() to check if the text starts with "The quick"
pattern = r"The quick"
match = re.match(pattern, text)
if match:
    print("match() found:", match.group())
else:
    print("match() found no match")
# Output: match() found: The quick

# Using search() to find the first occurrence of the word "rain"
pattern = r"rain"
search = re.search(pattern, text)
if search:
    print("search() found:", search.group())
else:
    print("search() found no match")
# Output: search() found: rain

'''
Explanation
re.findall(): Finds all occurrences of the pattern in the text, regardless of their position.
re.match(): Checks only the beginning of the string for a match. In this example, it matches "The quick" at the start of the text.
re.search(): Scans the entire string and returns the first occurrence of the pattern. Here, it finds the first occurrence of "rain" in the text.
'''