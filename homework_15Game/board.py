class Board:
    def __init__(self,n) -> None:
        self.n = n
    def boardd(n):
        n= int(input("inseret n "))
        board = ""
        for i in range(1,2*n+2):
            if i % 2 ==0:
                board +="|    "*(n+1)
            else:
                board +="_____"*n
            board+="\n"
        print(board)
obj = Board(3)
obj.boardd()