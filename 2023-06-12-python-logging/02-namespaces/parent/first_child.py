import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.info("Hello from first child")
    logger.debug("Debug message from first child")
