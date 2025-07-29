"""
AI Model for Transaction Category Prediction
This module uses a Multinomial Naive Bayes classifier with CountVectorizer
to automatically categorize transaction descriptions.
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from typing import Optional

# Basic training data: pairs of (description, category)
TRAIN_DATA = [
    ("Salary for June", "Income"),
    ("Electricity bill payment", "Utilities"),
    ("Dinner at restaurant", "Food"),
    ("Bus ticket", "Transportation"),
    ("Gym membership fee", "Health"),
    ("Stock dividends", "Income"),
    ("Groceries shopping", "Food"),
]

class TransactionCategoryPredictor:
    """
    A simple machine learning model to predict the category
    of a transaction based on its description using a 
    Multinomial Naive Bayes classifier.
    """
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()
        self._train()

    def _train(self):
        """
        Train the model on predefined labeled training data.
        """
        texts, labels = zip(*TRAIN_DATA)
        X = self.vectorizer.fit_transform(texts)
        self.classifier.fit(X, labels)

    def predict(self, description: Optional[str]) -> str:
        """
        Predict the category of a given transaction description.
        If description is empty or None, return 'Other'.
        """
        if not description or not description.strip():
            return "Other"
        X_test = self.vectorizer.transform([description])
        prediction = self.classifier.predict(X_test)
        return prediction[0]

# Create a single instance of the predictor for reuse
predictor = TransactionCategoryPredictor()

def predict_category(description: Optional[str]) -> str:
    """
    Public interface for predicting a transaction category.
    """
    return predictor.predict(description)
