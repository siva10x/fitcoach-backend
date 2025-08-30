import os
from supabase import create_client, Client
from dotenv import load_dotenv
from flask import jsonify

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def test_connection():
    try:
        response = supabase.table("users").select("*").limit(1).execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}