from src.pipeline.train_pipeline import TrainingPipeline
from src.exceptions.exception import SummarizerException
import sys

if __name__=='__main__':
    
    try:
        
        pipeline = TrainingPipeline()
        pipeline.run()
        
    except Exception as e:
        raise SummarizerException(e,sys)