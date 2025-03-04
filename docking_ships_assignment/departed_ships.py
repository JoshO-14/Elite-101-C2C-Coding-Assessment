from datetime import datetime


def current_time():
    current_time = '12:00AM'
    return datetime.strptime(current_time, "%I:%M%p")

def dp_list():
    departed_ships = []