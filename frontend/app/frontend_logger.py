# Script to configure logging for a Python application 
import os
import logging

def setup_logging(log_file='frontend-logs/app.log', log_level=logging.INFO):
    """
    Configures the logging for the application. Always creates new log file.
    
    Args:
        log_file (str): The file where logs will be written.
        log_level (int): The logging level (default is INFO).
    """   
    
    if os.path.exists(log_file):
        os.remove(log_file)
         
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    logger.info(f"Logging is set up. Logs will be written to {log_file}.")
