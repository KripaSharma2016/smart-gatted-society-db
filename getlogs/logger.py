import logging

formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s')


file_handler = logging.FileHandler("smart-gated-society-db.log")
#file_handler.setLevel(logging.WARN)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
#console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logs = logging.getLogger()
logs.addHandler(file_handler)
logs.addHandler(console_handler)
logs.setLevel(logging.DEBUG)

"""logs.critical("Something critical")
logs.error("An error")
logs.warning("A warning")
logs.info("My info is that you are here")
logs.debug("I'm debugging")"""