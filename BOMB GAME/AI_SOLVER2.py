import random
class AI_BOARD:
    def __init__(self,input_list):
        self.board = input_list#[random.randint(0,9) for _ in range(0,6)] # Membuat BOARD asli!
        self.list_of_cutted_boards = []
    def board_game(self):
        board_display = " ".join(str(n) for n in self.board) # BOARD yang hanya untuk ditampilkan saja!
        print(board_display)
    def cut_wire_checker(self,board,i):
        if i < 0 or i >= len(board):
            print(f"Index {i} is out of bounds for the board of length {len(board)}.")
            return False
        if i == 0:
            if board[i] > board[i + 1]:
                return True
            else:
                return False
        elif i == len(board) - 1:
            if board[i-1] < board[len(board) - 1]:
                return True
            else:
                return False
        elif board[i-1] > board[i] < board[i+1]:
            return True
        else:
            return False
    def cut_the_wire(self,board,i):
        if len(board) == 3:
            print(f"Can't cut again! this board has length {len(board)}. The board is {board}")
            return board

        elif len(board) < 3 or len(board) == 4:
            print(f"Can't cut again! this board has length {len(board)}. The board is {board}")
            return board
        else:
            if i == 0:
                if self.cut_wire_checker(board,i):
                    RemovedCableList = [i,i+1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    self.list_of_cutted_boards.append(board)
                    return self.cut_the_wire(board,i)
                else:
                    return board 
            elif i == len(board) - 1:
                if self.cut_wire_checker(board,i):
                    RemovedCableList = [i-1,len(board) - 1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    self.list_of_cutted_boards.append(board)
                    return self.cut_the_wire(board,i)
                else:
                    return board
            elif self.cut_wire_checker(board,i):
                    RemovedCableList = [i-1,i,i+1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    self.list_of_cutted_boards.append(board)
                    return self.cut_the_wire(board,i)
            else:
                    return board
            
                

    def validation_check(self,target):
        for candidate in target:
            if len(candidate) == 3:
                if candidate[0] < candidate[1] < candidate[2] or candidate[0] > candidate[1] > candidate[2]:
                    return True
            else:
                print("This board is not solvable!")
                return False
            
    def game_start_engine(self, board):
        for i in range(len(board)):
            copied_board = board.copy()
            original_len = len(copied_board)          # simpan panjang awal
            self.cut_wire_checker(board, i)
            result = self.cut_the_wire(copied_board, i)
            if len(result) == original_len:            # cek apakah benar2 ada yg kepotong
                continue

            if self.validation_check(self.list_of_cutted_boards):
                return True

            if self.game_start_engine(result):
                return True
        return False


run = True
while run:
    input = input("Input the list: ")
    input_list = [int(x) for x in input.split(",")]
    AISOLVE = AI_BOARD(input_list)
    AISOLVE.board_game()
    print("Starting the solver.....")
    result = AISOLVE.game_start_engine(AISOLVE.board)
    if result == True:
        print("This board is solvable!")
        run = False
    else:
        print(f"This board is not solvable! {AISOLVE.list_of_cutted_boards}")
        run = False