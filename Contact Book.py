# This is the code for Contact Book

class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))
        print("Contact added successfully.\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
            return
        print("Contact List:")
        for index, contact in enumerate(self.contacts):
            print(f"{index + 1}. {contact.name} - {contact.phone}")
        print()

    def search_contact(self):
        search = input("Enter name or phone number to search: ")
        results = [contact for contact in self.contacts if search in contact.name or search in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                self.display_contact(contact)
        else:
            print("No contacts found.\n")

    def update_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                print("Enter new details (leave blank to keep current value):")
                name = input(f"Name ({contact.name}): ")
                phone = input(f"Phone ({contact.phone}): ")
                email = input(f"Email ({contact.email}): ")
                address = input(f"Address ({contact.address}): ")

                contact.name = name if name else contact.name
                contact.phone = phone if phone else contact.phone
                contact.email = email if email else contact.email
                contact.address = address if address else contact.address

                print("Contact updated successfully.\n")
            else:
                print("Invalid contact number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    def delete_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                self.contacts.pop(index)
                print("Contact deleted successfully.\n")
            else:
                print("Invalid contact number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")
        print()

def main():
    manager = ContactManager()
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

