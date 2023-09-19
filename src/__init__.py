
import logging
import os,sys
from datetime import datetime

LOG_DIR='logs1'
LOG_DIR=os.path.join(os.getcwd(),"logs1")
os.makedirs(LOG_DIR,exist_ok=True)

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name=f"logs_{CURRENT_TIME_STAMP}.logs"
log_file_path=os.path.join(LOG_DIR,file_name)

logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO )