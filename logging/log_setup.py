import logging

from logging.handlers import RotatingFileHandler

def setup_logging():

  root = logging.getLogger()

  if root.handlers:

    return

  root.setLevel(logging.DEBUG)

  fmt = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")

  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  console.setFormatter(fmt)

  file_handler = RotatingFileHandler(

    "app.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    
  )

  file_handler.setLevel(logging.DEBUG)
  file_handler.setFormatter(fmt)

  root.addHandler(console)
  root.addHandler(file_handler)
