# 8.	Write a function that takes a credit card number and only displays the last four characters. 
# The rest of the card number must be replaced by ************.
# Examples
# '1234123456785678' ➞ '************5678'
# '8754456321113213' ➞ '************3213'
# '35123413355523' ➞ '**********5523'
card_number = input ("Write your card number ")
first_part= card_number[:-4]
only_last_four = card_number[-4:]
first_part_secret = ""
for i in first_part:
    first_part_secret+="*"
        
print (first_part_secret + only_last_four)
