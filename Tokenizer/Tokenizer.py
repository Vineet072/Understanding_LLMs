# not supported so used a virtual environment

# python -m venv .venv
# .venv\Scripts\activate

# pip install --upgrade transformers

# TikTokenizer website can be taken for reference for better understanding

# The model I used is open access, so no need to use hugging face token :)

import os
from transformers import AutoTokenizer

modelId="google/gemma-3-1b-it"
tokenizer=AutoTokenizer.from_pretrained(modelId)
print(tokenizer("Hello goel"))