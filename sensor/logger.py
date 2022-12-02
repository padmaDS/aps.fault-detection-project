
import logging
import os
from datetime import datatime
import os

LOG_FILE_NAME =f"{datatime.now().strftime('%m%d%y_%H_%M_%S')}.log"

LOG_FILE_DTR =os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_FILE_DTR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FILE_DTR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[(%asctime)s ], %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,



)