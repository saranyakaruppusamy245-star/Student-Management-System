def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{dept}\n")

    print("✅ Student Added Successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("⚠ No students found!\n")
            else:
                print("\n--- Student List ---")
                for line in data:
                    roll, name, dept = line.strip().split(",")
                    print(f"Roll: {roll} | Name: {name} | Dept: {dept}")
                print()
    except FileNotFoundError:
        print("⚠ File not found! Add students first.\n")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, dept = line.strip().split(",")
                if roll == roll_no:
                    print("\n✅ Student Found!")
                    print(f"Roll: {roll} | Name: {name} | Dept: {dept}\n")
                    found = True
                    break

        if not found:
            print("❌ Student Not Found!\n")

    except FileNotFoundError:
        print("⚠ File not found! Add students first.\n")


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            deleted = False
            for line in lines:
                roll, name, dept = line.strip().split(",")
                if roll != roll_no:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("✅ Student Deleted Successfully!\n")
        else:
            print("❌ Student Not Found!\n")

    except FileNotFoundError:
        print("⚠ File not found! Add students first.\n")


# Main Program
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting... Bye 👋")
        break
    else:
        print("⚠ Invalid choice! Try again.\n")