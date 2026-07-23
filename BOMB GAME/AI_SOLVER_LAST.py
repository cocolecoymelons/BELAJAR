import random
class AI_BOARD:
    def __init__(self):

        self.board = [] # Meminta User menginput board (baik berapa kolom) , membuat board random, dan menentukan apa bisa diselesaikan atau tidak

        self.solutions = []  # nampung semua kombinasi/jalur yang berhasil
        self.failed_combinations = []
    def board_game(self):
        print(" ".join(str(n) for n in self.board)) # Ini memisahkan elemem elemen pada self.board dengan pemisah tertentu
    def board_combination_generate(self):
            self.board.clear()
            self.solutions.clear()
            self.failed_combinations.clear()
            for _ in range(0,7):
                self.board.append(random.randint(0,9))
            return self.board

    def cut_wire_checker(self, board, i): # Meminta fungsi ini memotong kabel sesuai indeks
        if i < 0 or i >= len(board): 
            return False # akan di return False di cut_the_wire()
        if i == 0:
            return board[i] > board[i + 1]
        elif i == len(board) - 1:
            return board[i - 1] < board[i] #
        else:
            return board[i - 1] > board[i] < board[i + 1] #

    def cut_the_wire(self, board, i):
        if len(board) <= 4:
            return board # Jika terpenuhi, maka akan di return nilai board sehingga dapat di cek di engine
        if not self.cut_wire_checker(board, i):
            return board
        if i == 0:
            if self.cut_wire_checker(board, i):
                board.pop(1); board.pop(0)
                #return self.cut_the_wire(board, i)
            return board
        elif i == len(board) - 1:
            if self.cut_wire_checker(board, i):
                board.pop(len(board) - 1); board.pop(i - 1)
                #return self.cut_the_wire(board, i)
            return board
        else:
            if self.cut_wire_checker(board, i):
                board.pop(i + 1); board.pop(i); board.pop(i - 1)
                #return self.cut_the_wire(board, i)
            return board
        # Semua persyaratan akan me-return nilai board baik sudah dipotong maupun tidak dipotong

    def validation_check(self, board):
        if len(board) != 3: 
            return False # Apabila terpenuhi, maka nilai validation_check() adalah False di engine.
        return board[0] < board[1] < board[2] or board[0] > board[1] > board[2] # return jika len(board) = 3, lalu jika tidak monotic, maka return False

    def game_start_engine(self, board, path=None):
        if path is None:
            path = []

        if self.validation_check(board):
            self.solutions.append(tuple(path) + (tuple(board)))
            return  # jalur ini selesai (berhasil), tapi TETAP lanjut cek jalur lain
        else:
            self.failed_combinations.append(tuple(path) + (tuple(board)))
        for i in range(len(board)):
            copied_board = board.copy()
            original_len = len(copied_board)
            result = self.cut_the_wire(copied_board, i)

            if len(result) == original_len:
                continue  # potongan ke-i tidak menghasilkan perubahan, skip

            # rekursi terus ke SEMUA cabang, tidak return begitu ketemu satu
            self.game_start_engine(result, path + [tuple(board)])

AISOLVE = AI_BOARD()

run = True
while run:
    #user_input = input("Input the list: ")
    #input_list = [int(x) for x in user_input.split(",")]
    #AISOLVE = AI_BOARD(input_list)
    #AISOLVE = AI_BOARD()
    AISOLVE.board_game()
    print("Starting the solver.....")
    AISOLVE.game_start_engine(AISOLVE.board.copy())

    if AISOLVE.solutions:
        print(f"Found {len(AISOLVE.solutions)} solution/s:")
        for idx, sol in enumerate(AISOLVE.solutions, 1):
            print(f"{idx}. {sol}")
        run = False
    else:
        print("This board is not solvable!")
        for idx, sol in enumerate(AISOLVE.failed_combinations, 1):
            print(f"{idx}. {sol}")
        AISOLVE.board_combination_generate()
