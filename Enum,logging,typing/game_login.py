from password_hashing import password_validation,hashing_user_password

from sql_run_code import insert_players_data

run = True

while run:
    
    print("         Welcome         ")
    decision = input("""
    1.Login
    2.Sign in
    3.Exit program
    """)
    if decision == '1':
        while True:
            
            username = input("Username:(type NULL to exit)")
            if username == 'NULL':
                
                break
            
            username_password = input("Password:(type NULL to exit)")
            
            if username_password =='NULL':
                
                break
            
            if password_validation(username,username_password):
                
                print("Test is complete")
                
                run = False
                
                break
            
            else:
                continue
        
    elif decision == '2':
        
        username = input("Insert username:")
            
        username_password = input("Insert password: ")
        
        hashed_user_password = hashing_user_password(username_password)
        
        insert_players_data(username,hashed_user_password)
        
    elif decision == '3':
        
        print("You exit..")
        
        break
    
    else:
        
        print("Unknown menu!")