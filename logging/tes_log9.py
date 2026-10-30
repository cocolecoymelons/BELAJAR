import logging

logger_a = logging.getLogger("admin")
logger_a.setLevel(logging.DEBUG)

file_admin = logging.FileHandler("admin.log", encoding="utf-8")
logger_a.addHandler(file_admin)

logger_b = logging.getLogger("edit")
logger_b.setLevel(logging.DEBUG)
logger_b.addHandler(file_admin)
#logger_b.addHandler(logging.FileHandler("edit.log", encoding="utf-8"))

#layar = logging.StreamHandler()
#logger_a.addHandler(layar)
#logger_b.addHandler(layar)

logger_a.info("Pesan dari admin")
logger_b.info("Pesan dari edit ")