# 7.	Create a function that replaces all the vowels in a string with a specified character.
# Examples
# 'the aardvark', '#' ➞ 'th# ##rdv#rk'
# 'minnie mouse', '?' ➞ 'm?nn?? m??s?'
# 'shakespeare', '*' ➞ 'sh*k*sp**r*'
text = input ("Write your text ")
vowels=['a','e','i','o','u']
new_text = ""
i = 0
for i in text:
    if i in vowels:
        new_text+="#"
    else:
        new_text += i
print (new_text)


