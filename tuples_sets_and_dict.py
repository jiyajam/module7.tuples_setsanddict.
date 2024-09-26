##########7.1
seasons = ("Spring", "Summer", "Autumn", "Winter")
month = int(input("Enter the  month number (1-12): "))
if month in [12, 1, 2]:
    season = seasons[0]
elif month in [3, 4, 5]:
    season = seasons[1]
elif month in [6, 7, 8]:
    season = seasons[2]
elif month in [9, 10, 11]:
    season = seasons[3]

else:
    season = "Invalid month number"
print("the season is ",season)

#############7.2
names = set()
while True:
    name = input("Enter a name or click enter to quit: ")
    if name == "":
        break
    if name in names:
        print("name already exits ")
    else:
        print("new name added")
        names.add(name)
print("list of the names entered are: ")
for name in names:
    print(name)

#########7.3

airports = {}

while True:
    print("Options:")
    print("1. Add a new airport")
    print("2. Get airport information")
    print("3. Quit")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':

        icao_code = input("Enter ICAO code: ").upper()
        airport_name = input("Enter airport name: ")
        airports[icao_code] = airport_name
        print(f"Added: {icao_code} - {airport_name}")

    elif choice == '2':
        icao_code = input("Enter ICAO code: ").upper()
        if icao_code in airports:
            print(f"{icao_code}: {airports[icao_code]}")
        else:
            print("ICAO code not found.")
    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

