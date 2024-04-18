 
def board():
    n = int(input("insert n "))
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('-')
            board.append(row)
        return(board)
    
obj = board()
print(obj)
