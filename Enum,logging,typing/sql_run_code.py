import sqlite3

from player_enum import PlayerStatus

connect_player_db = sqlite3.connect("player_database.db")

db_cursor = connect_player_db.cursor()


def export_player_data_from_db(player_username):
    
    db_cursor.execute("""
    SELECT * FROM players_data_table
    WHERE player_username = ?
    ;
    """,(player_username,))

    player_data = db_cursor.fetchone()
    
    return player_data

def insert_players_data(username,user_password):
    
    db_cursor.execute("""
    INSERT INTO players_data_table(player_username,player_status,user_password)
    VALUES (?,?,?);
    """,(username,PlayerStatus.ONLINE.value,user_password))
    
    connect_player_db.commit()
    
    print("Sign in successfull!")

def show_players():
    
    db_cursor.execute("""
    SELECT * FROM players_data_table
    LIMIT 100
    """)
    
    rows = db_cursor.fetchall()
    
    the_headers = [header[0] for header in db_cursor.description]
    
    for data_column in rows:
        print(f"""
        {data_column[0]}. Username         :{data_column[1]}
                   Date account created : {data_column[2]}
                   Account status : {data_column[3]}
        """)
    if not rows:
        print("No data.")
        return

    #widths = [max(len(str(x)) for x in kolom) for kolom in zip(the_headers, *rows)]

    #garis = " | ".join(h.ljust(w) for h, w in zip(the_headers, widths))
    
    #print(garis)
    #for r in rows:
        #print(" | ".join(str(v).ljust(w) for v, w in zip(r, widths)))
    
def edit_player_profile(player_username):
    
    edit_run = True
    
    db_cursor.execute("""
    SELECT * FROM players_data_table
    WHERE player_username = ?
    ;
    """,(player_username,))

    player_data = db_cursor.fetchone()
    
    if player_data is None:
        
        print("Player not found!")
        
        return
    
    while edit_run:
        
        new_player_id = input("Insert new player number id(insert blank for skip): ")
        
        if new_player_id.strip() == '':
            
            new_player_id = player_data[0]
        
        new_player_username = input("Insert new player username(insert blank for skip): ")
       
        if new_player_username.strip() == '':
            
            new_player_username = player_data[1]
       
        player_status = input("Insert new player account status(1.Online 2.Locked 3.Banned #insert the number desired,blank to skip): ")
       
        if player_status.strip() == '1':
            
            player_status = PlayerStatus.ONLINE.value
        
        elif player_status.strip() == '2':
            
            player_status = PlayerStatus.LOCKED.value
            
        elif player_status.strip() == '3':
            
            player_status = PlayerStatus.BANNED.value
        
        elif player_status.strip() == '':
            
            player_status = player_data[3]
            
        else:
            
            print("Unknown command!")
            
        db_cursor.execute("""
        UPDATE players_data_table
        SET player_id = ?,
        player_username = ?,
        player_status = ?
        WHERE player_username = ?;
        """,(new_player_id,new_player_username,player_status,player_username))
        
        connect_player_db.commit()
        
        edit_run = False