"""
Create a function that takes the month and year (as integers) and 
returns the number of days in that month.
Examples
days(2, 2018) ➞ 28
days(4, 654) ➞ 30
days(2, 200) ➞ 28
days(2, 1000) ➞ 28
Notes
Don't forget about leap years!
"""
def f(a,b):
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        print( 31)
    elif a==4 or a==6 or a==9 or a ==11:
        print( 30)
    elif a==2 and b%4==0 and b%100!=0 :
        print( 29)
    else:
        print( 28)
f(2,200)

    