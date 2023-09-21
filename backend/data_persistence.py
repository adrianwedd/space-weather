
import sqlite3

# TODO: Add a docstring to explain the purpose of this function.

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
        
# TODO: This is a generic TODO. The exact requirements are not specified, but make sure to follow best practices and include comprehensive error-handling mechanisms. Further details will need to be discussed with the project manager or the team.

if __name__ == '__main__':
    initialize_db()
