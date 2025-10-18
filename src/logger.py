import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO # Log messages at INFO level and above (INFO, WARNING, ERROR, CRITICAL) will be shown
)

def get_logger(name):
    """
    Retrieves a logger instance with the specified name and sets its logging level to INFO.
    This allows for separate loggers to be used across different modules or components,
    all writing to the same log file as configured in the root logger.
    
    Args:
        name (str): The name of the logger to retrieve.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger