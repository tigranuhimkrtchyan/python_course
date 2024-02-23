""""
Given two strings, create a function that returns the total number 
of unique characters from the combined string.
Examples
count_unique('apple', 'play') ➞ 5
# 'appleplay' has 5 unique characters:
# 'a', 'e', 'l', 'p', 'y'
'sore', 'zebra' ➞ 7
'a', 'soup' ➞ 5
"""
two_str = ("apple","play")
comb = two_str[0]+ two_str[1]
print(len(set(comb)))
