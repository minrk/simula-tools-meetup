"""In this example we create a logger with two different handlers,
one stream handler for logging to the console and one file handler
for logging to a file. We also give the two handlers different formatters
and loglevels.
"""
import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.warning("Something bad happened")
    logger.debug("Something not important happened")


def main():
    stream_formatter = logging.Formatter("%(levelname)s - %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)

    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(name)s - %(funcName)s - %(message)s"
    )
    file_handler = logging.FileHandler(filename="example.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.info("Hello from main")
    logger.warning("Another message from main")
    do_something()


if __name__ == "__main__":
    main()
