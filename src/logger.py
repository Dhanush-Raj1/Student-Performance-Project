import logging
import os
from datetime import datetime

log_folder_name=f"{datetime.now().strftime('%m_%d_%Y')}"
logs_path=os.path.join(os.getcwd(), "logs", log_folder_name)
os.makedirs(logs_path, exist_ok=True)

log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_FILE_PATH=os.path.join(logs_path, log_file_name)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO )


if __name__=="__main__":
    logging.info("Logging has started hell yeah!!!")
     