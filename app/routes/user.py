from flask import Blueprint, jsonify, request
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["POST"])
def create_user():
    """
    Expects JSON body like:
    {
        "id": "some-user-id",
        "email": "user@gmail.com"
    }
    """
    try:
        data = request.get_json()
        user_id = data.get("id")
        email = data.get("email")

        if not user_id or not email:
            return jsonify({"error": "id and email are required"}), 400

        # Upsert into public.users
        response = supabase.table("users").upsert({
            "id": user_id,
            "email": email
        }).execute()

        return jsonify({
            "message": "User upserted successfully",
            "response": response.data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500