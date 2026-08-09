def edit_player(player_name,player_data):
    found = False
                                
    if player_name == '0':
        return

    for i in range(len(player_data)):

        if player_data[i]['name'] == player_name:

            found = True

            edit_player_name = input("Edit Player Name(0,00 for cancel or skip): ")

            if edit_player_name == '0':
                continue

            if edit_player_name == '00':

                edit_player_health = (input("Edit Player Health(00 for cancel): "))
                
                if edit_player_health == '00':
                    continue
                else:
                    player_data[i]['hp'] = int(edit_player_health)
                    # save_file("player_data_file",player_data)
                    continue
        
            edit_player_health = (input("Edit Player Health(00 for cancel): "))

            if edit_player_health == '00':
                player_data[i]['name'] = edit_player_name
                # save_file("player_data_file",player_data)
                continue
                
            player_data[i]['hp'] = int(edit_player_health)
            player_data[i]['name'] = edit_player_name

    if not found:

        print(f"There is no Name: {player_name} in your data!")

    # save_file("player_data_file",player_data)
    print("Success!")
