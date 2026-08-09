def remove_player(player_name, player_data):
    found = False

    if player_name == '0':
        return

    for i in range(len(player_data)):

        if player_data[i]['name'] == player_name:
            player_data.pop(i)
            # save_file("player_data_file",player_data)
            found = True
            print("Success!")
            break
    if not found:
        print(f"There is no Name: {player_name} in your data!")