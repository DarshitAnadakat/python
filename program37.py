import datetime

def load_data():
    data = []
    with open("birthdate.txt", "r") as file:
        for line in file:
            name, birthdate = line.strip().split(",")
            data.append((name, birthdate))
    return data

def save_data(data):
    with open("birthdate.txt", "w") as file:
        for name, birthdate in data:
            file.write(f"{name},{birthdate}\n")

def add_birthdate():
    name = input("Enter name: ")
    birthdate = input("Enter birthdate (format: yyyy-mm-dd): ")
    data.append((name, birthdate))
    save_data(data)
    print("Birthdate added successfully!")

def list_details():
    for name, birthdate in data:
        print(f"{name} ({birthdate})")

def show_today():
    today = datetime.date.today()
    today_birthdays = [name for name, birthdate in data if birthdate.endswith(today.strftime("-%m-%d"))]
    if today_birthdays:
        print("Today's Birthdays:")
        for name in today_birthdays:
            print(name)
    else:
        print("No birthdays today")


data = load_data()


show_today()


while True:
    print("Menu:")
    print("1. Add Birthdate")
    print("2. List All Details")
    print("3. Show Today's Birthdays")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_birthdate()
    elif choice == "2":
        list_details()
    elif choice == "3":
        show_today()
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again")

print("Goodbye!")
