from contact import Contact as Cn
from contact_list import Contact_list as Cl


def main():
    contact1 = Cn("John Brown", "brown@onet.pl", "555234000")
    contact2 = Cn("Anna May", "am@o2.pl", "232000199")
    contact3 = Cn("George Small", "smallg@google.pl", "222999100")
    contact4 = Cn("Paola Big", "bigpaola@poczta.pl", "100200300")
    contact_list1 = Cl()
    contact_list1.add_contact(contact1)
    contact_list1.add_contact(contact2)
    contact_list1.add_contact(contact3)
    contact_list1.add_contact(contact4)
    contact_list1.display()

if __name__ == "__main__":
    main()