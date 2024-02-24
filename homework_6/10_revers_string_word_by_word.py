"""
Given an input string, reverse the string word by word 
(reversed word also).
Examples
"the sky is blue" ➞ "eulb si yks eht"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, 
your reversed string should not contain leading or trailing spaces.
"""
# txt = input("insert a text ")
# revers_txt = txt.split(' ') [::-1]
# print(" ".join(revers_txt))
txt = input("insetr your text ")
reversed = ("").join(reversed(txt))
print(reversed.strip())