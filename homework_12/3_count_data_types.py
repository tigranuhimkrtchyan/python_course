"""
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. 
Finally return the total in a list.
List order is:
[int, str, bool, list, tuple, dictionary]
Examples
count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
Notes
If no arguments are given, return [0, 0, 0, 0, 0, 0]
"""
lst=[]

def count_datatypes(*args):
    count_int=0
    count_str=0
    count_bool=0
    count_list=0
    count_tuple=0
    count_dict=0
    if len(args)==0:
      return lst [0,0,0,0,0,0]
    
    for n in args:
        if isinstance(n,bool):
            count_bool+=1
        elif isinstance(n,int):
            count_int+=1
            
        elif isinstance(n,str):
            count_str+=1     
        
        elif isinstance(n,list):
            count_list+=1
          
        elif isinstance(n,tuple):
            count_tuple+=1
            
        elif isinstance(n,dict):
            count_dict+=1
         
    lst.append(count_int)
    lst.append(count_str)
    lst.append(count_bool)
    lst.append(count_list)
    lst.append(count_tuple)
    lst.append(count_dict)
    

    return lst

x = count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6])
print(x)
