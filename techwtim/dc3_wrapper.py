# program: dark castle v3.48
# name: Tom Snellgrove
# date: Oct 22, 2021
# description: app-side wrapper module that calls game functions


### import statements
import sys
import pickle
from dc3_start_me_up import start_me_up
from dc3_interpreter import interpreter
from dc3_cmd_execute import cmd_execute
from  dc3_score import score
from dc3_end import end


### wrapper code - loads game obj, calls other modules, and saves game obj
def wrapper(user_input):
		if user_input == "xyzzy42":
				end_of_game, out_buff = start_me_up()
		else:

				# object list loaded from save_obj_pickle2
				with open('save_obj_pickle2', 'rb') as f:
						master_obj_lst = pickle.load(f)

				# Gamestate vatiable instantiated from un-pickled list
				active_gs = master_obj_lst[0]

				active_gs.move_inc()
				active_gs.reset_buff() # resets buffer

				case, word_lst = interpreter(user_input, master_obj_lst)
				# pre-action triggers will go here
				cmd_execute(active_gs, case, word_lst)
				# post-action triggers will go here
				score(active_gs)
				if active_gs.get_game_ending() != "tbd":
						end(active_gs)

				### dump updated objects to save_obj_pickle2 ###
				with open('save_obj_pickle2', 'wb') as f:
						pickle.dump(master_obj_lst, f)

				end_of_game = active_gs.get_end_of_game()
				out_buff = active_gs.get_buff()

		return end_of_game, out_buff
