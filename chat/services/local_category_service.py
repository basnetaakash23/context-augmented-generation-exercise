from transformers import pipeline

class LocalCategoryService:
    def __init__(self):
        # Zero-shot classification pipeline using a small DistilBERT model
        self.classifier = pipeline(
            "zero-shot-classification",
            model="typeform/distilbert-base-uncased-mnli"  # small and fast
        )

        # Define your categories here
        self.labels = ["food", "travel", "tech", "weather", "finance", "health", "sports", "education", "general"]

    def classify(self, message: str) -> str:
        """
        Classify the message into one of the predefined categories.
        Returns the top predicted category.
        """
        result = self.classifier(message, self.labels)
        return result["labels"][0]  # highest scoring label
