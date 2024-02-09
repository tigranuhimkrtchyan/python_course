# 3.	Create a function that takes a number as an argument and returns "even"
#  for even numbers and "odd" for odd numbers
num = int(input ("insert number ")) 
res = (num % 2 == 1)* "odd" or (num % 2 ==0)* "even"
print(res)