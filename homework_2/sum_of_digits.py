# 1.	For this challenge, you are supposed to find the sum of the digits of a two-digit number.
# 45 ➞ 9
# 38 ➞ 11
# 67 ➞ 13
num = int(input ("insert two digit number"))
last_digit = num %10
first_digit = num //10
sum = last_digit + first_digit
print(sum)