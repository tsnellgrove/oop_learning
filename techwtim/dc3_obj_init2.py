# program: dark castle v3.11
# name: Tom Snellgrove
# date: July 29, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_classes import *

# Import the os module - current working dir code
import os

with open('save_obj_pickle2', 'rb') as f:
		master_obj_lst = pickle.load(f)

rusty_letters, dwarven_runes, dark_castle, backpack, burt, fist, conscience, rusty_key, shiny_sword, brass_key, bubbly_potion, wooden_chest, front_gate, entrance, main_hall, stateful_dict = master_obj_lst

## print(stateful_dict)

print("This is dc3_obj_init2")

# Get the current working directory - troubleshooting
cwd = os.getcwd()

# Print the current working directory - troubleshooting
print("Current working directory: {0}".format(cwd))
