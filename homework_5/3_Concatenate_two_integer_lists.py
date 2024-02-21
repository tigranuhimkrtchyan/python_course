# 3.	Create a function to concatenate two integer lists.
# Examples
# [1, 3, 5], [2, 6, 8] ➞ [1, 3, 5, 2, 6, 8]
# [7, 8], [10, 9, 1, 1, 2] ➞ [7, 8, 10, 9, 1, 1, 2]
# [4, 5, 1], [3, 3, 3, 3, 3] ➞ [4, 5, 1, 3, 3, 3, 3, 3]

lst1 = [4, 5, 1]
lst2 = [3, 3, 3, 3, 3]
lst1.extend(lst2)
print(lst1)