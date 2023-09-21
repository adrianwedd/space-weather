
import sqlite3  # Documentation: Please describe the functionality in detail.

# TODO: Add a docstring to explain the purpose of this function.  # Updated TODO: Please elaborate on the implementation details.

def initialize_db():  # Documentation: Please describe the functionality in detail.
    # Connect to SQLite database
    conn = sqlite3.connect('space_weather.db')
    
# Create table for A-index data if it doesn't exist  # Documentation: Please describe the functionality in detail.
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS a_index_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            a_index REAL,
            timestamp TEXT
        );
        """)
        
# TODO: This is a generic TODO. The exact requirements are not specified, but make sure to follow best practices and include comprehensive error-handling mechanisms. Further details will need to be discussed with the project manager or the team.  # Updated TODO: Please elaborate on the implementation details.

if __name__ == '__main__':  # Documentation: Please describe the functionality in detail.
    initialize_db()
