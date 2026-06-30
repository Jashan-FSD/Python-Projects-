import csv
import os

filename = input("Enter the file name: ") # students.csv

# Create file if it does not exist
if not os.path.exists(filename):
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Marks"])
    file.close()
    print("Since file is not found! A new file is created instead.")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice -> ")

    # Add Student
    if choice == "1":

        roll = input("Enter Roll No: ")

        # Check if Roll No already exists
        file = open(filename, "r")
        reader = csv.reader(file)

        found = False
        next(reader)  # Skip header

        for row in reader:
            if row[0] == roll:
                found = True
                break

        file.close()

        if found:
            print("Roll No already exists! Please enter a unique Roll No.")
        else:
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")

            file = open(filename, "a", newline="")
            writer = csv.writer(file)
            writer.writerow([roll, name, marks])
            file.close()

            print("Student Added Successfully!")

    # Search Student
    elif choice == "2":
        roll = input("Enter Roll No to Search -> ")

        file = open(filename, "r")
        reader = csv.reader(file)

        found = False

        next(reader)

        for row in reader:
            if row[0] == roll:
                print("\n-----Student Found-----")
                print("Roll No :", row[0])
                print("Name    :", row[1])
                print("Marks   :", row[2])
                print("-------------------------")
                found = True
                break

        if not found:
            print("Student Not Found!")

        file.close()

    # Delete Student
    elif choice == "3":
        roll = input("Enter Roll No to Delete -> ")

        rows = []

        file = open(filename, "r")
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 0 and row[0] != roll:
                rows.append(row)

        file.close()

        file = open(filename, "w", newline="")
        writer = csv.writer(file)
        writer.writerows(rows)
        file.close()

        print("Student Deleted Successfully!")

    # Display Students
    elif choice == "4":
        file = open(filename, "r")
        reader = csv.reader(file)

        next(reader)

        print("\n----- Student Records -----")

        for row in reader:
            print("Roll No :", row[0])
            print("Name    :", row[1])
            print("Marks   :", row[2])
            print("-------------------------")

        file.close()

    # Exit
    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")