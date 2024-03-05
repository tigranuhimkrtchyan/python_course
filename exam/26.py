par1 = "1"
par2 = 2
if type(par1) == int and type(par2)== int:
    print(str(par1)+str(par2))
elif type(par1)==str and type(par2)==str:    
    print(int(par1) + int(par2))
else:
    print(None)
