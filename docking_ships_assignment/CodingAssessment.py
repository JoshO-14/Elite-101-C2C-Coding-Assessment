import random
import shipcreation
import baycreation

#We will be creating a space fleeting docking schedule.
#The space ships will be docked in the order of their scheduled time and the space ships with the same arrival time will be docked in the order of their size.

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
    print("3. Display the ships that are docked in the bays.")
    print("4. Exit the program.")
    return input("Enter your choice: ")


#We will display the ships that are incoming and the docking bays that are available.

def print_bays_and_ships(docking_bay, ships):
    print("\nDocking Bays: ")
    for bay in docking_bay:
        print(f"{bay['bay_name']} | Docking time: {bay['bay_dockingtime']} | Ships: {bay['bay_ships']}")
    print('\n')
    print("Incoming Ships: ")
    for ship in ships:
        print(f"Ship ID - {ship['id']} | Ship - {ship['name']} | Arrival Time - {ship['arrival_time']} | Departure Time - {ship['departure_time']}")

def dock_ships(docking_bay, ships):
    decision_to_display = input("Would you like to see the current bays and ships? (y/n): ")
    if decision_to_display.lower() == 'y':
        print_bays_and_ships(docking_bay, ships)

    ship_of_choice = int(input("\nEnter the ID of the ship you want to dock: "))
    dock_of_choice = input("Enter the name of the bay you want to dock the ship in: ")

    for bay in docking_bay:
        if dock_of_choice.lower() == bay['bay_name'].lower():
            if len(bay['bay_ships']) < bay['bay_capacity']:
                for ship in ships:
                    if ship_of_choice == ship['id']:
                        bay['bay_ships'].append(ship['name'])
                        bay['bay_ships'].append(ship['arrival_time'])
                        bay['bay_ships'].append(ship['departure_time'])
                        ships.remove(ship)
                        bay['bay_capacity'] -= 1
                        print(f"Ship {ship_of_choice} has been docked in {dock_of_choice}.")
                        return
            else:
                print("Docking bay is full.")
            return
    print("Docking bay not found.")
                    


def main():
    docking_bay = bc.docking_bays
    while True:
        choice = menu()
        if choice == '1':
            print_bays_and_ships(docking_bay, ships)
        elif choice == '2':
            dock_ships(docking_bay, ships)
        elif choice == '3':
            pass
        elif choice == '4':
            print("Goodbye friend!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


#Now, we need to create a function that incorporates the user input to dock the ships in the bays.

