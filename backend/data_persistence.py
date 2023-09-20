
import sqlite3

def initialize_db():
    # Connect to SQLite database
    conn = sqlite3.connect('space_weather.db')
    
    # Create table for A-index data if it doesn't exist
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS a_index_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            a_index REAL,
            timestamp TEXT
        );
        """)
        
    # TODO: Implement further data persistence methods here.

if __name__ == '__main__':
    initialize_db()
