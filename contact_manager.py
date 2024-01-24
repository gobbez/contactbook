from contact import Contact

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"Contact {name} removed."
        return f"Contact {name} not found."

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.display_contact()
        return f"Contact {name} not found."

    def list_contacts(self):
        if not self.contacts:
            return "Contact list is empty."
        return '\n'.join([contact.display_contact() for contact in self.contacts])

# Example Usage
# manager = ContactManager()
# manager.add_contact("John Doe", "123456789", "john@example.com")
# print(manager.list_contacts())
