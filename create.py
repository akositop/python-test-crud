import psycopg2
from db_config import DB_CONFIG
from utils import create_table_if_not_exists
from rich import print

# Function that handle adding a person
def create_person(name, age):
    # Checker if no table exist
    create_table_if_not_exists()
    # Create Connection and pass the configs from db_config.py
    conn = psycopg2.connect(**DB_CONFIG)
    # Create cursor to execute postgres script
    cur = conn.cursor()
    try:
        # Create insert postgres SQL Script
        query = "INSERT INTO person (name, age) VALUES (%s, %s)"
        # Execute the script. Align the values from the query
        cur.execute(query, (name, age))
        conn.commit()
        print("[green]Added Person Successfully[/green]")
    except Exception as error:
        print(f"[red]Error: {error}[/red]")
        # Execute rollback to undo changes
        conn.rollback()
    finally:
        # Closes the connections to avoid memory leak
        cur.close()
        conn.close()
