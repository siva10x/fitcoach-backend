from flask import Blueprint, jsonify
from app.services.db_service import test_connection

workout_bp = Blueprint("workout", __name__)

@workout_bp.route("/workout", methods=["GET"])
def get_workout():
    return jsonify({"message": "This is a sample workout route"})

@workout_bp.route("/db-test", methods=["GET"])
def db_test():
    return jsonify(test_connection())
