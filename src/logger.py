import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Create the log directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), 'log')
os.makedirs(log_dir, exist_ok=True)

# Define the log file path
LOG_FILE_PATH = os.path.join(log_dir, 'app.log')

# Configure logging with TimedRotatingFileHandler
handler = TimedRotatingFileHandler(LOG_FILE_PATH, when = "midnight", interval=1, backupCount=7)
handler.suffix = "%Y-%m-%d"

logging.basicConfig(
    handlers = [handler],
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

# Example log message
logging.info("This is a test log message")