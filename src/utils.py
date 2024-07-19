import logging
import os
import logging

def setup_logger(name, level=logging.INFO, log_file='data_ingestion.log',  log_dir='logs'):
    """Setup a logger with both console and file handlers.

    Args:
        name (str): The name of the logger.
        log_file (str): The filename for the log file.
        log_dir (str): The directory where the log file will be saved.
        level (int): The logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
    file_handler.setLevel(level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

