import logging
from pathlib import Path

def setup_logger(log_file=None):
    """Configure application logging to file and console."""
    if log_file is None:
        project_dir = Path(__file__).resolve().parent.parent
        log_file = project_dir / "logs" / "automation.log"

    log_file = Path(log_file)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("email_automation")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
