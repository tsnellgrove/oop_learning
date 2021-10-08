# NO LONGER IN USE IN v3.42

# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 5, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_classes import *


# object list loaded from pickle
with open('save_obj_pickle2', 'rb') as f:
		master_obj_lst = pickle.load(f)

# object vatiables declared / instantiated from un-pickled list
rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, game_state, stateful_dict = master_obj_lst

print("pickle load")

print("obj_init2: The id of " + antechamber.name + " is " + str(id(antechamber)))
print("obj_init2: The game_state id of antechamber (from main_hall) is " + str(id(game_state._map_dict['main_hall']['north'])))
print("obj_init2: The stateful_dict['paths']['main_hall']['north'] id is " + str(id(stateful_dict['paths']['main_hall']['north'])))
