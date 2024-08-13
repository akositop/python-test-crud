from create import create_person
from view_all import view_all_person
from view import view_person
from update import update_person
from delete import delete_record
from rich import print

def main():
    # Create loop for operation to execute user choice
    while True:
        # Display Choices
        print("\n Person Menu Operations: ")
        print("1. Create Person")
        print("2. Edit Person")
        print("3. View a Specific Person")
        print("4. View Person")
        print("5. Delete Person")
        print("6. Exit")
        
        # Assign the input to choice
        choice = input("Select operation number (1-6): ")

        # Analyze the choice and execute function the choice
        if choice == "1":
            print("CREATE PERSON:")
            name = input("Enter name: ")
            age = int(input("Enter age: "))

            # Execute create_person function to create person
            create_person(name, age)
        elif choice == "2":
            print("\n EDIT PERSON:")
            id = input("Enter person ID to update: ")
            new_name = input("Enter updated name: ")
            new_age = int(input("Enter updated age: "))

            # Execute update_person function to update person
            update_person(id, new_name, new_age)
        elif choice == "3":
            print("\n VIEW ALL PERSON:")

            # Execute view_all_person function to show all person
            view_all_person()
        elif choice == "4":
            print("\n VIEW PERSON:")
            id = input("Enter ID to view a specific person: ")

            # Execute view_all_person function to show specific person
            view_person(id)
        elif choice == "5":
            print("\n DELETE PERSON:")
            id = input("Enter ID to delete: ")

            # Execute delete_record function to delete specific person
            delete_record(id)
        elif choice == "6":
            # To exit the loop and end the program
            print("[red]Terminating the program...[/red]")
            break
        else:
            # Out of range of the choices
            print("[red]Invalid choice. Please try again.[/red]")

# Handle single file execution
if __name__ == "__main__":
    main()
