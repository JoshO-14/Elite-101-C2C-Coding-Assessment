import random
import shipcreation
import name_of_ships as sn
import baycreation as bc

#We will be creating a space fleeting docking schedule.
#The space ships will be docked in the order of their scheduled time and the space ships with the same arrival time will be docked in the order of their size.

ships = shipcreation.ship_creation()
"""
We need to incorporate a menu for the user to do the following functions:
1. Display the ships that are incoming and the docking bays that are available.
2. Dock the ships in the bays.
3. Display the ships that are docked in the bays.
4. Remove the ships from the bays.
5. Exit the program.
"""

def menu():
    print("\nWelcome to the Space Fleet Docking Schedule!")
    print("1. Display the ships that are incoming and the docking bays that are available.")
    print("2. Dock the ships in the bays.")
    print("3. Display the ships that are docked in the bays.")
    print("4. Remove the ships from the bays.")
    print("5. Exit the program.")
    choice = input("Please enter the number of your choice: ")
    return choice



#We will display the ships that are incoming and the docking bays that are available.

def print_bays_and_ships(docking_bay, ships):
    print("\nDocking Bays: ")
    for bay in docking_bay:
        print(f"Bay {bay['bay_id']} - {bay['bay_size']} bay, Docking time: {bay['bay_dockingtime']}, Capacity: {bay['bay_capacity']}")
    print('\n')
    print("Incoming Ships: ")
    for ship in ships:
        print(f"Ship - {ship['name']}, Size - {ship['size']}, Arrival Time - {ship['arrival_time']}, Departure Time - {ship['departure_time']}")


        
def main():
    docking_bay = bc.docking_bays
    while True:
        choice = menu()
        if choice == '1':
            print_bays_and_ships(docking_bay, ships)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
       

#Now, we need to create a function that incorporates the user input to dock the ships in the bays.

main()