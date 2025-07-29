"""
Database models using SQLAlchemy for managing financial transactions.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the SQLAlchemy object (used by the Flask app)
db = SQLAlchemy()

class Transaction(db.Model):
    """
    Represents a financial transaction (either income or expense).

    Attributes:
        id (int): Unique identifier for each transaction.
        amount (decimal): The monetary amount of the transaction.
        transaction_type (str): Type of transaction ('income' or 'expense').
        category (str): Category associated with the transaction (e.g., 'Food', 'Salary').
        transaction_date (datetime): Timestamp when the transaction occurred.
        description (str): Optional text providing more context or notes.
    """
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'
    category = db.Column(db.String(50), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        """
        Returns a string representation of the transaction.
        Useful for debugging and logging purposes.
        """
        return f"<Transaction {self.id}: {self.transaction_type} {self.amount} - {self.category}>"
