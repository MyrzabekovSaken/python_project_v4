import os
import json
from collections import deque

from locations.location import Location
from actors.player import Player

MAP_FILE_PATH = "./map.json"



def search_location_in_dict(location, search_title):
    """search location in dict by title BFS"""
    
    queue = deque([location])
    while queue:
        current_location = queue.popleft()
        if current_location["title"] == search_title:
            return current_location
        queue.extend(current_location["locations"])
    return None


def get_location_from_console(location: Location):
    current_location_title = input("Enter location title: ")
    new_location_title = input("Enter new location title: ")
    new_location = Location(title=new_location_title, locations=[])
    new_player = Player(first_name="Alex", hp=100, inventory=[], attack_point=100)
    l = search_location_in_dict(location, current_location_title)
    if l:
        if "locations" not in l:
            l["locations"] = []
        l["locations"].append(new_location.to_dict())
        l["previous_location"] = current_location_title
        if "player" not in l:
            l["player"] = []
        l["player"].append(new_player.to_dict())
    else:
        raise ValueError("Location not found")

def map_maker():
    map = Location(locations=[])
    if os.path.isfile(MAP_FILE_PATH):
        with open(MAP_FILE_PATH, "r") as f:
            map = json.load(f)
            get_location_from_console(map)
        with open(MAP_FILE_PATH, "w") as f:
            json.dump(map, f, indent=2)

    else:
        with open(MAP_FILE_PATH, "w") as f:
            json.dump(map.to_dict(), f, indent=2)
