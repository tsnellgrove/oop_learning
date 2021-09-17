# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 17, 2021
# description: main wrapper modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!

# import statements
import sys
import pickle
from itertools import islice
from dc3_static_init import * # variables declared in import = global to module
from dc3_classes import *
from dc3_helper import *
from dc3_obj_init2 import *

# wrapper code - calls interpreter and saves game state
def wrapper(user_input):

		# object list loaded from pickle
###		with open('save_obj_pickle2', 'rb') as f:
###				master_obj_lst = pickle.load(f)

		# object vatiables declared / instantiated from un-pickled list
###		rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, game_state, stateful_dict = master_obj_lst

###		print("pickle load")

###		print("obj_init2: The id of " + antechamber.name + " is " + str(id(antechamber)))
###		print("obj_init2: The game_state id of antechamber (from main_hall) is " + str(id(game_state._map_dict['main_hall']['north'])))
###		print("obj_init2: The stateful_dict['paths']['main_hall']['north'] id is " + str(id(stateful_dict['paths']['main_hall']['north'])))

		stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1
		stateful_dict['out_buff'] = "" # resets buffer

		### test commands ###
#		stale_biscuits.take(stateful_dict)
#		fresh_water.drink(stateful_dict)
#		front_gate.examine(stateful_dict)
##		print(stateful_dict['room'])
##		print(id(stateful_dict['room']))
		print("wrapper: The id of " + antechamber.name + " is " + str(id(antechamber)))
		print("wrapper: The game_state id of antechamber (from main_hall) is " + str(id(game_state._map_dict['main_hall']['north'])))
		print("wrapper: The stateful_dict['paths']['main_hall']['north'] id is " + str(id(stateful_dict['paths']['main_hall']['north'])))
		### test commands ###

		case, word_lst = interpreter(stateful_dict, user_input)
		# pre-action triggers will go here
		if case in ['go', 'put', '2word']:
				cmd_execute(stateful_dict, case, word_lst)
		# post-action triggers will go here

		master_obj_lst = [rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, game_state, stateful_dict]

		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f) # Why are list elements updated? But works!
		
		print("pickle dump")
		
		return stateful_dict['end_of_game'], stateful_dict['out_buff']
