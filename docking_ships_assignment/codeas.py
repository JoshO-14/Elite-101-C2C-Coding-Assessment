import random
from datetime import datetime
import shipcreation
import baycreation
import departed_ships

#We will be creating a space fleeting docking schedule.
#The space ships will be docked in the order of their scheduled time and the space ships with the same arrival time will be docked in the order of their size.
departed_ships = departed_ships.departed_ships
ships = shipcreation.ship_creation()
bc = baycreation
"""
We need to incorporate a menu for the user to do the following functions:
1. Display the ships that are incoming and the docking bays that are available.
2. Dock the ships in the bays.
3. Display the ships that are docked in the bays.
4. Remove the ships from the bays.
5. Exit the program.
"""
print("\nWelcome to the Space Fleet Docking Schedule!")

def menu():
    print("\nSelect an option:")
    print("\n1. Display the ships that are incoming and the docking bays that are available.")
    print("2. Dock the ships in the bays.")
    print("3.Exit the program.")
    return input("Enter your choice: ")


#We will display the ships that are incoming and the docking bays that are available.
######
def print_bays_and_ships(docking_bay, ships):
    print("\nDocking Bays: ")
    for bay in docking_bay:
        print(f"{bay['bay_name']} | Docking time: {bay['bay_shipatime']} to {bay['bay_shipdtime']}| Ships: {bay['bay_ships']}")
    print('\n')
    print("Incoming Ships: ")
    for ship in ships:
        print(f"Ship ID - {ship['id']} | Ship - {ship['name']} | Arrival Time - {ship['arrival_time']} | Departure Time - {ship['departure_time']}")
######

######
def dock_ships(docking_bay, ships):
    decision_to_display = input("Would you like to see the current bays and ships? (y/n): ")
    if decision_to_display.lower() == 'y':
        print_bays_and_ships(docking_bay, ships)

    ship_of_choice = int(input("Enter the ID of the ship you want to dock: \n"))
    dock_of_choice = input("Enter the name of the bay you want to dock the ship in: \n").lower()

    def find_ship_by_id(ship_id):
        for ship in ships:
            if ship['id'] == ship_id:
                return ship
        return None
    def find_bay_by_name(bay_name):
        for bay in docking_bay:
            if bay['bay_name'] == bay_name:
                return bay
        return None
    for ship in ships:
        if find_ship_by_id(ship_of_choice) == ship:
            for bay in docking_bay:
                if find_bay_by_name(dock_of_choice) == bay:
                    bay['bay_ships'].append(ship)
                    ships.remove(ship)
                    print(f"Ship ID - {ship['id']} has been docked in {bay['bay_name']}")
                    break
                else:
                    print("Bay not found. Please try again.")
                    break
        else:
            print("Ship ID not found. Please try again.")
            break
    return docking_bay
######

######

######
def main():
    docking_bay = bc.docking_bays
    while True:
        choice = menu()
        if choice == '1':
            print_bays_and_ships(docking_bay, ships)
        elif choice == '2':
                dock_ships(docking_bay, ships)
        elif choice == '3':
            print("Goodbye friend!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


#Now, we need to create a function that incorporates the user input to dock the ships in the bays.

