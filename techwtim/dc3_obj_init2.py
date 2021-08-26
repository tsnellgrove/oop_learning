# program: dark castle v3.33
# name: Tom Snellgrove
# date: Aug 26, 2021
# description: object instantiation module

# import statements
import pickle
from dc3_classes import *


# object list loaded from pickle
with open('save_obj_pickle2', 'rb') as f:
		master_obj_lst = pickle.load(f)

# object vatiables declared / instantiated from un-pickled list
rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, wooden_chest, crystal_box, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, stateful_dict = master_obj_lst

