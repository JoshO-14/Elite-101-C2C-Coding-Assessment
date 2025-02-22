import random
import time
import name_of_ships as sn

#We will be creating a space fleeting docking schedule.
#The space ships will be docked in the order of their scheduled time and the space ships with the same arrival time will be docked in the order of their size.
#There will be a specific code name to each space ship and the code name will be unique, while detailing the size of eah space ship.

#alpha = smallest
#beta = medium
#gamma = large
#delta = extra large

sizes = ['alpha', 'beta', 'gamma', 'delta']
arrival_time = ["6:30 AM", "7:00 AM","8:30 AM","10:30 AM","12:30 PM","2:00 PM","3:30 PM","4:00 PM","5:30 PM","6:00 PM","7:30 PM","8:00 PM","9:30 PM",]
departure_time = ["7:30 AM", "8:00 AM","8:30 AM","10:30 AM","12:30 PM","2:00 PM","3:30 PM","4:00 PM","5:30 PM","6:00 PM","7:30 PM","8:00 PM","9:30 PM",]

#We created a list of arrival times and sizes for the ships.
#We will now create a dictionary that contains the name of each ship, the arrival time and the size.

ships = []
for i in range(20): #Essentially, we are going to create a template (dictionary) for 1 ship for all the 20 ships to follow.
   
   #To prevent error of creating a single dictionary for all 20 ships, we will use the random.choices() function to randomly select the name of the ship, the arrival time and the size of the ship.
   ship = {#creating a single dictionary as a template
        'name': sn.name_of_ships[i % len(sn.name_of_ships)], #looping through the list of ship names to assign a name to each ship.
        'size': random.choice(sizes),
        'arrival_time': random.choice(arrival_time),
        'departure_time': random.choice(departure_time)
    }  
   ships.append(ship) #appending, or adding, the dictionary to the list of ships for all 20 ships to follow. 

random.shuffle(ships) #shuffling the list of ships to randomize the order of the ships.

#We have successfully created a list of dictionaries that contains a unique name of the ship, the arrival time and the size of the ship.

#We will now sort the ships based on their sizes and arrival time.

Bay_1 = []
Bay_2 = []
Bay_3 = []
Bay_4 = []
Bay_5 = []

#We created four empty lists that will be used to dock the ships based on their sizes.


#We need to sort the ships based on their arrival time.
#We will be using the sorted function to sort the ships based on their arrival time.

def get_arrival_time(ship):
    return ship['arrival_time']

#Now we will do the same for the departure time.
def get_departure_time(ship):
    return ship['departure_time']
#We created a function that will return the arrival time of each ship.

alpha_bay = sorted(alpha_bay, key=get_arrival_time)
beta_bay = sorted(beta_bay, key=get_arrival_time)
gamma_bay = sorted(gamma_bay, key=get_arrival_time)
delta_bay = sorted(delta_bay, key=get_arrival_time)

#Now, we will sort the ships based on their departure time.
alpha_bay = sorted(alpha_bay, key=get_departure_time)
beta_bay = sorted(beta_bay, key=get_departure_time) 
gamma_bay = sorted(gamma_bay, key=get_departure_time)
delta_bay = sorted(delta_bay, key=get_departure_time)

#We have successfully sorted the ships based on their arrival and departure time.
#We used the lambda function to sort the ships based on their arrival time in ascending order.

#Now, we will print the ships in each bay.
def print_ships(bay_name, bay):
    print(f"{bay_name} Bay:")
    for ship in bay:
        print(f"{ship['name']} - {ship['size']} - {ship['departure_time']} - {ship['arrival_time']}")
    print("\n")  
#We have successfully printed the ships in each bay.

#However, there are too may ships in each bay.
#We need to limit the number of ships depending on what size they are.
#alpha bay can only hold 6 ships, beta bay can only hold 5 ships, gamma bay can only hold 5 ships and delta bay can only hold 4 ships.

#We will now limit the number of ships in each bay.
alpha_bay = alpha_bay[:4]
beta_bay = beta_bay[:6]
gamma_bay = gamma_bay[:6]   
delta_bay = delta_bay[:4]

#We have successfully limited the number of ships in each bay.  
#So now, the ships that cannot be docked will be sent to the next available bay.

#We will now print the ships in each bay.
print_ships("Alpha", alpha_bay)
print_ships("Beta", beta_bay)   
print_ships("Gamma", gamma_bay)
print_ships("Delta", delta_bay)