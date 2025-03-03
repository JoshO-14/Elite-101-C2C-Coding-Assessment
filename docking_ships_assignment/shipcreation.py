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
    arrival_time = ["6:00AM", "6:30AM", "7:00AM","8:30AM","10:30AM","12:30PM","2:00PM","3:30PM","4:00PM","5:00PM","6:00PM", "6:30PM", "7:00PM","8:30PM","10:30PM","12:30AM","2:00AM","3:30AM","4:00AM","5:00AM"]
    departure_time = ["7:30AM", "8:00AM","8:30AM","10:30AM","12:30PM","2:00PM","3:30PM","4:00PM","5:00PM","6:00PM", "6:30PM", "7:00PM","8:30PM","10:30PM","12:30AM","2:00AM","3:30AM","4:00AM","5:00AM","6:00AM"]
    #We created a list of arrival times and sizes for the ships.
    #We will now create a dictionary that contains the name of each ship, the arrival time and the size.

    ships = []
    for i in range(10): #Essentially, we are going to create a template (dictionary) for 1 ship for all the 20 ships to follow.
    
        ship = {#creating a single dictionary as a template
            'id': random.randint(1,1000),
            'name': ships_name[i % len(sn.name_of_ships)], #looping through the list of ship names to assign a name to each ship.
            'size': random.choice(sizes),
            'arrival_time': random.choice(arrival_time),
            'departure_time': random.choice(departure_time)
        }  
        ships.append(ship) #adding, the dictionary to the list of ships for all 20 ships to follow. 
    return ships #returning the list of ships.
    
    #We have successfully created a list of dictionaries that contains a unique name of the ship, the arrival time and the size of the ship.

