"""
Write a function that takes a string name and a number num (either 0 or 1) 
and return 'Hello' + name if num is 1, otherwise return 'Bye' + name.
Examples
say_hello_bye('alon', 1) ➞ 'Hello Alon'
say_hello_bye('Tomi', 0) ➞ 'Bye Tomi'
say_hello_bye('jose', 0) ➞ 'Bye Jose'
"""
def f(name,number):
    match number:
        case 1:
            print(f"Hello {name}")
        case 0:
            print(f"Bye {name}")
        case _:
            print("not valid number insert 1 or 0 ")
f(name=input("Insert your name "),number = int(input("insert number ")))

