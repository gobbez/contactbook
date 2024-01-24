from contact_manager import ContactManager

def main_menu():
    print("Contact Book Application")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    manager = ContactManager()

    while True:
        user_choice = main_menu()

        if user_choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)

        elif user_choice == '2':
            print(manager.list_contacts())

        elif user_choice == '3':
            name = input("Enter the name to search: ")
            print(manager.search_contact(name))

        elif user_choice == '4':
            name = input("Enter the name to delete: ")
            print(manager.remove_contact(name))

        elif user_choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
