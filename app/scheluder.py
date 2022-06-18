"""A module to set recurrent tasks using cronjobs."""
from pathlib import Path

from crontab import CronTab

from app.config import paths
from app.logger import logger
from app.utils import log_start_and_finish_decorator


def add_logging_and_timestamps_to_command(script_file_path: Path, name: str) -> str:
    """Add start and finish timestamp logs to a bash script."""
    timestamp_command = ";".join(
        (
            f"echo Start {name}: $(date)",
            f"sh {script_file_path}",
            f"echo End {name}: $(date)",
        )
    )
    return f"({timestamp_command}) >> {paths.log_file_path} 2>&1"  # output to log file


def create_command(name: str) -> str:
    """Create a command to run and log the script in bash if exists."""
    script_file_path = paths.scripts_path / f"{name}.sh"
    if script_file_path.exists() is False:
        logger.error("Script file %s does not exist.", script_file_path)
        return ""
    return add_logging_and_timestamps_to_command(script_file_path, name)


def set_job(day: int, name: str, crontab_session: CronTab) -> None:
    """Set a cronjob for an arbitrary day at 00:00 a.m."""
    command = create_command(name)
    if command == "":
        return
    cron_job = crontab_session.new(command=command)
    cron_job.setall(f"0 0 {day} * *")


@log_start_and_finish_decorator(logger)
def reset_jobs() -> None:
    """Reset the cronjobs to run daily from start of month."""
    with CronTab(user="root") as crontab_session:
        crontab_session.remove_all()
        for day, name in enumerate(paths.scheluder_scripts, start=1):
            set_job(day, name, crontab_session)
