# program: dark castle v3.20
# name: Tom Snellgrove
# date: Aug 6, 2021
# description: object instantiation module
# purpose: at start of main, loads obj from default pickle and saves to session save pickle

# NOTE: no longer in use but might go back to using in order to load objects from pickle once program is complete
# NOTE: could just make this an import rather than a function?

# import statements
import pickle
from dc3_classes import *

def start_me_up():
		with open('default_obj_pickle', 'rb') as f:
				master_obj_lst = pickle.load(f)

		rusty_letters, dwarven_runes, messy_handwriting, dark_castle, backpack, burt, fist, conscience, alcove, control_panel, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, wooden_chest, front_gate, iron_portcullis, entrance, main_hall, antechamber, stateful_dict = master_obj_lst

		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f)


