"""
Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the last 
character of the second items in reverse order.lst=[(19542209, "New York") ,
(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), 
(39865590, "California")]
"""
lst=[(19542209, "New York") ,
(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), 
(39865590, "California")]
print(lst.sort(key =lambda x:x[1][-1]))