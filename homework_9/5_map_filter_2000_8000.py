"""
Using map() and filter() functions add 2000 to the values below 8000.
"""
lst = [1,7982,145,500,9000,15000]
lst1 = list(filter(lambda i :i<8000,lst))
print(lst1)
print(list(map(lambda i:i+2000,lst1)))