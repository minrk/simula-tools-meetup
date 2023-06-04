"""In stead of actually creating a logger it is also possible to
use the ROOT logger by calling the the methods on the logging
module directly.
"""

import logging


def main():
    logging.debug("This is a simple DEBUG level message.")
    logging.info("This is a simple INFO level message.")
    logging.warning("This is a simple WARNING level message.")
    logging.error("This is a simple ERROR level message.")
    logging.exception("This is an ERROR level message with exc_info.")

    try:
        raise Exception("Random exception!")
    except Exception:
        logging.exception("This is an ERROR level message with a stack trace!")

    logging.critical("This is a simple CRITICAL level message")
    logging.fatal("This is a simple FATAL level message")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
