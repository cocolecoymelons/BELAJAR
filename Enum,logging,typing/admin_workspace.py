import sqlite3

from sql_run_code import export_player_data_from_db,show_players,edit_player_profile_on_sql
from edit_player_profile_file import edit_player_profile
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
        
        edit_player_profile()
        
    elif admin_decision == '4':
        
        break
