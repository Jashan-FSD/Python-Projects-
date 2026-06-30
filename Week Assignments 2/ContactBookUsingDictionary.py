# Contact Book using Dictionary

contacts = {}

while True:
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        if len(phone) == 10:
            contacts[name] = phone
            print("Contact Added Successfully!")
        elif len(phone) > 10 or len(phone) < 10:
            print("Invalid Number ! The Total length should be in 10 digit.")

    elif choice == "2":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "3":
        name = input("Enter Name to Update: ")

        if name in contacts:
            new_phone = input("Enter New Phone Number: ")
            contacts[name] = new_phone
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        if len(contacts) == 0:
            print("Contact Book is Empty!")
        else:
            print("\n-----All Contacts-----")
            for name, phone in contacts.items():
                print(name, ":", phone)
            print("-----------------------")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Enter 1 to 6.")