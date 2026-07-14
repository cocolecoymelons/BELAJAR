class AI_BOARD:
    def init(self, input_list):
        self.board = input_list
        self.solutions = []  # nampung semua kombinasi/jalur yang berhasil

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
        if i == 0:
            if self.cut_wire_checker(board, i):
                board.pop(1); board.pop(0)
                return self.cut_the_wire(board, i)
            return board
        elif i == len(board) - 1:
            if self.cut_wire_checker(board, i):
                board.pop(len(board) - 1); board.pop(i - 1)
                return self.cut_the_wire(board, i)
            return board
        else:
            if self.cut_wire_checker(board, i):
                board.pop(i + 1); board.pop(i); board.pop(i - 1)
                return self.cut_the_wire(board, i)
            return board

    def validation_check(self, board):
        if len(board) != 3:
            return False
        return board[0] < board[1] < board[2] or board[0] > board[1] > board[2]

    def game_start_engine(self, board, path=None):
        if path is None:
            path = []

        if self.validation_check(board):
            self.solutions.append(path + [tuple(board)])
            return  # jalur ini selesai (berhasil), tapi TETAP lanjut cek jalur lain

        for i in range(len(board)):
            copied_board = board.copy()
            original_len = len(copied_board)
            result = self.cut_the_wire(copied_board, i)

            if len(result) == original_len:
                continue  # potongan ke-i tidak menghasilkan perubahan, skip

            # rekursi terus ke SEMUA cabang, tidak return begitu ketemu satu
            self.game_start_engine(result, path + [tuple(board)])
run = True
while run:
    input_list = [int(x) for x in input("Input the list: ").split(",")]
    AISOLVE = AI_BOARD(input_list)
    AISOLVE.board_game()
    print("Starting the solver.....")
    AISOLVE.game_start_engine(AISOLVE.board.copy())

    if AISOLVE.solutions:
        print(f"Ditemukan {len(AISOLVE.solutions)} jalur solusi:")
        for idx, sol in enumerate(AISOLVE.solutions, 1):
            print(f"{idx}. {sol}")
    else:
        print("Board ini tidak bisa diselesaikan.")