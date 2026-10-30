import logging

root = logging.getLogger()
admin = logging.getLogger("admin")

#print(root.name, root.level, root.handlers)
#print(admin.name, admin.level, admin.handlers)

#admin.info("ini info")
#admin.warning("Ini warning")
root.warning("ini warning dari root.")