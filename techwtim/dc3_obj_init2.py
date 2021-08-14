# program: dark castle v3.20
# name: Tom Snellgrove
# date: Aug 6, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_classes import *


# object list loaded from pickle
with open('save_obj_pickle2', 'rb') as f:
		master_obj_lst = pickle.load(f)

# object vatiables declared / instantiated from un-pickled list
rusty_letters, dwarven_runes, messy_handwriting, dark_castle, backpack, burt, fist, conscience, alcove, control_panel, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, wooden_chest, front_gate, iron_portcullis, entrance, main_hall, antechamber, stateful_dict = master_obj_lst

