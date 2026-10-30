import logging

logger = logging.getLogger("tes_log6.log")
logger.setLevel(logging.DEBUG)

layar = logging.StreamHandler()
file_h = logging.FileHandler("hasil.log")

logger.addHandler(layar)
logger.addHandler(file_h)
logger.addHandler(logging.StreamHandler())
#logger.addHandler(logging.FileHandler("hasil.log"))

print(len(logger.handlers))

logger.info("Halo")

