""" this file contains code for logger configuration
    python logging -> logger -> handler(s) -> formatter
"""

import logging

# setup the handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

# configure the logger
logging.basicConfig(level=logging.DEBUG, handlers=[console_handler, file_handler])

logger = logging.getLogger("testLogger")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")