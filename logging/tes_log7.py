import logging

logger = logging.getLogger("tes_log7")
logger.setLevel(logging.DEBUG)

layar = logging.StreamHandler()
layar.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

file_h = logging.FileHandler("tes_log7.log",encoding="utf-8")
file_h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

logger.addHandler(layar)
logger.addHandler(file_h)

logger.info("Halo")
logger.warning("Awas")