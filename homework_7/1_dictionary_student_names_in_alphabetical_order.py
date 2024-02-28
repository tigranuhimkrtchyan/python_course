"""
Create a function that takes a dictionary of student names 
and returns a list of student names in alphabetical order.
Examples
{
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
} ➞ ["Becky", "John", "Steve"]
"""
d = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
lst = []
for i in d.values():
    lst.append(i)
print(sorted(lst))