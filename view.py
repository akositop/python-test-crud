import psycopg2
from db_config import DB_CONFIG
from utils import create_table_if_not_exists
from rich import print

# Function that handle viewing a specific person using ID
def view_person(id):
    # Checker if no table exist
    create_table_if_not_exists()
    # Create Connection and pass the configs from db_config.py
    conn = psycopg2.connect(**DB_CONFIG)
    # Create cursor to execute postgres script
    cur = conn.cursor()
    try:
        # Create Read postgres SQL Script with specific ID
        query = "SELECT * FROM person WHERE id= %s"
        # Execute the script. Align the values from the query
        cur.execute(query, (id))
        # Store to a variable the retrieve data
        result = cur.fetchone()
        # Add check if the person exist
        if result:
            # Destructuring the result to match the columns
            id, name, age = result
            print(f"ID: [sky_blue3]{id}[/sky_blue3]")
            print(f"Name: [sky_blue3]{name}[/sky_blue3]")
            print(f"Age: [sky_blue3]{age}[/sky_blue3]")
        else:
            print(f"[red]Person does not exist in the records[/red]")
    except Exception as error:
        print(f"[red]Error: {error}[/red]")
    finally:
        # Closes the connections to avoid memory leak
        cur.close()
        conn.close()