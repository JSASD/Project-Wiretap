import csv
import math
import random

class Phantom:
    def read_csv_to_campus(file_name):
        campus = {}
        with open(file_name, mode ='r') as file:
            csvFile = csv.DictReader(file)
            
            for lines in csvFile:
                building = lines['Building']
                room = lines['Room']
                extension = lines['Extension']
                
                wing = room[0]
                floor = room[1]
                
                if building not in campus:
                    campus[building] = {}
                if wing not in campus[building]:
                    campus[building][wing] = {}
                if floor not in campus[building][wing]:
                    campus[building][wing][floor] = {}
                
                campus[building][wing][floor][room] = extension

        return campus

    def select_phones(campus, percentage):
        selected_phones = {}
        
        for building_name, building in campus.items():
            selected_phones[building_name] = {}
            
            for wing, floors in building.items():
                selected_phones[building_name][wing] = {}
                
                for floor, rooms in floors.items():
                    num_rooms = len(rooms)
                    num_to_select = math.ceil(num_rooms * percentage)
                    
                    available_rooms = list(rooms.keys())
                    selected_phones[building_name][wing][floor] = []
                    
                    for i in range(num_to_select):
                        target_idx = random.randint(0, len(available_rooms) - 1)
                        selected_room = available_rooms.pop(target_idx)
                        selected_extension = rooms[selected_room]
                        
                        selected_phones[building_name][wing][floor].append(selected_extension)
                        
        return selected_phones

    # Read the campus configuration from the CSV
    campus = read_csv_to_campus("campus_rooms.csv")

    # Test the function
    selected_10_percent = select_phones(campus, 0.1)
    print("With 10% rule:", selected_10_percent)
