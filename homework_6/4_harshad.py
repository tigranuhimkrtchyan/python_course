"""
A number is said to be Harshad if it's exactly divisible 
by the sum of its digits. Create a function that determines 
whether a number is a Harshad or not.
Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True
is_harshad(89) ➞ False
is_harshad(516) ➞ True
is_harshad(200) ➞ True
"""
"""num = int(input("Insert a number "))
sum = 0
rest_num = num
while rest_num > 0:
   sum += rest_num % 10 
   rest_num //=10
print(num % sum ==0 )
"""
num =int(input("insert a number "))
last_digit = num % 10
midl_digit = num //10 %10
first_digit = num //100
print( num % (last_digit +  midl_digit + first_digit) ==0)