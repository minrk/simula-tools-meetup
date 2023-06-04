import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.info("Hello from first grand child")
    logger.debug("Debug message from first grand child")
