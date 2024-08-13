# Helper functions

import psycopg2
from db_config import DB_CONFIG
from rich import print

# Helper function that checks if the table already exist
def create_table_if_not_exists():
    # Create Connection and pass the configs from db_config.py
    conn = psycopg2.connect(**DB_CONFIG)
    # Create cursor to execute postgres script
    cur = conn.cursor()
    try:
        # Create Read postgres SQL Script
        query = '''
        CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
        '''
         # Execute the script. Align the values from the query
        cur.execute(query)
        conn.commit()
    except Exception as error:
        print(f"[red]Error: {error}[/red]")
        conn.rollback()
    finally:
        # Closes the connections to avoid memory leak
        cur.close()
        conn.close()
