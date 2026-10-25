import logging

logging.basicConfig(
  level=logging.DEBUG,
  format='%(levelname)s - %(asctime)s - %(message)s',
  datefmt='%Y %m %d, %H:%M:%S',
  filename='tes_log3.py.log',
  filemode='a'
)

logging.debug("Tes log 3, ini adalah syntax umum logging.")