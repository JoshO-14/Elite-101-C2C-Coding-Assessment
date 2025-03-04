import random
from datetime import datetime
import time
import shipcreation
import baycreation
import departed_ships

#We will be creating a space fleeting docking schedule.
#The space ships will be docked in the order of their scheduled time and the space ships with the same arrival time will be docked in the order of their size.
departed_ships = departed_ships.dp_list()
ships = shipcreation.ship_creation()
bc = baycreation
current_time = '12:00AM'
current_time = datetime.strptime(current_time, "%I:%M%p")
departed_ships = departed_ships

"""
We need to incorporate a menu for the user to do the following functions:
1. Display the ships that are incoming and the docking bays that are available.
2. Dock the ships in the bays.
3. Exit the program.
"""
print("\nWelcome to the Space Fleet Docking Schedule!")

def menu():
    print("\nSelect an option:")
    print("\n1. Display the ships that are incoming and the docking bays that are available.")
    print("2. Dock the ships in the bays.")
    print("3. Check for departing ships.")
    print("4.Exit the program.")
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
`    if ship_of_choice =! str:
        print("Invalid Ship ID")`
    dock_of_choice = input("Enter the name of the bay you want to dock the ship in: \n").lower()

    def find_ship_by_id(ship_id):
        for ship in ships:
            if ship['id'] == ship_id:
                return ship
        return None
    def find_bay_by_name(bay_name):
        for bay in docking_bay:
            if bay['bay_name'].lower() == bay_name:
                return bay
        return None
    
    def ship_and_bay_time(ship, bay):
        ship_arrival_time = datetime.strptime(ship['arrival_time'], "%I:%M%p")
        ship_departure_time = datetime.strptime(ship['departure_time'], "%I:%M%p")
        bay_arrival_time = datetime.strptime(bay['bay_shipatime'], "%I:%M%p")
        bay_departure_time = datetime.strptime(bay['bay_shipdtime'], "%I:%M%p")
        
        print(f"\nShip arrival time: {ship_arrival_time}")
        print(f"Ship departure time: {ship_departure_time}")
        print(f"Bay arrival time: {bay_arrival_time}")
        print(f"Bay departure time: {bay_departure_time}\n")
        
        if bay_arrival_time <= ship_arrival_time:
            return True
        else:
            return False
        
    ship = find_ship_by_id(ship_of_choice)
    bay = find_bay_by_name(dock_of_choice)

    if ship and bay:
        if ship_and_bay_time(ship, bay):
            bay['bay_ships'].append(ship['name'])
            bay['bay_ships'].append("Arrival time: " + ship['arrival_time'])
            bay['bay_ships'].append("Departure time: " + ship['departure_time'])
            ships.remove(ship)
            print(f"{ship['name']} has been docked successfully!")
        else:
            print(f"{ship['name']} cannot be docked at this time.")
    else:
        if not ship:
            print(f"Ship with ID {ship_of_choice} not found.")
        if not bay:
            print(f"Bay with name {dock_of_choice} not found.")
        return bay
    
def check_for_departure(docking_bay):
    print("\nChecking for departing ships...")
    time.sleep(3)
    def time_confirmation():
        for bay in docking_bay:
            for ship in bay['bay_ships']:
                if ship['departure_time'] == current_time:
                    print(f"{ship['name']} has departed.")
                    bay['bay_ships'].remove(ship)
                    departed_ships.append(ship)
                    break
                else:
                   print("No ships are departing at this time.")
        
    time_confirmation()
            

                
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
            check_for_departure(docking_bay)
        elif choice == '4':
            print("Goodbye friend!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


