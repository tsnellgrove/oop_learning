# program: dark castle v3.47
# name: Tom Snellgrove
# date: Oct 16, 2021
# description: gets obj from default_pkl, welcome text, sets starting values



# import statements
import sys
import pickle
import random
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *
from dc3_class_deff import *

def start_me_up():

		### object list loaded from default_obj_pickle ###
		with open('default_obj_pickle', 'rb') as f:
				master_obj_lst = pickle.load(f)

		active_gs = master_obj_lst[0]

		### Assign Random Secret Code ###
		portcullis_code = random.randint(0, 7)
		port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
		active_gs.set_dynamic_desc_dict('messy_handwriting', port_code_txt)		

		### introductory text ###
		active_gs.buffer(descript_dict["introduction"])
		active_gs.buffer(descript_dict["entrance"])
		active_gs.buffer("The room contains: Front Gate")

		### dump updated objects to save_obj_pickle ###
		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f)

		end_of_game = active_gs.get_end_of_game()
		out_buff = active_gs.get_buff()

		return end_of_game, out_buff
