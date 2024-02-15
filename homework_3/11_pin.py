# 11.	Create a function to test if a string is a valid pin or not.
# A valid pin has:
# * Exactly 4 or 6 characters.
# * Only numerical characters(0-9).
# * No whitespace.
# Notes. Empty strings should return false when tested.
pin = input("insert your pin ")
if len(pin)>=4 or len(pin)<=6:
    first= True
else:
    first = False
if pin.isdigit():
    second = True
else:
    second = False
if first and second :
    print("True")
else:
    print("False")
