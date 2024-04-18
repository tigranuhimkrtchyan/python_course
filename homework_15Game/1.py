 
def board():
    n = int(input("insert n "))
    board = []
    row = []
    for i in range(n):        
        for j in range(n):
            row.append('-')
            board.append(row)
        return(board)
    
obj = board()
print(obj)
