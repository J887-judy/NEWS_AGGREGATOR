import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "news_aggregator.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor
