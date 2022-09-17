"""A module to configure and create the logger."""
import logging
from logging.config import dictConfig

import telegram

from automata.config import paths
from automata.config import telegram_config

telegram_bot = telegram.Bot(token=telegram_config.token)


logging_schema = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(filename)s\t%(message)s",
            "datefmt": "%d %b %y %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "level": "INFO",
            "filename": paths.log_file,
            "maxBytes": 1_000_000,  # 1 MB
            "backupCount": 4,
        },
    },
    "loggers": {
        "__main__": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "root": {"level": "INFO", "handlers": ["file"]},
}
dictConfig(logging_schema)


logger = logging.getLogger("__main__")
logger.addFilter(
    lambda record: telegram_bot.send_message(
        chat_id=telegram_config.chat_id, text=record.getMessage()
    )
)
