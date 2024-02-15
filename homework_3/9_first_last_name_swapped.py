# 9.	Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
# Examples
# 'Donald Trump' ➞ 'Trump Donald'
# 'Rosie O'Donnell' ➞ 'O"Donnell Rosie'
# 'Seymour Butts' ➞ 'Butts Seymour'
text =input("Insert first and last name ")
index_of_space =text.find(" ")
first_name = text[:index_of_space]
last_name = text[index_of_space+1:]
print(last_name,first_name)



