import logging

from sql_run_code import export_player_data_from_db,edit_player_profile_on_sql

from player_enum import PlayerStatus

admin_edit_logger = logging.getLogger("Admin Workspace_edit player profile file")

def edit_player_profile():

    player_username = input("Insert player username: ").strip()

    admin_edit_logger.debug(f"Admin inserting player's name [{player_username}].")
  
    player_data = export_player_data_from_db(player_username)

    admin_edit_logger.debug("System export player's data.")

    if not player_data:
        
        print("Player is not found!")

        admin_edit_logger.debug(f"Player named [{player_username}] is not found in the database.")
      
        return
    
    edit_run = True

    admin_edit_logger.debug(f"Player named [{player_username}] is found.")
  
    while edit_run:
    
        new_player_id = input("Insert new player number id(insert blank for skip): ")
        
        if new_player_id.strip() == '':
            
            new_player_id = player_data[0]
      
            admin_edit_logger.debug(f"Admin bypassed the player id editing section for [{player_username}].")

        new_player_username = input("Insert new player username(insert blank for skip): ")
       
        if new_player_username.strip() == '':
            
            new_player_username = player_data[1]

            admin_edit_logger.debug(f"Admin bypassed the player username editing section for [{player_username}].")
            
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

                admin_edit_logger.debug(f"Admin bypassed the player account status editing section for [{player_username}].")
              
                break
              
            else:
                
                print("Unknown command!")
            
        edit_run = False
            
    edit_player_profile_on_sql(new_player_id,new_player_username,player_status,player_username)

    admin_edit_logger.debug("""
    The editing section is done,
    resulting the player named [{}] profile as
    {new_player_id},{new_player_username},{player_status}.
    """)