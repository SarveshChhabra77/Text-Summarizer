import os
# Dataset Constants
DATASET_NAME = "cnn_dailymail"
DATASET_VERSION = "3.0.0"


# Model Constants
TOKENIZER_MODEL_NAME = "t5-small"
MODEL_NAME = "t5-small"

# Artifact Paths
ARTIFACTS_DIR = "artifacts"
MODEL_DIR = os.path.join(ARTIFACTS_DIR,'model')
TOKENIZER_DIR = os.path.join(ARTIFACTS_DIR,'tokenizer')



