import random
class AI_BOARD:
    def __init__(self):
        self.board = [] #[random.randint() for _ in range()] <- if i want to test the AI 
        self.solutions = []
        self.failed_combinations = []
    def board_combination_generate(self):
        self.board.clear()
        self.solutions.clear()
        self.failed_combinations.clear()
        for _ in range(0,10):
            self.board.append(random.randint(0,9))
        return self.board
    def board_game(self):
        print(" ".join(str(n) for n in self.board)) 
    def cut_wire_checker(self, board, i): 
        if i < 0 or i >= len(board): 
            return False 
        if i == 0:
            return board[i] > board[i + 1]
        elif i == len(board) - 1:
            return board[i - 1] < board[i] 
        else:
            return board[i - 1] > board[i] < board[i + 1] 

    def cut_the_wire(self, board, i):
        if len(board) <= 4:
            return board 
        if not self.cut_wire_checker(board, i):
            return board
        if i == 0:
            if self.cut_wire_checker(board, i):
                RemovedCableList = [i,i+1]
                for REMOVE in sorted(RemovedCableList, reverse=True):
                    board.pop(REMOVE)

            return board
        elif i == len(board) - 1:
            if self.cut_wire_checker(board, i):
                RemovedCableList = [i,i-1,]
                for REMOVE in sorted(RemovedCableList, reverse=True):
                    board.pop(REMOVE)

            return board
        else:
            if self.cut_wire_checker(board, i):
                RemovedCableList = [i-1,i,i+1]
                for REMOVE in sorted(RemovedCableList, reverse=True):
                    board.pop(REMOVE)

            return board


    def validation_check(self, board):
        if len(board) != 3: 
            return False
        return board[0] < board[1] < board[2] or board[0] > board[1] > board[2] 

    def game_start_engine(self, board, path=None):
        if path is None: # Path role in this function is as the footsteps. As the AI try to solve the board, theres n steps to solve the board
            # So with variable path as a list, we could store all the steps and later display it. For this actions to happen, you can go to
            # the next file (AI_SOLVER_LAST.py)
            path = []

        if self.validation_check(board):
            self.solutions.append(tuple(path) + (tuple(board))) # I used tuple for any case if theres any accident on the combinations numbers
            # I also asked to Claude, and suggesting me to use tuple.
            return
        else:
            self.failed_combinations.append(tuple(path) + (tuple(board)))
        for i in range(len(board)):
            copied_board = board.copy()
            original_len = len(copied_board)
            result = self.cut_the_wire(copied_board, i)

            if len(result) == original_len:
                continue 


            self.game_start_engine(result, path + [tuple(board)])
def main_game_board_generator_engine():
    AISOLVE = AI_BOARD()

    while True:
        #user_input = input("Input the list: ")
        #input_list = [int(x) for x in user_input.split(",")]
        #AISOLVE = AI_BOARD(input_list)
        #AISOLVE = AI_BOARD()
    
        AISOLVE.board_combination_generate() # Call board combination generator func. For every board that has been
        #generated,the AI try to solve the generated board. 
        main_game_board = AISOLVE.board.copy() #This variable will be our game board in the main code
        AISOLVE.game_start_engine(AISOLVE.board.copy()) # Call the Ai engine to solve the board

        if AISOLVE.solutions:
            return main_game_board
