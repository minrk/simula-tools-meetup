import logging
import parent

logger = logging.getLogger(__name__)


def default_messages():
    """Here we simply call the do_something functions using the
    default loglevel that is set in this module"""
    logger.info("Hello from main")
    parent.first_child.do_something()
    parent.second_child.first_grand_child.do_something()
    parent.second_child.second_grand_child.do_something()


def set_first_grand_child_to_debug_v1():
    """Here we will change the loglevel on the first grand child
    of the second child by using the logger from the module directly"""
    # Set loglevel to DEBUG on first grand child
    print("-" * 40)
    logger.info("Set first grand child to DEBUG")
    parent.second_child.first_grand_child.logger.setLevel(logging.DEBUG)
    # This should now print debug message
    parent.second_child.first_grand_child.do_something()
    # This should only print info
    parent.second_child.second_grand_child.do_something()
    # Reset first child to info
    logger.info("Set first grand child to INFO")
    parent.second_child.first_grand_child.logger.setLevel(logging.INFO)
    # This should now only print info
    parent.second_child.first_grand_child.do_something()


def set_first_grand_child_to_debug_v2():
    """Here we will change the loglevel on the first grand child
    of the second child by using the namespace"""
    # Set loglevel to DEBUG on first grand child
    print("-" * 40)
    logger.info("Set first grand child to DEBUG")
    logging.getLogger("parent.second_child.first_grand_child").setLevel(logging.DEBUG)
    parent.second_child.first_grand_child.logger.setLevel(logging.DEBUG)
    # This should now print debug message
    parent.second_child.first_grand_child.do_something()
    # This should only print info
    parent.second_child.second_grand_child.do_something()
    # Reset first child to info
    logger.info("Set first grand child to INFO")
    logging.getLogger("parent.second_child.first_grand_child").setLevel(logging.DEBUG)
    # This should now only print info
    parent.second_child.first_grand_child.do_something()


def set_all_grand_children_of_second_child_to_debug():
    """Here we will change the loglevel on all the grand children
    of the second child using namespaces"""
    print("-" * 40)
    logger.info("Set all grand children of second child to DEBUG")
    logging.getLogger("parent.second_child").setLevel(logging.DEBUG)
    parent.second_child.first_grand_child.logger.setLevel(logging.DEBUG)
    # This should now print debug message
    parent.second_child.first_grand_child.do_something()
    # This should only print info
    parent.second_child.second_grand_child.do_something()


def main():
    default_messages()
    set_first_grand_child_to_debug_v1()
    set_first_grand_child_to_debug_v2()
    set_all_grand_children_of_second_child_to_debug()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
