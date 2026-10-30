import logging

induk = logging.getLogger("Admin")
induk.setLevel(logging.DEBUG)
induk.addHandler(logging.FileHandler("admin.log", encoding="utf-8"))

anak = logging.getLogger("Admin.Edit")
anak.setLevel(logging.DEBUG)
anak.propagate = False
anak.addHandler(logging.FileHandler("edit.log", encoding="utf-8"))

induk.info("pesan dari induk")
anak.info("pesan dari anak")