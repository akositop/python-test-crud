import psycopg2
from db_config import DB_CONFIG
from utils import create_table_if_not_exists
from rich import print

# Function that handle updating a person
def update_person(person_id, update_name, update_age):
    # Checker if no table exist
    create_table_if_not_exists()
    # Create Connection and pass the configs from db_config.py
    conn = psycopg2.connect(**DB_CONFIG)
    # Create cursor to execute postgres script
    cur = conn.cursor()
    try:
        # Create update postgres SQL Script
        query = "UPDATE person SET name = %s, age = %s WHERE id = %s"
        # Execute the script. Align the values from the query
        cur.execute(query, (update_name, update_age, person_id))
        conn.commit()
        print(f"[green]Uodated { update_name } Successfully[/green]")
    except Exception as error:
        print(f"[red]Error: {error}[/red]")
        # Execute rollback to undo changes
        conn.rollback()
    finally:
        # Closes the connections to avoid memory leak
        cur.close()
        conn.close()
