import psycopg2
from db_config import DB_CONFIG
from utils import create_table_if_not_exists
from rich import print

# Function that handle delete a person using ID
def delete_record(id):
    # Checker if no table exist
    create_table_if_not_exists()
    # Create Connection and pass the configs from db_config.py
    conn = psycopg2.connect(**DB_CONFIG)
     # Create cursor to execute postgres script
    cur = conn.cursor()
    try:
        # Create Read postgres SQL Script
        query = "DELETE FROM person WHERE id = %s"
        # Execute the script. Align the values from the query
        cur.execute(query, (id))
        conn.commit()
        print("[green]Person[/green] [red]Deleted[/red] [green]Successfully[/green]")
    except Exception as error:
        print(f"[red]Error: {error}[/red]")
         # Execute rollback to undo changes
        conn.rollback()
    finally:
        # Closes the connections to avoid memory leak
        cur.close()
        conn.close()
