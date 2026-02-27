from transformers import AutoModelForSeq2SeqLM,AutoTokenizer,Trainer,TrainingArguments,DataCollatorForSeq2Seq
from src.constants import MODEL_NAME,MODEL_DIR,TOKENIZER_DIR
from src.exceptions.exception import SummarizerException
from src.logging.logger import logger
import sys
import os


class Model_Trainer:
    
    def __init__(self):
        
        try:
            
            logger.info('Loading pretrained model')
            self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
            self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)
            
        except Exception as e:
            
            raise SummarizerException(e,sys)
        
        
    def train(self,tokenized_data):
        
        try:
            
            logger.info('initializing pretrained model')
            
            os.makedirs(MODEL_DIR,exist_ok=True)
            
            training_args = TrainingArguments(
                output_dir="artifacts/results",
                learning_rate=5e-5,
                per_device_train_batch_size=2,
                num_train_epochs=1,
                weight_decay=0.01,
                logging_dir="artifacts/logs",
                logging_steps=50,
                save_strategy="epoch",
                fp16=False,
                save_total_limit=2
            )
            data_collator = DataCollatorForSeq2Seq(
                tokenizer=self.tokenizer,
                model=self.model
            )
            trainer = Trainer(
                model = self.model,
                args=training_args,
                train_dataset = tokenized_data,
                tokenizer = self.tokenizer,
                data_collator=data_collator
            )
            
            logger.info('Training Started')
            logger.info(f"Training on device: {self.model.device}")
            trainer.train()
            
            logger.info('Saving trainer model')
            trainer.save_model(MODEL_DIR)
            
            logger.info('Training complted')
            
        except Exception as e:
            
            raise SummarizerException(e,sys)



