from volunteer import *

from report import generate_report

from utils import clear_screen, pause

def menu():

    while True:

        clear_screen()

        print("=" * 45)
        print(" NayePankh Foundation Management System")
        print("=" * 45)

        print("1. Add Volunteer")
        print("2. View Volunteers")
        print("3. Search Volunteer")
        print("4. Update Volunteer")
        print("5. Delete Volunteer")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_volunteer()

        elif choice == "2":
            view_volunteers()

        elif choice == "3":
            search_volunteer()

        elif choice == "4":
            update_volunteer()

        elif choice == "5":
            delete_volunteer()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid Choice")

        pause()

menu()