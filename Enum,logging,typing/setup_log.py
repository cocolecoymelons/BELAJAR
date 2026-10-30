import logging

from logging.handlers import RotatingFileHandler

def setup_log_func(name):

  root = logging.getLogger()
  root.setLevel(logging.DEBUG)

  if root.handlers:
    
    print(root.handlers)

    return

  log_in_terminal = logging.StreamHandler()
  log_in_terminal.setLevel(logging.INFO)
  log_in_terminal.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | In file %(name)s, line %(lineno)d, %(message)s.")
  )

  file_handler = RotatingFileHandler(f"{name}.log", maxBytes=1_000_000, backupCount=3)
  file_handler.setLevel(logging.DEBUG)
  file_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | In file %(name)s, line %(lineno)d, %(message)s.")
  )

  root.addHandler(log_in_terminal)
  root.addHandler(file_handler)

  return 

  
  