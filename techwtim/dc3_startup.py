# program: dark castle v3.20
# name: Tom Snellgrove
# date: Aug 6, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_helper import *
from dc3_static_init import *
from dc3_classes import *

def start_me_up():
		with open('default_obj_pickle', 'rb') as f:
				master_obj_lst = pickle.load(f)

		rusty_letters, dwarven_runes, messy_handwriting, dark_castle, backpack, burt, fist, conscience, alcove, control_panel, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, wooden_chest, front_gate, iron_portcullis, entrance, main_hall, antechamber, stateful_dict = master_obj_lst

		buffer(stateful_dict, descript_dict["introduction"])
		entrance.examine(stateful_dict) # can eventually replace with just desc ref?
		print(stateful_dict['out_buff'])

		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f)
