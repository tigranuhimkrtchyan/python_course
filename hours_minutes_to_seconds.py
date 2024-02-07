"5.	Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them."

hours = int(input("Insert houres ")) 
minutes = int(input("Insert minutes "))
c = hours * 3600 + minutes * 60
print(c)