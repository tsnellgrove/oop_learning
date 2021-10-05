# program: dark castle v3.42
# name: Tom Snellgrove
# date: Oct 3, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
import pickle
import random
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *
from dc3_class_deff import *
import gc

def start_me_up():

		print("start_me_up start")

		### object list loaded from default_obj_pickle ###
		with open('default_obj_pickle', 'rb') as f:
				master_obj_lst = pickle.load(f)

		stateful_dict = master_obj_lst[0]
		active_gs = master_obj_lst[1]

		print("start_me_up - post-pickle load")

		#	troubleshooting
		print("start_up - pre active_gs assignments")
		for obj in gc.get_objects():
				if isinstance(obj, GameState):
						print(obj, id(obj), sys.getrefcount(obj))
				if isinstance(obj, Room):
						print(obj, id(obj), sys.getrefcount(obj))

		### Assign Random Secret Code ###
		portcullis_code = random.randint(0, 7)
		port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
		active_gs.set_dynamic_desc_dict('messy_handwriting', port_code_txt)
		
		stateful_dict['dynamic_desc_dict']['messy_handwriting'] = port_code_txt

		print("start_me_up - post actvie_gs assignments")
		for obj in gc.get_objects():
				if isinstance(obj, GameState):
						print(obj, id(obj), sys.getrefcount(obj))
				if isinstance(obj, Room):
						print(obj, id(obj), sys.getrefcount(obj))

		### introductory text ###
		buffer(stateful_dict, descript_dict["introduction"])
		buffer(stateful_dict, descript_dict["entrance"])

		### dump updated objects to save_obj_pickle ###
		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f)

		print("start_me_up - pickle dump")
		
		return stateful_dict['end_of_game'], stateful_dict['out_buff']		
