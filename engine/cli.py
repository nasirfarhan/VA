import argparse
import os 
import sys
import textwrap
import subprocess
import base
import json

def main():
    args=parse_args ()
    args.func(args)

def parse_args():

    parser = argparse.ArgumentParser()

    commands= parser.add(dest='command')
    commands.required = True

    move_parser = commands.add_parser('mv')
    move_parser.set_defaults(func=move)

    look_parser = commands.add_parser('lk')
    look_parser.set_defaults(func=look)

    inventory_parser = commands.add_parser('in')
    inventory_parser.set_defaults(func=inventory)

    save_parser= commands.add_parser('sv')

    load_parser= commands.add_parser('ld')

    skill_parser = commands.add_parser('skl')

    use_skill_parser = commands.add_parser('useskl')

    help_parser = commands.add_parser('help')

    quit_parser = commands.add_parser('quit')


def move(args):
    base.move()

def inventory(args):
     player = os.path.join(os.path.dirname(__file__), '../assets/player.json')
     with open(player, 'r') as f:
      data = json.load(f)  
     for item in data["inventory"]:
         print(f'{item}')

def skill(args):
    player = os.path.join(os.path.dirname(__file__), '../assets/player.json')
    with open(player, 'r') as f:
      data = json.load(f)  
    for title, info in data["skills"].items():
        print(f"{title} -> {info['type']}")


   
