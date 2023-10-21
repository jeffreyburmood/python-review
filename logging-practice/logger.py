""" this file contains code for logger configuration
    python logging -> logger -> handler(s) -> formatter
"""

import logging

# setup logger and provide name
logger = logging.getLogger("testLogger")

# setup logging level
logger.setLevel(logging.DEBUG)

# setup the handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

# create the formatter (same for both handlers in this example
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s")

# add formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# configure the logger
# logging.basicConfig(
#    level=logging.DEBUG,
#    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s",
#    handlers=[console_handler, file_handler]
# )

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
