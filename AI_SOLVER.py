import random
class AI_BOARD:
    def __init__(self):
        self.board = [random.randint(0,10) for _ in range(5)] # Membuat BOARD asli!
    def board_game(self):
        board_display = " ".join(str(n) for n in self.board) # BOARD yang hanya untuk ditampilkan saja!
        print(board_display)
    def solving_the_board(self,board):
        copied_board = board.copy()
        i = 0
        print("Removing cables from starting point of index 0...")
        RemovedCableList = [i,i+1]
        for REMOVE in sorted(RemovedCableList, reverse=True):
            copied_board.pop(REMOVE)
            print("Succes removing the Cable in index 0 and 1.")
            print(copied_board)
            if copied_board[0] < copied_board[1] < copied_board[2] or copied_board[0] > copied_board[1] > copied_board[2]:
                print("This board is solveable")
                return True
            else:
                print("This board is not solveable with starting point of index 0.")
                print("Try another method....")
                
        copied_board = board.copy()
        i = 4
        print("Removing cables from starting point of index 4...")
        RemovedCableList = [i,i-1]
        for REMOVE in sorted(RemovedCableList, reverse=True):
            copied_board.pop(REMOVE)
            print("Succes removing the Cable in index 3 and 4.")
            print(copied_board)
            if copied_board[0] < copied_board[1] < copied_board[2] or copied_board[0] > copied_board[1] > copied_board[2]:
                print("This board is solveable")
                return True
            else:
                print("This board is not solveable with starting point of index 0.")
                print("Try another method....")
        print("No other method left.... this board is not solveable.")
        print(copied_board)
        return False
AISOLVE = AI_BOARD()
run = True
while run:
    AISOLVE.board_game()
    print("Starting the solver.....")
    result = AISOLVE.solving_the_board(AISOLVE.board)
    if result == False:
        run = False