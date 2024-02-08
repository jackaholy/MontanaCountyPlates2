"""
Created on Feb. 7. 2024

This file is the python script where you run the actual program. This script opens a csv file containing
a list of Montana counties alongside the county city seat, and the license plate prefix number. The user
can search through the list by city names, and have returned to them name of the county in which it is located,
and the license plate prefix number.

If the user tries entering a city that is not in the csv file they can choose to add it by entering the country
number in which it is located.

@author: jackholy
"""

import sys
import csv

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


# This code was acquired with help from chat.openai.com
def save_county_data_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for city, county_info in county_data.items():
            writer.writerow([city, county_info[0], county_info[1]])


def choose_county_seat():
    while True:
        chosen_city = input("Please enter a Montana city name (enter 'quit' to exit): ")
        # If the number matches a key in the dictionary get the data from that entry
        if chosen_city in county_data:
            county_info = county_data[chosen_city]
            print(f"City: {chosen_city}\n"
                  f"County Name: {county_info[0]}\n"
                  f"County Number: {county_info[1]}")
        # If they type 'quit', exit the program
        elif chosen_city.lower() == "quit":
            sys.exit(0)
        # If the city doesn't exist ask the user if they want to add it as a new city
        elif chosen_city not in county_data:
            enter_new_city = input("\nCity not found. Do you store as new City? (enter 'yes' to continue): ")
            # If the user chooses to add the new city...
            if enter_new_city.lower() == "yes":
                new_county_number = input(f"Please enter County Number where '{chosen_city}' is located: ")
                # Check if the county number exists.
                for county_seat, (county_name,  # This line was acquired with help from chat.openai.com
                                  existing_county_number) in county_data.items():
                    if new_county_number == existing_county_number:
                        # Get the appropriate county name from the county number
                        county_data[chosen_city] = (county_name, new_county_number)
                        save_county_data_to_csv('MontanaCounties.csv')  # Save the updated data
                        # Show the user the new information about their Montana city
                        print("New city saved successfully!\n"
                              f"New City Name: {chosen_city}\n"
                              f"County Name: {county_name}\n"
                              f"County Seat City: {county_seat}\n"
                              f"County Number: {new_county_number}")
                        break
                else:
                    print(f"'{new_county_number}' is not a valid county number...")
        else:
            print("Invalid input.")


def main():
    read_file("MontanaCounties.csv")
    choose_county_seat()


if __name__ == "__main__":
    main()
