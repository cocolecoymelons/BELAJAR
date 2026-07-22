import random
from AI_SOLVER_GENERATOR import main_game_board_generator_engine
#from #AI_SOLVER_LAST import
class BOARD:
    def __init__(self):
        self.board = main_game_board_generator_engine() # This func comes from other file that i imported. This func calls a mini computer
        #board generator AI to find a solvable board instead of random numbers that cant be solved by the user.
    def board_game(self):
        board_display = " ".join(str(n) for n in self.board) # Declaring a variable contains board's series numbers
        print(board_display) #print the numbers
    def board_status_checker(self,board,i):
        if  i >= len(board) or i < 0:
            print("Please choose the right cable")
        elif i == 0:
            return board[i] > board[i+1]
        elif i == len(board) - 1:
            return board[i] > board[i-1]
        else:
            return board[i-1] > board[i] < board[i+1]
    def board_wire_cutter(self,board,i):
        if len(board) <= 4:
            return board
        if not self.board_status_checker(board, i):
            return board
        if i == 0:
            if self.board_status_checker(board, i):
                RemovedCableList = [i,i+1]
                for REMOVE in sorted(RemovedCableList, reverse=True):
                    board.pop(REMOVE)
                return board
        elif i == len(board) - 1:
            if self.board_status_checker(board, i):
                RemovedCableList = [i,i-1]
                for REMOVE in sorted(RemovedCableList, reverse=True):
                    board.pop(REMOVE)
                return board
        elif board[i-1] > board[i] < board[i+1]:
            if self.board_status_checker(board, i):
                RemovedCableList = [i,i-1]
                for REMOVE in sorted(RemovedCableList, reverse=True):
                    board.pop(REMOVE)
                return board
        
    def board_validation_checker(self,board):
        if len(board) != 3:
            return False
        return board[0] < board[1] < board[2] or board[0] > board[1] > board[2] #if any one of this conditions True,
    #then the func returns True, else False
    
    def game_engine(self,board,i):
        self.board_status_checker(board,i) # Call the func to check the board status if for i (index) satisfy any logical conditions.
        if self.board_status_checker(board, i): # if the the func returns True, then:
            self.board_wire_cutter(board,i) #Call the func to cut the desired i
            self.board_validation_checker(board) #Call the function to check if the board is finished or not.
            if self.board_validation_checker(board): # If the func returns True, then the game_engine func will returns True.
                return True
        elif self.board_status_checker(board, i) == False: #Other wise if the user choose wrong cable, the game_engine returns False and lose the game.
            print("You choose the wrong cable, the bomb explode.")
            return True
        return False

BoardGame = BOARD()
run = True
print("""Hello Welcome to the Game!
Your mission is to cut all of the wire that desired by the numbers order.
if you failed, the bomb will explode and you lose the game.
Theres a pattern to know what number cable is to cut first before others.
Good luck!""")
while run: # While loop the game
    BoardGame.board_game() # Call the func to display the board.
    print("Choose cable to cut:\n0,1,2,3,4")
    decision = input("") # Asking user the index.
    result = BoardGame.game_engine(BoardGame.board,int(decision)) # Call the engine func also declare it as "result" variable
    if result: # if the result returns True,then the code below will be executed
        print("Bomb has been defused.")
        run = False
