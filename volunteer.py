from file_handler import load_data, save_data

def add_volunteer():
    volunteers = load_data()

    print("\n----- Add New Volunteer -----")

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")
    availability = input("Enter Availability (Weekday/Weekend): ")

    volunteer = {
        "id": len(volunteers) + 1,
        "name": name,
        "age": age,
        "phone": phone,
        "city": city,
        "availability": availability
    }

    volunteers.append(volunteer)

    save_data(volunteers)

    print("\n✅ Volunteer Added Successfully!")
    
def view_volunteers():
    volunteers = load_data()

    if not volunteers:
        print("\nNo volunteers found.")
        return

    print("\n========== Volunteer List ==========")

    for volunteer in volunteers:
        print(f"\nID : {volunteer['id']}")
        print(f"Name : {volunteer['name']}")
        print(f"Age : {volunteer['age']}")
        print(f"Phone : {volunteer['phone']}")
        print(f"City : {volunteer['city']}")
        print(f"Availability : {volunteer['availability']}")
        print("-" * 35)
        
def search_volunteer():
    volunteers = load_data()

    search_name = input("\nEnter volunteer name: ").lower()

    found = False

    for volunteer in volunteers:

        if volunteer["name"].lower() == search_name:

            print("\nVolunteer Found")

            print(f"ID : {volunteer['id']}")
            print(f"Name : {volunteer['name']}")
            print(f"Age : {volunteer['age']}")
            print(f"Phone : {volunteer['phone']}")
            print(f"City : {volunteer['city']}")
            print(f"Availability : {volunteer['availability']}")

            found = True
            break

    if not found:
        print("\nVolunteer Not Found")
        
def update_volunteer():

    volunteers = load_data()

    volunteer_id = int(input("\nEnter Volunteer ID: "))

    for volunteer in volunteers:

        if volunteer["id"] == volunteer_id:

            volunteer["name"] = input("New Name: ")
            volunteer["age"] = input("New Age: ")
            volunteer["phone"] = input("New Phone: ")
            volunteer["city"] = input("New City: ")
            volunteer["availability"] = input("New Availability: ")

            save_data(volunteers)

            print("\nVolunteer Updated Successfully!")

            return

    print("\nVolunteer Not Found")
    
def delete_volunteer():

    volunteers = load_data()

    volunteer_id = int(input("\nEnter Volunteer ID: "))

    for volunteer in volunteers:

        if volunteer["id"] == volunteer_id:

            volunteers.remove(volunteer)

            save_data(volunteers)

            print("\nVolunteer Deleted Successfully!")

            return

    print("\nVolunteer Not Found")