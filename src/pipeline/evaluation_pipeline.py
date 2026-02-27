from src.components.data_loader import DataLoader
from src.components.model_evaluation import ModelEvaluation
from src.logging.logger import logger
from src.exceptions.exception import SummarizerException
import sys


class EvaluationPipeline:
    
    def __init__(self):
        
        try:
            
            self.loader = DataLoader()
            self.evaluator = ModelEvaluation()
            
        except Exception as e:
            
            raise SummarizerException(e,sys)
        
        
    def run(self):
        
        try:
            
            logger.info('Evaluation Pipeline Started')
            
            dataset = self.loader.load_data()
            
            scores = self.evaluator.evaluate(dataset=dataset)
            
            logger.info(f'Rouge Score : {scores}')
            
            print(f'Rouge Scores : {scores}')
            
            logger.info('Evaluation Pipeline Completed Successfully')
        
        except Exception as e:
            
            raise SummarizerException(e,sys)