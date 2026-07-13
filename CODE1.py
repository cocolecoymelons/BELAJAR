import random
class BOARD:
    def __init__(self):
        self.board = [random.randint(0,10) for _ in range(5)] # Membuat BOARD asli!
    def board_game(self):
        board_display = " ".join(str(n) for n in self.board) # BOARD yang hanya untuk ditampilkan saja!
        print(board_display)
    def board_status_checker(self,board,decision):
        new_board = board.copy()
        if len(new_board) <= 3: # Kalau Jumlah list 3
            if len(new_board) == 3:
                if new_board[0] < new_board[1] < new_board[2] or new_board[0] > new_board[1] > new_board[2]: # a < b < c akan bernilai benar dan bom berhasil dijinakkan
                    print("The Bomb is defused.")
                    return False
                else: #KAlau Tidak , maka lewat.
                    print("Unstable current caused by missing cables leading to igniting the Bomb. *BOOM")
                    return False
            else:
                print("Unstable current caused by missing cables leading to igniting the Bomb. *BOOM")
                return False

        i = int(decision) # Pilihan dibuat dalam variabel i
        try:

            if i == len(new_board) - 1: # kalau i nya lebih kecil dari jumlah elemen dalam list:
                if new_board[i] < new_board[i-1] or new_board[i] <= new_board[i-1] or new_board[i] == new_board[i-1]:
                    print("You cut the wrong wire, the Bomb explode!")
                    return False
                
                elif new_board[i] > new_board[i - 1]:
                    print("You cut the wire!")
                    RemovedCableList = [i,i - 1]
                    for REMOVE in sorted(RemovedCableList, reverse= True):
                        board.pop(REMOVE)
                    return True

            elif i == 0:
                if new_board[i] < new_board[i+1] or new_board[i] <= new_board[i+1] or new_board[i] == new_board[i+1]:
                    print("You cut the wrong wire, the Bomb explode!")
                    return False
                elif new_board[i] > new_board[i + 1]:
                    print("You cut the wire!")
                    RemovedCableList = [i,i + 1]
                    for REMOVE in sorted(RemovedCableList,reverse= True):
                        board.pop(REMOVE)
                    return True
                    
            elif i == -1:
                print("There's no such thing!") 

        except IndexError:
            print("That's not how it works.")

        except ValueError:
            print("Error: Wrong Value!")

        if new_board[i - 1] > new_board[i] < new_board[i + 1]:
            print("You cut the wire!") # misalkan kabel a,b,c , maka a > b < c benar
            RemovedCableList = [i - 1,i,i+1]
            for REMOVE in sorted(RemovedCableList,reverse=True):
                board.pop(REMOVE)
            return True
        elif new_board[i - 1] <= new_board[i] < new_board[i + 1] or new_board[i - 1] < new_board[i] <= new_board[i + 1]:
            print("Those three wires are connected, you cut the wrong wire!")
            return False
        elif new_board[i - 1] < new_board[i] > new_board[i + 1] or new_board[i - 1] <= new_board[i] > new_board[i + 1] or new_board[i - 1] < new_board[i] >= new_board[i + 1]:
            print("You cut the wrong wire, the Bomb explode!")
            return False
        elif new_board[i - 1] == new_board[i] or new_board[i + 1] == new_board[i]:
            print("You cut the wrong wire, the Bomb explode!")
            return False
            
BoardGame = BOARD()
run = True
print("""Hello Welcome to the Game!
Your mission is to cut all of the wire that desired by the numbers order.
if you failed, the bomb will explode and you lose the game.
Theres a pattern to know what number cable is to cut first before others.
Good luck!""")
while run:
    BoardGame.board_game()
    print("Choose cable to cut:\n0,1,2,3,4")
    decision = input("")
    result = BoardGame.board_status_checker(BoardGame.board,decision)
    if result == False:
        break
