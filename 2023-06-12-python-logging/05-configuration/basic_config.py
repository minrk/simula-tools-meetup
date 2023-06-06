import logging

logger = logging.getLogger(__name__)


def main():
    logger.debug("A debug message!")
    logger.info("An info message!")
    logger.warning("A warning message!")
    logger.error("An error message!")
    try:
        raise Exception("An exception!")
    except Exception:
        logger.exception("An exception message!")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        # stream="sys.stdout",
        filemode="a",
        filename="example.log",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        format="[%(asctime)s] - %(levelname)s - %(message)s",
    )
    main()
