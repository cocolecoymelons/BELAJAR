import sqlite3

from sql_run_code import show_players,edhit_player_profile

program_run = True

while program_run:
    admin_decision = input("""
    
    1.Show players
    2.Edit player profile
    3.Player login history
    4.Exit
    
    """)
    
    if admin_decision == '1':
        
        show_players()
    
    elif admin_decision == '2':
        
        player_username = input("Insert player username: ").strip()
        
        edit_player_profile(player_username)
        
    elif admin_decision == '4':
        
        break