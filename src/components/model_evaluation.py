from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
import evaluate
import torch
from src.exceptions.exception import SummarizerException
from src.logging.logger import logger
from src.constants import MODEL_DIR,TOKENIZER_DIR
import sys



class ModelEvaluation:
    
    def __init__(self):
        
        try:
            
            logger.info('Loading model for evaluation')
            
            self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)
            self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)
            self.rouge = evaluate.load('rouge')
            self.device = torch.device(
                "cuda" if torch.cuda.is_available() else "cpu"
            )
            self.model.to(self.device)
        
        except Exception as e:
            
            raise SummarizerException(e,sys)
        
        
    def evaluate(self,dataset,num_samples=50):
        
        try:
            
            logger.info('Starting evaluation')
            
            predictions = []
            references = []
            
            test_dataset = dataset['test'].select(range(num_samples))
            
            self.model.eval()
            
            with torch.no_grad():
                for sample in test_dataset:
                        
                    inputs = self.tokenizer(
                        'summarize: '+sample['article'],
                        max_length=512,
                        truncation=True,
                        return_tensors="pt"
                    ).to(self.device)
                    
                    outputs = self.model.generate(
                        inputs['input_ids'],
                        max_length = 50,
                        num_beams = 4,
                        early_stopping = True
                    )
                    
                    summary = self.tokenizer.decode(outputs[0],skip_special_tokens=True)
                    
                    predictions.append(summary)
                    references.append(sample["highlights"])
            
                
            scores = self.rouge.compute(
                    predictions=predictions,
                    references = references,
                    use_stemmer=True
                )
                
            logger.info("Evaluation completed")
                
            return scores
            
        
        except Exception as e:
            
            raise SummarizerException(e,sys)
