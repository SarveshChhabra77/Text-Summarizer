import os
import logging
from datetime import datetime


Log_file_name=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Log_dir = os.makedirs(os.getcwd(),'logs')

os.makedirs(Log_dir,exist_ok=True)

Log_file_path = os.path.join(Log_dir,Log_file_name)

logging.basicConfig(
    filename=Log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d-%(name)s-%(levelname)s-%(message)s'
)

logger = logging.getLogger('')