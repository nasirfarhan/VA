import os
import json

ORIGINAL_FILE = os.path.join(os.path.dirname(__file__), '../assets/player.json')
SAVE_FILE = os.path.join(os.path.dirname(__file__), "../assets/savefile.json")

PROGRESS = {}

def move(location):
    global PROGRESS
    PROGRESS["location"] = location
    print(f"You moved to {location}")

def load():
    global PROGRESS
    if not os.path.exists(SAVE_FILE):
        with open(ORIGINAL_FILE, 'r') as og:
            PROGRESS = json.load(og)
        with open(SAVE_FILE, 'w') as save:
            json.dump(PROGRESS, save, indent=4)
    else:
        with open(SAVE_FILE, 'r') as save:
            PROGRESS = json.load(save)
    print("Veins of Ashes loaded!")
         

def save():
    global PROGRESS

    with(SAVE_FILE , 'w') as save:
        json.dump(PROGRESS , save , indent=4)
    
    print("Progress saved!")


def display_skill():

    for name, details in PROGRESS["skills"].items():
        print(f"{name} - {details['type']}")






     

