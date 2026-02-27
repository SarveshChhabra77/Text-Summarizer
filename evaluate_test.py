from src.pipeline.evaluation_pipeline import EvaluationPipeline
from src.exceptions.exception import SummarizerException
import sys

if __name__=='__main__':
    
    try:
        
        pipeline = EvaluationPipeline()
        pipeline.run()
        
    except Exception as e:
        raise SummarizerException(e,sys)