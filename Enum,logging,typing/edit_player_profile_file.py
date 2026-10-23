from sql_run_code import export_player_data_from_db,edit_player_profile_on_sql

from player_enum import PlayerStatus

def edit_player_profile():

    player_username = input("Insert player username: ").strip()
    
    player_data = export_player_data_from_db(player_username)
            
    if not player_data:
        
        print("Player is not found!")
        
        return
    
    edit_run = True
    
    while edit_run:
    
        new_player_id = input("Insert new player number id(insert blank for skip): ")
        
        if new_player_id.strip() == '':
            
            new_player_id = player_data[0]
        
        new_player_username = input("Insert new player username(insert blank for skip): ")
       
        if new_player_username.strip() == '':
            
            new_player_username = player_data[1]
            
            
        while True:
            
            player_status = input("Insert new player account status(1.Online 2.Locked 3.Banned #insert the number desired,blank to skip): ")
           
            if player_status.strip() == '1':
                
                player_status = PlayerStatus.ONLINE.value
            
                break
            
            elif player_status.strip() == '2':
                
                player_status = PlayerStatus.LOCKED.value
                
                break
                
            elif player_status.strip() == '3':
                
                player_status = PlayerStatus.BANNED.value
                
                break
                
            elif player_status.strip() == '':
                
                player_status = player_data[3]
                
                break
                
            else:
                
                print("Unknown command!")
            
        edit_run = False
            
    edit_player_profile_on_sql(new_player_id,new_player_username,player_status,player_username)
