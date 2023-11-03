from Building import *
import csv
class Map():
    def make_buildings(self):
        read_list = []
        buildings_list= []
        # H = House, R = Restaurant, M = Movie, O = Office, W = Wind Farms, F = Farm
        legend = ["House", "Restaurant", "Movie", "Office", "Wind", "Farm"]
        with open("build.csv", 'r') as b:
            data = csv.reader(b, delimiter=',')
            for row in data:
                read_list.append(row)
        
        for i in range(len(read_list)):
            buildings_list.append(Building(str(read_list[i][0]), read_list[i][1], read_list[i][2]))
        
        building_dict = dict(zip(legend, buildings_list))
        return building_dict

    def manage_city(self, map, amount, buildings):
        # old_buildings = dict()
        current_buildings = dict()
        choice = input("Would you like to build, or demolish a building? ")
        if choice.lower() == "build":
            num_builds = int(input("How many buildings would you like to add? "))
            if num_builds >= 1:
                for _ in range(0, num_builds):
                    building = input("What building do you want to add? ")
                    change_res = buildings.get(building)
                    for k, v in buildings.items():
                        if building == k:
                            x = int(input("Type in a x-coord: "))
                            y = int(input("Type in a y-coord: "))
                            width = int(input("Type in a width for an area for 1 or more buildings: "))
                            length = int(input("Type in a length for an area for 1 or more buildings: "))
                            if (x >= 21 or y >= 21) or (x < 1 or y < 1):
                                print("Not a valid coordinate")
                                continue
                            elif width <= 0 or length <= 0:
                                print("Not a possible length")
                            elif map[y-1][x-1] != "-":
                                print("Spot already taken!")
                            elif width == 1 and length == 1:
                                amount += int(change_res.get_metal()) + int(change_res.get_wood())
                                map[y-1][x-1] = v.get_building()
                                if building not in current_buildings.keys():
                                    current_buildings[building] = list()
                                current_buildings[building].append(tuple([x, y]))
                            elif width > 1 and length > 1:
                                for i in range(length):
                                    for j in range(width):
                                        amount += int(change_res.get_metal()) + int(change_res.get_wood())
                                        map[y+i-1][x+j-1] = v.get_building()
                                        if building not in current_buildings.keys():
                                            current_buildings[building] = list()
                                        current_buildings[building].append(tuple([y+j-1, x+i+1]))
                if building == "Road":
                    x1 = int(input("Type in a starting x-coord: "))
                    y1 = int(input("Type in a starting y-coord: "))
                    x2 = int(input("Type in an ending x-coord: "))
                    y2 = int(input("Type in an ending y-coord: "))
                    # if x1 >= 1 and x2 >= 1 and y1 >= 1 and y2 >= 1:
                    if x1 <= x2 and y1 <= y2:
                        if x1 == x2 and y1 < y2:
                            for i in range(y1, y2+1):
                                amount += 400
                                map[i-1][x1-1] = "P"
                                if building not in current_buildings.keys():
                                    current_buildings[building] = list()
                                current_buildings[building].append(tuple([x1, i]))
                        elif x1 < x2 and y1 == y2:
                            for i in range(x1, x2+1):
                                map[y1-1][i-1] = "P"
                                if building not in current_buildings.keys():
                                    current_buildings[building] = list()
                                current_buildings[building].append(tuple([i, y1]))
            else:
                print("Not a valid amount")
        elif choice.lower() == "demolish":
            while True:
                x = int(input("Type in the x-coord of the building: "))
                y = int(input("Type in the y-coord of the building: "))
                location = (x, y)
                if (x >= 21 or y >= 21) or (x < 1 or y < 1):
                    print("Not a valid coordinate")
                    continue
                elif map[y-1][x-1] == "-":
                    print("Building not at that location")
                    continue
                else:
                    map[y-1][x-1] = "-"
                    change_res = buildings.get(map[y-1][x-1])
                    # for k in current_buildings.keys():
                    #     if location in current_buildings[k]:
                    #         current_buildings[k].remove(location)
                    #     old_buildings[k].append(location)
                    # print("Building demolished")
                    # print(f"Old building positions: {old_buildings}")
                    break
        else:
            print("Not a valid choice")
        print(current_buildings)
        return amount