import random
import name_of_ships as sn

#alpha = smallest ship
#beta = medium size ship
#gamma = large ship
#delta = extra large ship

ships_name = sn.name_of_ships
random.shuffle(ships_name)
def ship_creation():

    sizes = ['alpha', 'beta', 'gamma', 'delta']
    arrival_time = ["6:30 AM", "7:00 AM","8:30 AM","10:30 AM","12:30 PM","2:00 PM","3:30 PM","4:00 PM","5:30 PM","6:00 PM"]
    departure_time = ["7:30 AM", "8:00 AM","8:30 AM","10:30 AM","12:30 PM","2:00 PM","3:30 PM","4:00 PM","5:30 PM","6:00 PM"]

    #We created a list of arrival times and sizes for the ships.
    #We will now create a dictionary that contains the name of each ship, the arrival time and the size.

    ships = []
    for i in range(10): #Essentially, we are going to create a template (dictionary) for 1 ship for all the 20 ships to follow.
    
        ship = {#creating a single dictionary as a template
            'name': ships_name[i % len(sn.name_of_ships)], #looping through the list of ship names to assign a name to each ship.
            'size': random.choice(sizes),
            'arrival_time': random.choice(arrival_time),
            'departure_time': random.choice(departure_time)
        }  
        ships.append(ship) #adding, the dictionary to the list of ships for all 20 ships to follow. 
    return ships #returning the list of ships.
    
    #We have successfully created a list of dictionaries that contains a unique name of the ship, the arrival time and the size of the ship.

