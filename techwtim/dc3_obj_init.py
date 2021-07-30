# program: dark castle v3.11
# name: Tom Snellgrove
# date: July 29, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_classes import *

with open('default_obj_pickle', 'rb') as f:
		master_obj_lst = pickle.load(f)

rusty_letters, dwarven_runes, dark_castle, backpack, burt, fist, conscience, rusty_key, shiny_sword, brass_key, bubbly_potion, wooden_chest, front_gate, entrance, main_hall, stateful_dict = master_obj_lst

print(stateful_dict)
