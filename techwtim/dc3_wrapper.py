# program: dark castle v3.42+
# name: Tom Snellgrove
# date: Oct 4, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
import pickle
#import random
#from itertools import islice
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *
from dc3_class_deff import *
import gc
from dc3_start_me_up import start_me_up
from dc3_demo import interpreter, cmd_execute

# wrapper code - calls interpreter and saves game state
def wrapper(user_input):

		print("wrapper start - new dedicated module!") # troubleshooting

		if user_input == "xyzzy42":
				end_of_game, out_buff = start_me_up()
		else:

				print("wrapper post-declare_classes pre-pickle-load")
				for obj in gc.get_objects():
						if isinstance(obj, GameState):
								print(obj, id(obj))

				# object list loaded from pickle
				with open('save_obj_pickle2', 'rb') as f:
						master_obj_lst = pickle.load(f)

				# object vatiables declared / instantiated from un-pickled list
				stateful_dict, active_gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room = master_obj_lst

				print("wrapper - post-pickle load")

				stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1
				stateful_dict['out_buff'] = "" # resets buffer

				### test commands ###
#				stale_biscuits.take(stateful_dict)
#				fresh_water.drink(stateful_dict)
#				torn_note.examine(stateful_dict)
				### test commands ###

				#	troubleshooting
				print("wrapper - pre interpreter")
				for obj in gc.get_objects():
						if isinstance(obj, GameState):
								print(obj, id(obj), sys.getrefcount(obj))
						if isinstance(obj, Room):
								print(obj, id(obj), sys.getrefcount(obj))

##				case, word_lst = interpreter(user_input, master_obj_lst)
				case, word_lst = interpreter(user_input, stateful_dict, master_obj_lst)
###			case, word_lst = interpreter(stateful_dict, user_input)
				# pre-action triggers will go here
				if case in ['go', 'put', '2word']:
						cmd_execute(stateful_dict, active_gs, case, word_lst)
				# post-action triggers will go here

				master_obj_lst = [stateful_dict, active_gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room]

				with open('save_obj_pickle2', 'wb') as f:
						pickle.dump(master_obj_lst, f) # Why are list elements updated? But works!
		
				print("wrapper - pickle dump")
				
				end_of_game = stateful_dict['end_of_game']
				out_buff = stateful_dict['out_buff']

		print("wrapper end - new dedicated module!")

		return end_of_game, out_buff
