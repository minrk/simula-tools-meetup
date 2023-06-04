import logging
import family


logger = logging.getLogger(__name__)


def default_messages():
    """Here we simply call the do_something functions using the
    default loglevel that is set in this module"""
    logger.info("Hello from main")
    family.parent.first_child.do_something()
    family.parent.second_child.first_grand_child.do_something()
    family.parent.second_child.second_grand_child.do_something()


def family_debug():
    """Here we set the loglevel to DEBUG for the whole
    family package"""
    print("-" * 40)
    logger.info("Hello from main")
    logging.getLogger("family").setLevel(logging.DEBUG)
    family.parent.first_child.do_something()
    family.parent.second_child.first_grand_child.do_something()
    family.parent.second_child.second_grand_child.do_something()


def main():
    default_messages()
    family_debug()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
