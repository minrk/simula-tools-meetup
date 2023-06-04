"""Historically logging in python have used the "old" printf style
for string formatting and interpolation, see 
https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
for more info.

It is of course perfectly to use the more modern f-strings or
.format strings, but note that python loggers are optimized 
for this printf (%) style, see
https://docs.python.org/3/howto/logging.html#optimization
"""
import time
import logging

logger = logging.getLogger(__name__)


def main():
    # printf style
    logger.info("What %s is it? %.5f", "time", time.time())
    logger.info("Now with %(my_arg)s arguments!", {"my_arg": "named"})

    # f-strings
    logger.info(f"What time is it? {time.time():.5f}")
    # format strings
    logger.info("Now with {my_arg} arguments!".format(**{"my_arg": "named"}))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
