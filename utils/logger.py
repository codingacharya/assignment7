# utils/logger.py

import logging

from config.settings import (
    LOG_FILE,
    LOG_LEVEL
)


def setup_logger():

    logging.basicConfig(
        filename=LOG_FILE,
        level=getattr(logging, LOG_LEVEL),
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )

    return logging.getLogger(
        "ComplaintResponder"
    )


logger = setup_logger()