import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.info("Hello from second grand child")
    logger.debug("Debug message from second grand child")
