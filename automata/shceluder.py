"""A module to set recurrent tasks."""
import os

from crontab import CronTab

from logger import log_execution

JOBS = ("update", "cleanup")
LOG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "logs", "cron.log"
)
SCRIPTS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts")


def create_command(script: str) -> str:
    """Create a command to run a script."""
    script_file_path = os.path.join(SCRIPTS_PATH, script)
    return f"sh {script_file_path} >> {LOG_FILE_PATH} 2>&1"


def set_job(job: str, day: int, cron: CronTab) -> None:
    """Set a cronjob for arbitrary day."""
    cron_job = cron.new(command=create_command(f"{job}.sh"))
    cron_job.setall(f"* * {day} * *")


@log_execution
def reset_jobs() -> None:
    """Set the cronjobs."""
    with CronTab(user="root") as cron:
        cron.remove_all()
        for day, task in enumerate(JOBS, start=1):
            set_job(task, day, cron)
