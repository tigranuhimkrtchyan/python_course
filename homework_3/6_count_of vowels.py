# 6.	Create a function that takes a string and returns the number (count) of vowels contained within it.
# Examples
# 'Celebration' ➞ 5
# 'Palm' ➞ 1
# 'Prediction' ➞ 4
# Notes
text = input ("Write your text ")
vowels=['a','e','i','o','u']
count =0
for i in text:
    if i in vowels:
        count+=1
print (count)

