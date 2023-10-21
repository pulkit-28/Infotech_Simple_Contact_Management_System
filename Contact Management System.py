
contacts = {}


def load_contacts():
    global contacts
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts[name] = (phone, email)
    except FileNotFoundError:
        print("No contacts file found.")


def save_contacts():
    global contacts
    with open("contacts.txt", "w") as f:
        for name in contacts:
            phone, email = contacts[name]
            f.write(f"{name},{phone},{email}\n")


def add_contact():
    global contacts
    name = input("Enter the name of the contact: ")
    if name in contacts:
        print("This contact already exists.")
    else:
        phone = input("Enter the phone number of the contact: ")
        email = input("Enter the email address of the contact: ")
        contacts[name] = (phone, email)
        print("Contact added successfully.")


def view_contacts():
    global contacts
    if contacts:
        print("Here is your contact list:")
        for name in contacts:
            phone, email = contacts[name]
            print(f"{name}: {phone}, {email}")
    else:
        print("You have no contacts.")


def edit_contact():
    global contacts
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone, email = contacts[name]
        print(f"Current contact information: {name}: {phone}, {email}")
        new_phone = input("Enter the new phone number or press enter to keep the same: ")
        new_email = input("Enter the new email address or press enter to keep the same: ")
        if new_phone:
            phone = new_phone
        if new_email:
            email = new_email
        contacts[name] = (phone, email)
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")


def delete_contact():
    global contacts
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")


def get_choice():
    print("\nWelcome to your contact manager. Please choose an option:")
    print("1. Add a new contact")
    print("2. View your contact list")
    print("3. Edit an existing contact")
    print("4. Delete a contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    load_contacts()
    while True:
        choice = get_choice()
        if choice == "1":
            add_contact()
            save_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
            save_contacts()
        elif choice == "4":
            delete_contact()
            save_contacts()
        elif choice == "5":
            print("Thank you for using your contact manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()