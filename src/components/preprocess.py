from transformers import AutoTokenizer
from src.exceptions.exception import SummarizerException
from src.logging.logger import logger
from src.constants import TOKENIZER_MODEL_NAME,TOKENIZER_DIR
import sys
import os




class Preprocess:
    
    def __init__(self):
        
        try:
            
            logger.info('Initializing Tokenizer')
            self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_MODEL_NAME)
            
        except Exception as e:
            raise SummarizerException(e,sys)
        
        
    def _tokenize_function(self,examples):
        
        try:
            inputs = ['summarize: '+article for article in examples['article']]
        
            model_inputs = self.tokenizer(
                inputs,
                max_length = 512,
                truncation = True,
                padding="max_length"
            )
            
            labels = self.tokenizer(
                examples['highlights'],
                max_length = 128,
                truncation = True
            )
            
            model_inputs['labels'] = labels['input_ids']
            
            return model_inputs
        
        except Exception as e:
            raise SummarizerException(e,sys)
        
        
    def transform(self,dataset):
        
        try:
            logger.info('Starting preprocessing')
            
            train_dataset = dataset['train'].select(range(1000))
            
            tokenized_dataset = train_dataset.map(
                self._tokenize_function,
                batched = True,
                remove_columns=train_dataset.column_names
            )
            
            logger.info('Preprocessing completed')       
            os.makedirs(TOKENIZER_DIR,exist_ok=True)
            
            self.tokenizer.save_pretrained(TOKENIZER_DIR)
            
            return tokenized_dataset
            
        except Exception as e:
            raise SummarizerException(e,sys)