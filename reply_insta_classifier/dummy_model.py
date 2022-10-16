from transformers import pipeline

class Dummy_text_classifier:

    def __init__(self) -> None:
        self.classifier = pipeline("text-classification", model = "textattack/distilbert-base-uncased-CoLA")

    def classify_text(self, input: str) -> dict:
        return self.classifier(input)
