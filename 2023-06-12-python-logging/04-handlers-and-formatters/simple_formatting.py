"""In this example we create a logger with a stream handler and a formatter.
We then change the formatter and see that the formatting changes

Note also that since we create a separate handler, we don't need to call
the logging.basicConfig
"""
import logging


def main():
    # See https://docs.python.org/3/library/logging.html#logrecord-attributes for the different attributes
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logger.info("My current format!")

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.info("My format changed!")


if __name__ == "__main__":
    main()
