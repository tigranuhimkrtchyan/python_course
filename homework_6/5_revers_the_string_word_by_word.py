"""
Given an input string, reverse the string word by word.
Examples
"the sky is blue" ➞ "blue is sky the"
"  hello world!  " ➞ "world! hello"
"a good   example" ➞ "example good a"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. 
However, your reversed string should not contain leading or 
trailing spaces

"""
txt = input("insert a text ")
revers_txt = txt.split(' ') [::-1]
print(revers_txt)
txt1 = " ".join (revers_txt)
print(txt1.strip())