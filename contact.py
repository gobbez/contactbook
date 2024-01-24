class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display_contact(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
