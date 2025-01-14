class Contact_list:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def display(self):
        if not self.contacts:
            print("List is empty!")
        else:
            for contact in self.contacts:
                print(contact)

