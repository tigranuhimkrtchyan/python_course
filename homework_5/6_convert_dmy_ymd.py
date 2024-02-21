# 6.	Create a function that converts a date formatted 
# as MM/DD/YYYY to YYYYDDMM.
# Examples
# '11/12/2019' ➞ '20191211'
# '12/31/2019' ➞ '20193112'
# '01/15/2019' ➞ '20191501'
s = '11/12/2019'
converted = s[-4:] + s[3:5] + s[:2]
print(converted)