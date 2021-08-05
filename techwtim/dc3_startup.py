# program: dark castle v3.11
# name: Tom Snellgrove
# date: July 29, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_helper import *
from dc3_static_init import *
from dc3_classes import *


# Import the os module - current working dir code
import os




def start_me_up():
		with open('default_obj_pickle', 'rb') as f:
				master_obj_lst = pickle.load(f)

		rusty_letters, dwarven_runes, dark_castle, backpack, burt, fist, conscience, rusty_key, shiny_sword, brass_key, bubbly_potion, wooden_chest, front_gate, entrance, main_hall, stateful_dict = master_obj_lst

		buffer(stateful_dict, descript_dict["introduction"])
		entrance.examine(stateful_dict) # can eventually replace with just desc ref?

##		print(stateful_dict['hand'])

#		with open('save_obj_pickle', 'wb') as f:
#				pickle.dump(master_obj_lst, f)

		print("Just before startup write") # troubleshooting

		# Get the current working directory - troubleshooting
		cwd = os.getcwd()

		# Print the current working directory - troubleshooting
		print("Current working directory: {0}".format(cwd))

		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f)

		print("Just after startup write") # troubleshooting

		return stateful_dict['out_buff']


