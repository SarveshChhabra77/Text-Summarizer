from src.logging.logger import logger
from src.exceptions.exception import SummarizerException
from src.constants import DATASET_NAME,DATASET_VERSION
from datasets import load_dataset
import sys

class DataLoader:
    def load_data(self):
        try:
            
            logger.info('Loading dataset')
            
            dataset = load_dataset(
                DATASET_NAME,
                DATASET_VERSION
            )
            
            logger.info('Dataset loaded successfully')
            
            return dataset
        
        except Exception as e:
            
            raise SummarizerException(e,sys)
        
        
        
        
        
        