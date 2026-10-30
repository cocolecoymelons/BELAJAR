import logging

logger = logging.getLogger("tes_log8")
logger.setLevel(logging.DEBUG)

layar = logging.StreamHandler()
layar.setLevel(logging.INFO)
layar.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

file_h = logging.FileHandler("tes_log8.log", encoding="utf-8")
file_h.setLevel(logging.DEBUG)
file_h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

logger.addHandler(layar)
logger.addHandler(file_h)

logger.debug("Detail kecil")
logger.info("Halo")
logger.warning("Awas")