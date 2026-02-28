from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
from src.logging.logger import logger
from src.exceptions.exception import SummarizerException
import sys

from src.constants import MODEL_DIR,TOKENIZER_DIR

# MODEL_NAME = 'sarvesh77/text-summarizer'

class PredictionPipeline:
    
    def __init__(self):
        
        try:
            
            logger.info('Loading trained model for predictions')
            
            self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)
            self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)
            
        except Exception as e:
            
            raise SummarizerException(e,sys)
    
    def run(self,text:str):
        
        try:
            
            logger.info('Generating summary')
            
            inputs = self.tokenizer(
                'summary: '+ text,
                max_length = 512,
                truncation = True,
                return_tensors = 'pt'
            )
            
            outputs = self.model.generate(
                inputs['input_ids'],
                max_length=50,
                num_beams = 4,
                early_stopping = True
            )
            
            summary = self.tokenizer.decode(
                outputs[0],
                skip_special_tokens = True
            )
            
            return summary
        
        except Exception as e:
            
            raise SummarizerException(e,sys)