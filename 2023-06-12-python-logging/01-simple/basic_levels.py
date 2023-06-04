"""There are 6 general logging levels which are given as integer values from
0 to 50 https://docs.python.org/3/library/logging.html#logging-levels

The most common loglevel to use is INFO which has a value of 20 (DEBUG is 10 and
WARNING is 20). Any message with a higher log level than the one set will be 
displayed.

The default loglevel will be WARNING, so in order to actually
get INFO and DEBUG messages you need to add some configuration, which
we can do with the `logging.basicConfig` method
"""

import logging

logger = logging.getLogger(__name__)


def basic_levels():
    logger.debug("This is a simple DEBUG level message.")
    logger.info("This is a simple INFO level message.")
    logger.warning("This is a simple WARNING level message.")
    logger.error("This is a simple ERROR level message.")
    logger.exception("This is an ERROR level message with exc_info.")

    try:
        raise Exception("Random exception!")
    except Exception:
        logger.exception("This is an ERROR level message with a stack trace!")

    logger.critical("This is a simple CRITICAL level message")
    logger.fatal("This is a simple FATAL level message")


def show_levels():
    for level, name in logging._levelToName.items():
        print(f"{level=} {name=}")


def main():
    show_levels()
    basic_levels()


if __name__ == "__main__":
    # See https://docs.python.org/3/library/logging.html#logging.basicConfig
    logging.basicConfig(level=logging.DEBUG)
    main()
