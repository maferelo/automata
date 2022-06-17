"""A module to set recurrent tasks."""
import os

from crontab import CronTab

from automata.logger import log_execution

JOBS = ("update", "cleanup")
LOGS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
SCRIPTS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts")


def create_command(name: str) -> str:
    """Create a command to run a script."""
    script_file_path = os.path.join(SCRIPTS_PATH, name)
    command = f"sh {script_file_path}"
    command = "; ".join(
        [f"echo Start {name}: $(date)", command, f"echo End {name}: $(date)"]
    )
    log_file_path = os.path.join(LOGS_PATH, f"{name}.log")
    command = f"({command}) >> {log_file_path} 2>&1"
    return command


def set_job(name: str, day: int, cron: CronTab) -> None:
    """Set a cronjob for arbitrary day."""
    cron_job = cron.new(command=create_command(f"{name}.sh"))
    cron_job.setall(f"* * {day} * *")


@log_execution
def reset_jobs() -> None:
    """Set the cronjobs."""
    with CronTab(user="root") as cron:
        cron.remove_all()
        for day, task in enumerate(JOBS, start=1):
            set_job(task, day, cron)
