"""A module to set recurrent tasks."""
from crontab import CronTab


def set_tasks() -> None:
    """Set the cronjobs."""
    with CronTab(user="root") as cron:
        job = cron.new(command="echo hello_world")
        # cron = Crontab()
        # cron.add("* * * * *", "python3 /home/pi/src/app.py")
        # cron.write()
        job.minute.every(1)
