import sqlite3

import logging
from setup_log import setup_log_func
from sql_run_code import show_players

from edit_player_profile_file import edit_player_profile
program_run = True

setup_log_func(__name__)
admin_logger = logging.getLogger("Admin Workspace")

admin_logger.info("Admin run the workspace...")

while program_run:

  try:
    
    admin_decision = input("""
    
    1.Show players
    2.Edit player profile
    3.Player login history
    4.Exit
    
    """)
    
    if admin_decision == '1':
      
      show_players()
      admin_logger.info("Admin run show players command.")

    elif admin_decision == '2':
        
      edit_player_profile()
      admin_logger.info("Admin run edit player profile command.")
                        
    elif admin_decision == '4':
        
      admin_logger.info("Admin exit the program.")
      break

    else:

      print("Unknown menu!")
      admin_logger.info("Admin inserting an unknown command.")

  except sqlite3.OperationalError:

    print("Operational Error: Database table is not found or is locked.")

    admin_logger.info("Database SQL system catch an Operational Error.")

  except sqlite3.IntegrityError:

    print("Integrity Error: Insert a similar data is probihited.")

    admin_logger.info("Database SQL system catch an Integrity Error.")

  except IndexError:

    print("Index Error: Unknown index accessing.")

    admin_logger.info("Database SQL system catch an Index Error.")
  