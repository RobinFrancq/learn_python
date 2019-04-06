import logging

# instellen van de logger (naar een file + level)
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

logging.critical("Critical")
logging.error("Error")
logging.warn("Warning") # Default log-level (dus alles eronder zie je niet in de console

# Deze zie je niet in de console (bij default level)
logging.info("Info")
logging.debug("Debug")