# 5.	Given a list of integers, determine whether the sum 
# of its elements is even or odd.
# The return value should be a string "odd" or "even".
# If the input list is empty, consider it as a list with a zero [0].
# Examples
# [0] ➞ 'even'
# [1] ➞ 'odd'
# [] ➞ 'even'
# [0, 1, 5] ➞ 'even'
lst = [0,1,5]
if sum(lst) % 2 == 1:
    print("odd")
else:
    print("even")