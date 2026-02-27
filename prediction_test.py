from src.pipeline.prediction_pipeline import PredictionPipeline
from src.exceptions.exception import SummarizerException
from src.logging.logger import logger
import sys

if __name__=='__main__':
    
    try:
        
        pipeline = PredictionPipeline()
        
        text = """
            Artificial intelligence is transforming industries by automating tasks,
            improving decision-making, and enabling new business models.
            Companies are investing heavily in AI research and development.
            """
        summary = pipeline.run(text=text)
        
        logger.info('Summary Generated')
        
        print('Summary: ' + summary)  
    
    except Exception as e:
        
        raise SummarizerException(e,sys)      