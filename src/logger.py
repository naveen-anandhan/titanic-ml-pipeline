import logging
import os
from datetime import datetime

# logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# daily log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(filename)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.INFO,
)

# expose logger object
logger = logging.getLogger(__name__)
