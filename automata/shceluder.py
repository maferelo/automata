"""A module to set recurrent tasks."""
from crontab import CronTab

from logger import logger


def set_tasks() -> None:
    """Set the cronjobs."""
    with CronTab(user="root", tabfile="log.tab") as cron:
        job = cron.new(command="echo hello_world")
        job.minute.every(1)

        logger.info("Cronjobs are set.")
        for line in cron.log:
            logger.info(line["pid"], " - ", line["date"])
