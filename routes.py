"""
Flask API routes for handling transaction CRUD operations.
Includes input validation, error handling, and category prediction using an AI model.
"""

from flask import request, jsonify
from models import db, Transaction
from ai_model import predict_category
from datetime import datetime

def register_routes(app):
    """
    Registers all API endpoints to the Flask app.
    """

    @app.route("/api/transactions", methods=["GET"])
    def get_transactions():
        """
        Retrieve all transactions ordered by transaction date (most recent first).
        Returns a list of transactions in JSON format.
        """
        try:
            transactions = Transaction.query.order_by(Transaction.transaction_date.desc()).all()
            results = [
                {
                    "id": t.id,
                    "amount": float(t.amount),
                    "transaction_type": t.transaction_type,
                    "category": t.category,
                    "transaction_date": t.transaction_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "description": t.description or "",
                }
                for t in transactions
            ]
            return jsonify(results), 200
        except Exception:
            return jsonify({"error": "Failed to retrieve transactions"}), 500

    @app.route("/api/transactions", methods=["POST"])
    def create_transaction():
        """
        Create a new transaction.
        Automatically predicts the category if not provided, using the AI model.
        """
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400
        
        try:
            amount = float(data.get("amount", 0))
            if amount <= 0:
                return jsonify({"error": "Amount must be a positive number"}), 400

            transaction_type = data.get("transaction_type", "").lower()
            if transaction_type not in ("income", "expense"):
                return jsonify({"error": "transaction_type must be 'income' or 'expense'"}), 400

            description = data.get("description", "").strip()
            category = data.get("category", "").strip() or predict_category(description)

            if len(category) > 50:
                return jsonify({"error": "Category name too long"}), 400

            transaction = Transaction(
                amount=amount,
                transaction_type=transaction_type,
                category=category,
                description=description,
                transaction_date=datetime.utcnow(),  # Default to UTC time
            )
            db.session.add(transaction)
            db.session.commit()

            return jsonify({"message": "Transaction created", "id": transaction.id}), 201
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid input data"}), 400
        except Exception:
            return jsonify({"error": "Failed to create transaction"}), 500

    @app.route("/api/transactions/<int:id>", methods=["PUT"])
    def update_transaction(id):
        """
        Update an existing transaction by ID.
        If the category is not provided, it is automatically predicted based on the updated description.
        """
        transaction = Transaction.query.get(id)
        if not transaction:
            return jsonify({"error": "Transaction not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400

        try:
            if "amount" in data:
                amount = float(data["amount"])
                if amount <= 0:
                    return jsonify({"error": "Amount must be a positive number"}), 400
                transaction.amount = amount

            if "transaction_type" in data:
                t_type = data["transaction_type"].lower()
                if t_type not in ("income", "expense"):
                    return jsonify({"error": "transaction_type must be 'income' or 'expense'"}), 400
                transaction.transaction_type = t_type

            if "description" in data:
                description = data["description"].strip()
                transaction.description = description
                # Predict category again if user didn’t send one
                if not data.get("category"):
                    transaction.category = predict_category(description)

            if "category" in data:
                category = data["category"].strip()
                if len(category) > 50:
                    return jsonify({"error": "Category name too long"}), 400
                transaction.category = category

            db.session.commit()
            return jsonify({"message": "Transaction updated"}), 200

        except (ValueError, TypeError):
            return jsonify({"error": "Invalid input data"}), 400
        except Exception:
            return jsonify({"error": "Failed to update transaction"}), 500

    @app.route("/api/transactions/<int:id>", methods=["DELETE"])
    def delete_transaction(id):
        """
        Delete a transaction by ID.
        """
        transaction = Transaction.query.get(id)
        if not transaction:
            return jsonify({"error": "Transaction not found"}), 404

        try:
            db.session.delete(transaction)
            db.session.commit()
            return jsonify({"message": "Transaction deleted"}), 200
        except Exception:
            return jsonify({"error": "Failed to delete transaction"}), 500
