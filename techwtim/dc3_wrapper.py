# program: dark castle v3.44
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
import pickle
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *
from dc3_class_deff import *
from dc3_start_me_up import start_me_up
from dc3_interpreter import interpreter
from dc3_cmd_execute import cmd_execute
from  dc3_score import score
from dc3_end import end


# wrapper code - calls interpreter and saves game state
def wrapper(user_input):
		if user_input == "xyzzy42":
				end_of_game, out_buff = start_me_up()
		else:

				# object list loaded from save_obj_pickle2
				with open('save_obj_pickle2', 'rb') as f:
						master_obj_lst = pickle.load(f)

				# object vatiables declared / instantiated from un-pickled list
				stateful_dict = master_obj_lst[0]
				active_gs = master_obj_lst[1]

				active_gs.move_inc()
				stateful_dict['out_buff'] = "" # resets buffer
				active_gs.reset_buff() # resets buffer

				case, word_lst = interpreter(user_input, master_obj_lst)
				# pre-action triggers will go here
				cmd_execute(stateful_dict, active_gs, case, word_lst)
				# post-action triggers will go here
				score(stateful_dict, active_gs)
				if active_gs.get_game_ending() != "tbd":
						end(stateful_dict, active_gs)

				### dump updated objects to save_obj_pickle2 ###
				with open('save_obj_pickle2', 'wb') as f:
						pickle.dump(master_obj_lst, f)

				end_of_game = active_gs.get_end_of_game()
#				out_buff = stateful_dict['out_buff']
				out_buff_old = stateful_dict['out_buff']
				out_buff_new = active_gs.get_buff()
				out_buff = out_buff_old + out_buff_new

		return end_of_game, out_buff
