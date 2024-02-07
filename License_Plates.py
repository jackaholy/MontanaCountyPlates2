import sys

# Dictionary to store county data
county_data = {}


def read_file(file):
    try:
        # Open the designated file
        with open(file, 'r') as file:
            for line in file:
                # Split the line by the comma
                info = line.strip().split(',')
                # Assign the proper county info to the dictionary
                county_name = info[0]
                county_seat = info[1]
                county_number = info[2]
                # Store the county information in the dictionary
                county_data[county_seat] = (county_name, county_number)

    except FileNotFoundError:
        print(f"Error: The file '{file}' cannot be found.")
    except IOError:
        print(f"Error: Unable to read the file '{file}'.")


def choose_county_name():
    while True:
        chosen_city = input("Please enter a Montana county name (enter 'quit' to exit): ")
        # If the number matches a key in the dictionary get the data from that entry
        if chosen_city in county_data:
            county_info = county_data[chosen_city]
            print(f"County Number: {chosen_city}\n"
                  f"County Name: {county_info[1]}\n"
                  f"County Seat: {county_info[0]}")
        # If they type 'quit', exit the program
        elif chosen_city.lower() == "quit":
            sys.exit(0)
        elif chosen_city not in county_data:
            print("Invalid county name.")
        else:
            print("Invalid input.")


def main():
    read_file("MontanaCounties.csv")
    choose_county_name()


if __name__ == "__main__":
    main()
