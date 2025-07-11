import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class MyAIAgent:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained("my_model")
        self.tokenizer = AutoTokenizer.from_pretrained("my_model")

    def respond(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model(inputs["input_ids"], attention_mask=inputs["attention_mask"])
        response = torch.argmax(outputs.logits)
        return response
