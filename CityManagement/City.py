from Building import *
import random
from Map import *

resource_limit, initial_amount, food_resource, water_resource = 400000, 0, 0, 0
m = Map()
city_map = [['-' for x in range(25)] for i in range(25)]

buildings = m.make_buildings()

def manage_resources():
    resources = ["Water", "Food"]
    global initial_amount
    global food_resource
    global water_resource
    choose_resource = random.choice(resources)
    resource_gained = random.randint(20, 3000)
    resource_loss = random.randint(15, 2000)
    maintain = random.randint(0, 1)
    
    if maintain == 0 and choose_resource == "Water":
        initial_amount += resource_gained
        water_resource += resource_gained
        print(f"You added {resource_gained} liters of {choose_resource} to the community pantry.")
    elif maintain == 0 and choose_resource == "Food":
        initial_amount += resource_gained
        food_resource += resource_gained
        print(f"You added {resource_gained} pounds of {choose_resource} community pantry.")
    elif maintain == 1 and choose_resource == "Water":
        initial_amount -= resource_gained
        water_resource -= resource_gained
        if water_resource <= 0:
            print(f"You used {resource_loss} liters of {choose_resource}. You have no more water")
        else:
            print(f"You used {resource_loss} liters of {choose_resource}.")
    elif maintain == 1 and choose_resource == "Food":
        initial_amount -= resource_loss
        food_resource -= resource_loss
        if food_resource <= 0:
            print(f"You used {resource_loss} pounds of {choose_resource}. You have no more food")
        else:
            print(f"You used {resource_loss} pounds of {choose_resource}.")
                
if __name__ == "__main__":
    print("Welcome to the City Map Planner.\nYou can add any building to a 20x20 grid map")
    choice = True
    while choice:
        option = input("What would you like to do? ")
        if option.lower() == "quit":
            choice = False
        elif option.lower() == "manage":
            global curr_buildings
            curr_buildings = m.manage_city(city_map, initial_amount, buildings)
            # print("\nCurrent building positions: ")
            # print(f"{curr_buildings}\n")
        elif option.lower() == "map":
            for b in city_map:
                print(b)
        elif option.lower() == "resources":
            manage_resources()
            if water_resource <= 0 and food_resource <= 0:
                print(f"You have 0 liters of water and 0 lbs of food left.")
            if initial_amount < resource_limit:
                print("You still have enough resources in your city!")
            else:
                print("Resource Limit Reached!")
        elif option.lower() == "resourcecount":
            print(curr_buildings)
        
    