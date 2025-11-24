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

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    move_parser = commands.add_parser('mv')
    move_parser.set_defaults(func=move)

    look_parser = commands.add_parser('lk')
    look_parser.set_defaults(func=look)

    inventory_parser = commands.add_parser('in')
    inventory_parser.set_defaults(func=inventory)

    save_parser = commands.add_parser('sv')
    save_parser.set_defaults(func=save_progress)

    load_parser = commands.add_parser('ld')
    load_parser.set_defaults(func=load_progress)

    skill_parser = commands.add_parser('skl')
    skill_parser.set_defaults(func=display_skill)

    quit_parser = commands.add_parser('quit')
    quit_parser.set_defaults(func=quit_and_exit)

    return parser.parse_args()



def move(args):
    base.move()

def inventory(args):
     base.display_inventory()


def save_progress():
    base.save()
    
def load_progress():
    base.load()

def display_skill():
    base.display_skill()

def help():
    print("Help")

def quit_and_exit(args=None):
    print("\nYou are trying to quit the game.")

    choice = input("Do you want to save before exiting? (yes/no/cancel): ").strip().lower()

    if choice in ("yes", "y"):
        print("Saving progress...")
        base.save()         
        print("Game saved. Exiting now.")
        sys.exit(0)

    elif choice in ("no", "n"):
        print("Exiting without saving.")
        sys.exit(0)

    elif choice in ("cancel", "c"):
        print("Quit cancelled. Returning to game...")
        return  

    else:
        print("Invalid choice. Quit cancelled.")
        return


   
