# 10.	An isogram is a word that has no duplicate letters. 
# Create a function that takes a string and returns either True or False depending on whether or not it's an 'isogram'.
# Examples
# 'Algorism' ➞ True
# 'PasSword' ➞ False
# # Not case sensitive.
# 'Consecutive' ➞ False
text = input("Insert text ")
num1= len(text)
num2 = len(set(text))
if num1 == num2:
    print("True")
else:
    print("False")
    
