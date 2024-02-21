# 8.	EXTRA Knowledge 
# Given a list, rotate the values clockwise by one 
# (the last value is sent to the first position).
# Check the examples for a better understanding.
# Examples
# [1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
# [6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
# [20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]
lst =[1, 5,8,2]
new_lst = lst[-1:] + lst[:-1]
print(new_lst)
