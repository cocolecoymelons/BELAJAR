import random
class AI_BOARD:
    def __init__(self):
        self.board = [random.randint(0,10) for _ in range(10)] # Membuat BOARD asli!
    def board_game(self):
        board_display = " ".join(str(n) for n in self.board) # BOARD yang hanya untuk ditampilkan saja!
        print(board_display)
    def solving_the_board(self,board):
        copied_board = board.copy()
        for i in range(0,9):
            
                    
            
AISOLVE = AI_BOARD()
run = True
while run:
    AISOLVE.board_game()
    print("Starting the solver.....")
    result = AISOLVE.solving_the_board(AISOLVE.board)
    if result == False:
        run = False