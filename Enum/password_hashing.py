import hashlib
from sql_run_code import export_player_data_from_db

def password_validation(username,password):
    
    player_data = export_player_data_from_db(username)
    
    if player_data is None:
        
        print("User not found!")
        return False
        
    player_password = player_data[4]
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if player_password == hashed_password:
        
        return True
        
    else:
        print("Wrong username or password!")
        
def hashing_user_password(password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    return hashed_password
        