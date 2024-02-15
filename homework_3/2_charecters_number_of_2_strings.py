# 2.	Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# Examples
# "AB", "CD" ➞ True
# "ABC", "DE" ➞ False
# "hello", "edabit" ➞ False
txt1 =input ("Insert 1st txt ")
txt2 = input ( "Insert 2nd txt ")
if len(txt1) ==len(txt2):
    print ("True ")
else: print ("False")

