"""Create cronjobs for the application."""
from crontab import Crontab


def set_tasks():
    """Set the cronjobs."""
    with Crontab(user="root") as cron:
        job = cron.new(command="echo hello_world")
        # cron = Crontab()
        # cron.add("* * * * *", "python3 /home/pi/src/app.py")
        # cron.write()
        job.minute.every(1)

    print("cron.write() was just executed")
