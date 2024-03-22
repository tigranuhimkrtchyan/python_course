"""
Գրել դեկորատոր, որը ստուգում է, թե ինչ տիպի փոփոխական է վերադարձվում։
"""

def dec(func):
    def wrapper(*args,**kwargs):        
        func(*args,**kwargs)
        for i in args:
            print(type(i))
        
    return wrapper
@dec
def mmm(*args,**kwargs):
    print("type of variables")
    
mmm([1,2,3],5,"hi")



