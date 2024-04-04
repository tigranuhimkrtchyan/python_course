"""
Create a class that takes the following four arguments for a particular football player:
    	name
    	age
   	 height
    	weight
Also, create three functions for the class that returns the following strings:
    	get_age() returns "name is age age"
    	get_height() returns "name is heightcm"
   	 get_weight() returns "name weighs weightkg"
Examples
 	p1 = player("David Jones", 25, 175, 75)

 	p1.get_age() ➞ "David Jones is age 25"
 	p1.get_height() ➞ "David Jones is 175cm"
 	p1.get_weight() ➞ "David Jones weighs 75kg"
Notes
name will be passed in as a string and age, height, weight will be integers.
"""
class Player:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self) -> str:
    
        def get_age():
            return f"{self.name} is age {self.age}"
        def get_height():
            return f"{self.name} is {self.height} cm"
        def  get_weight():
            return f"{self.name} weights {self.weight} kg"
p1 = Player("David Jones", 25, 175, 75)
print(p1.get_age())
print(p1.get_height()) 
print(p1.get_weight())