
from file_save_load_function import save_file,load_file
from file_edit_player import edit_player
from file_remove_player import remove_player
from file_add_player import add_player

player_data = load_file("player_data_file")

while True:
    try:
        decision = input("""
            MENU
        ------------
        1. Add Player
        2. Remove Player
        3. Edit Player
        4. Break

""")
        if decision == '1':

            player_name = input("Input Player name (0 for cancel): ")

            add_player(player_name, player_data)

            save_file("player_data_file",player_data)

        elif decision == '2':

            player_name = input("Input Player name (0 for cancel, make sure the name is correct): ")
                
            remove_player(player_name,player_data)

            save_file("player_data_file",player_data)

        elif decision == '3':
            player_name = input("Input Player name (0 for cancel, make sure the name is correct): ")
                            
            if player_name == '0':
                continue

            edit_player(player_name,player_data)

            save_file("player_data_file",player_data)

        elif decision == '4':
            break

    except ValueError:
        print("INPUT ANGka WOI ANJENG")

print(player_data)
