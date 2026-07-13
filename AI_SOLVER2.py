import random
class AI_BOARD:
    def __init__(self,listinput):
        self.board = listinput # Membuat BOARD asli!
    def board_game(self):
        board_display = " ".join(str(n) for n in self.board) # BOARD yang hanya untuk ditampilkan saja!
        print(board_display)
    def cut_the_wire(self,board,i):
        if len(board) == 3:
            print("Can't cut again!")
            return board

        elif len(board) < 3 or len(board) == 4:
            print("Can't cut again!")
            return board
        else:
            if i == 0:
                if board[i] > board[i + 1]:
                    RemovedCableList = [i,i+1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    return board
                else:
                    return board 
            elif i == len(board) - 1:
                if board[i-2] < board[len(board) - 1]:
                    RemovedCableList = [i-2,len(board) - 1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    return board
                else:
                    return board
            elif board[i-1] > board[i] < board[i+1]:
                    RemovedCableList = [i-1,i,i+1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    return board
            else:
                if board[i] > board[i+1]:
                    RemovedCableList = [i,i+1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    return board
                elif board[i-1] < board[len(board) - 1]:
                    RemovedCableList = [i-1,len(board) - 1]
                    for REMOVE in sorted(RemovedCableList, reverse=True):
                        board.pop(REMOVE)
                    return board
                else:
                    print("Can't cut again!")
                    return board
            
                

    def validation_check(self,board):
        if board[0] < board[1] < board[2] or board[0] > board[1] > board[2]:
            return True
        else:
            print("This board is not solveable!")
            print(board)
            return False
            
    def game_start_engine(self,board):
        for i in range(len(board)):
            copied_board = board.copy()
            result = self.cut_the_wire(copied_board,i)
            if result == copied_board:
                continue

            if len(result) == 3:
                if self.validation_check(result):
                    return True
                continue

            if self.game_start_engine(result):
                return True
        return False


run = True
while run:
    input = (input("Put the list: "))
    list_of_input = [int(x) for x in input.split(",")]
    AISOLVE = AI_BOARD(list_of_input)
    AISOLVE.board_game()
    print("Starting the solver.....")
    result = AISOLVE.game_start_engine(AISOLVE.board)
    if result == True:
        print("This board is solveable!")
        run = False
    else:
        print("This board is not solveable!")
        run = False