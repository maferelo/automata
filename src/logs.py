import os
import logging


def create_logger() -> logging.Logger:
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(__file__), '..', 'info.log'),
        level=logging.INFO, 
        format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    return logging.getLogger()