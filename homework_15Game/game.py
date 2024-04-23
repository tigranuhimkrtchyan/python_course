import random

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
curren_player = "X"
gamerunning = True
class Board:
    def __init__(self) -> None:
        self=self
        
    def print_board(self):   
        print(board[0],"|",board[1],"|",board[2])
        print("---------")
        print(board[3],"|",board[4],"|",board[5])
        print("---------")
        print(board[6],"|",board[7],"|",board[8])

    def make_move(self,position):
        self.position = position
        position = int(input("Pleasa insert position from 1 to 9  "))
        if position >=1 and position <=9:
            board[position -1] = curren_player
        else:
            print("NOt correct position")
        return board  
         
    def is_waled_move(self,position):
        self.position = position
        if board[position -1] != " ":
            print("It has already been entered.Insert new position")
    def switch_player(self):
        if curren_player == "X":
            curren_player = "O"
        else:
            curren_player = "X"
    def check_win(self):
        if board[0] == board[1] == board[2] != " " or board[3] == board[4] == board[5] != " " or board[6] == board[7] == board[8] != " " or board[0] == board[3] == board[6] != " " or board[1] == board[4] == board[7] != " " or board[2] == board[5] == board[8] != " " or board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
            print("you won!!!")

    def check_drow(self):
        return(" " not in self.board)
    
class Player:
    def __init__(self,player_symbol):
        self.player_symbol = player_symbol

class Human_player(Player):
    def __init__(self, player_symbol):
        super().__init__(player_symbol)
    def get_move():
        while True:
            return
        
class Computer_player(Player):
    def __init__(self, player_symbol):
        super().__init__(player_symbol)
    def get_move(self,board,position):
        self.board = board
        self.position = position
        while curren_player == "0":
            position =  random.randint(0,8)
            if board[position] == " ":
                board[position] = 0
                   

class Game:
    def __init__(self) -> None:
        self.board = Board
        self.human_player = Human_player
        self.computer_player = Computer_player
    def play_game(self):
        self.board.print_board() 
        while gamerunning:
            Board.print_board()
            Board.make_move()
            Board.is_waled_move()
            Board.switch_player()
            Board.check_win()
            Board.check_drow()
            Human_player.get_move()
            Computer_player.get_move()