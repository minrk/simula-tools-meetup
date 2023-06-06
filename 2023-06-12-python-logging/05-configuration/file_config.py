from pathlib import Path
import logging
from logging import config as logging_config


here = Path(__file__).absolute().parent


def main():
    logging_config.fileConfig(here / "config.ini")
    logger = logging.getLogger(__name__)
    logger.info("Hey, that was easy.")

    app_logger = logging.getLogger("app")
    app_logger.info("Hey, that was also easy.")


if __name__ == "__main__":
    main()
