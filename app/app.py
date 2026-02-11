import os
import time
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_PORT = int(os.getenv("DB_PORT", "5432"))

def try_db_connection(retries=10, delay=2):
    last_error = None
    for _ in range(retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            conn.close()
            return True, None
        except Exception as e:
            last_error = str(e)
            time.sleep(delay)
    return False, last_error

@app.get("/")
def home():
    ok, err = try_db_connection()
    return jsonify({
        "service": "flask-app",
        "status": "ok",
        "db_connection": ok,
        "db_error": err if not ok else None
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})
