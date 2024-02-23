"""
Write a function that takes a list of numbers and returns a
 list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
[1, 2, 3, 4, 5, 6] ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
[-1, -2, -3, -4, -5, -6] ➞ [-12, -9]
[0, 0] ➞ [0, 0]
Notes
Count 0 as an even number.
"""
lst = [-1,-2,-3,-4,-5,-6]
sum_odd, sum_even = 0, 0 
even_odd = []
for i in lst :
    if i % 2 :
        sum_odd += i
    else :
        sum_even +=i
even_odd.append(sum_even)
even_odd.append(sum_odd)
print(even_odd)
