import logging

logging.basicConfig(
  level=logging.DEBUG,
  filename='tes_log4.py.log',
  filemode='a',
  format='[{asctime}]: [{levelname}-8] On file [{filename}] occured an error on line [{lineno}] : {message}. # {process} - {threadName}',
  datefmt='%Y %m %d, %H:%M:%S',
  style='{',
  force=True,
  encoding='utf-8'
)

logging.debug("Ini adalah tes_log4 dengan format dan isi basicConfig yang lain.")