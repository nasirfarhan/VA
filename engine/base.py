import os
import json

def move(location =None):
    player = os.path.join(os.path.dirname(__file__), '../assets/player.json')

    with open(player, 'r') as f:
      data = json.load(f)  

    if location is None:
        location = data["location"]
    
    data["location"] = location

    with open (player , 'w') as f:
        json.dump(data , f , indent=4)
    
    print(f'You are now at{location}')



