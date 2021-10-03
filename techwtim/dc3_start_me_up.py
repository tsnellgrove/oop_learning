# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 5, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
import pickle
import random
#from itertools import islice
from dc3_static_init import * # variables declared in import = global to module
#from dc3_classes import *
#from dc3_classes2 import declare_classes
from dc3_helper import *
import gc

def start_me_up():

		print("start_me_up start")

		from dc3_define_class_gs import GameState

		active_gs = GameState('active_gs1', {}, {}, {}, {})
		print("classes immediately after bootstrap active_gs is declared")
		for obj in gc.get_objects():
				if isinstance(obj, GameState):
						print(obj, id(obj), sys.getrefcount(obj))
		print("classes: active_gs declared")

		from dc3_define_class_other import Writing, ViewOnly, Room, Item, Door, Container, Food, Jug, Beverage

#		declare_classes(first_time=True)
#		global game_state

		print("start_me_up post-declare_classes and pre-pickle load")

		for obj in gc.get_objects():
				if isinstance(obj, GameState):
						print(obj, id(obj), sys.getrefcount(obj))

		# default object list loaded from pickle (NO active_gs)
		with open('default_obj_pickle', 'rb') as f:
				master_obj_lst = pickle.load(f)

		# object vatiables declared / instantiated from un-pickled list
		rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, stateful_dict = master_obj_lst

		print("start_me_up - pickle load")

		#	troubleshooting
		print("start_up - pre active_gs assignments")
		for obj in gc.get_objects():
				if isinstance(obj, GameState):
						print(obj, id(obj), sys.getrefcount(obj))
				if isinstance(obj, Room):
						print(obj, id(obj), sys.getrefcount(obj))

		#	global game_state
		active_gs._name = 'active_gs2'
		active_gs._dynamic_desc_dict = {'messy_handwriting' : ""}
		active_gs._map_dict = {
						'entrance' : {'north' : main_hall},
						'main_hall' : {'south' : entrance, 'north' : antechamber},
						'antechamber' : {'south' : main_hall, 'north' : throne_room},
						'throne_room' : {'south' : antechamber}
						}
		active_gs._static_obj_dict = {'universal' : [backpack, burt, fist, conscience]}
		active_gs._state_dict = {}

		### Assign Random Secret Code ###
		portcullis_code = random.randint(0, 7)
		port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
		active_gs.set_dynamic_desc_dict('messy_handwriting', port_code_txt)
		
		stateful_dict['dynamic_desc_dict']['messy_handwriting'] = port_code_txt

#		print("start_up: The id of " + antechamber.name + " is " + str(id(antechamber)))
#		print("star_up: The game_state id of antechamber (from main_hall) is " + str(id(game_state._map_dict['main_hall']['north'])))
#		print("start_up: The stateful_dict['paths']['main_hall']['north'] id is " + str(id(stateful_dict['paths']['main_hall']['north'])))

		print("start_me_up - post actvie_gs assignments")
		for obj in gc.get_objects():
				if isinstance(obj, GameState):
						print(obj, id(obj), sys.getrefcount(obj))
				if isinstance(obj, Room):
						print(obj, id(obj), sys.getrefcount(obj))

		buffer(stateful_dict, descript_dict["introduction"])
		buffer(stateful_dict, descript_dict["entrance"])

		master_obj_lst = [rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, active_gs, stateful_dict]

		with open('save_obj_pickle2', 'wb') as f:
				pickle.dump(master_obj_lst, f)

		print("start_me_up - pickle dump")
		
		return stateful_dict['end_of_game'], stateful_dict['out_buff']		
