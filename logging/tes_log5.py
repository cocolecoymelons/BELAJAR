import logging

logger = logging.getLogger("A")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
logger.addHandler(handler)

logger.info("Halo")