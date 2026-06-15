from file_handler import load_data


def generate_report():

    volunteers = load_data()

    total_volunteers = len(volunteers)

    weekend = 0
    weekday = 0

    cities = set()

    for volunteer in volunteers:

        if volunteer["availability"].lower() == "weekend":
            weekend += 1

        elif volunteer["availability"].lower() == "weekday":
            weekday += 1

        cities.add(volunteer["city"])

    print("\n========== NayePankh Foundation Report ==========")
    print(f"Total Volunteers      : {total_volunteers}")
    print(f"Weekend Volunteers    : {weekend}")
    print(f"Weekday Volunteers    : {weekday}")
    print(f"Cities Covered        : {len(cities)}")
    print("================================================")