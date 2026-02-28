from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_DIR = "artifacts/model"
TOKENIZER_DIR = "artifacts/tokenizer"

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)

repo_name = "sarvesh77/text-summarizer"

model.push_to_hub(repo_name)
tokenizer.push_to_hub(repo_name)