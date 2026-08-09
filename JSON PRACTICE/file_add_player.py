def add_player(player_name,player_data):
    is_same = False

    if player_name == '0':
        return player_data

    for i in range(len(player_data)):

        if player_data[i]['name'] == player_name:
            is_same = True
            break


    if is_same:
        print(f"Name {player_name} is already exist!")
        is_same = False
        return player_data   
        
    player_hp = int(input("Input Player health point: "))

    new_player = {
        'name': player_name,
        'hp': player_hp
    }

    player_data.append(new_player)
    print("Success")
    return player_data