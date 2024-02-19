def check(s):
    regex=eval(s)
    if regex:
        return True
    else:
        return False 
print(check("13 > 44 > 33 > 1"))