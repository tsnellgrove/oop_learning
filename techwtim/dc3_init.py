# program: dark castle v3.30
# name: Tom Snellgrove
# date: Aug 17, 2021
# description: object instantiation module


# import statements
import pickle
from dc3_classes import *
import random


# object instantiation - starting state
rusty_letters = Writing('rusty_letters', 'rusty letters', "letters", 'rusty_letters')
dwarven_runes = Writing('dwarven_runes', 'dwarven runes', "runes", 'dwarven_runes')
messy_handwriting = Writing('messy_handwriting', 'messy handwriting', 'handwriting', 'messy_handwriting')

dark_castle = ViewOnly('dark_castle', "dark castle", "castle", 'dark_castle', None)
backpack = ViewOnly('backpack', "backpack", "backpack", 'backpack', None)
burt = ViewOnly('burt', 'burt', "burt", 'burt', None)
fist = ViewOnly('fist', 'fist', "fist", 'fist', None)
conscience = ViewOnly('conscience', 'conscience', "conscience", 'conscience', None)
alcove = ViewOnly('alcove', 'alcove', 'alcove', 'alcove', None)
control_panel = ViewOnly('control_panel', 'control panel', 'panel', 'control_panel', None)

rusty_key = Item('rusty_key', 'rusty key', "key", 'rusty_key', None, True)
shiny_sword = Item('shiny_sword', 'shiny sword', "sword", 'shiny_sword', dwarven_runes, True)
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None, True)
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'bubbly_potion', None, True)
torn_note = Item('torn_note', 'torn note', 'note', 'torn_note', messy_handwriting, True)

wooden_chest = Container('wooden_chest', 'wooden chest', "chest", 'wooden_chest', None,
				False, False, brass_key, False, [bubbly_potion])
# giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])

front_gate = Door('front_gate', 'front gate', "gate", 'front_gate', rusty_letters, False, False, rusty_key)
# screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)
iron_portcullis = Door('iron_portcullis', 'iron portcullis', 'portcullis', 'iron_portcullis', None, False, False, None)

#entrance = Room('entrance', 'entrance', "entrance", 'entrance', None, [dark_castle],
#				[], [front_gate], [], {'north' : front_gate})
entrance = Room('entrance', 'entrance', "entrance", 'entrance', None, [dark_castle],
				[front_gate], {'north' : front_gate})
#main_hall = Room('main_hall', 'main hall', "hall", 'main_hall', None, [],
#				[shiny_sword, brass_key], [front_gate], [wooden_chest], {'south' : front_gate})
main_hall = Room('main_hall', 'main hall', "hall", 'main_hall', None, [],
				[shiny_sword, brass_key, front_gate, wooden_chest], {'south' : front_gate})
#antechamber = Room('antechamber', 'antechamber', 'antechamber', 'antechamber', None, [alcove, control_panel],
#				[torn_note], [iron_portcullis], [], {'north' : iron_portcullis})
antechamber = Room('antechamber', 'antechamber', 'antechamber', 'antechamber', None, [alcove, control_panel],
				[torn_note, iron_portcullis], {'north' : iron_portcullis})


#### dictionary of variables passed to all functions ###
#### any object variable that is passed to helper() must be in this dict ###
stateful_dict = {
		'hand' : [], 
		'backpack' : [rusty_key],
		'universal' : [backpack, burt, fist, conscience],
		'room' : entrance,
		'out_buff' : "",
		'score' : 0,
		'end_of_game' : False,
		'current_score' : 0,
		'move_counter' : 0,
		'game_ending' : "",
		'paths' : {
				'entrance' : {'north' : main_hall},
				'main_hall' : {'south' : entrance, 'north' : antechamber},
				'antechamber' : {'south' : main_hall, 'north' : entrance} # temp place holder for throne_room
				},
		'descript_updates' : {
				'messy_handwriting' : ""
				}
		}

### Assign Random Secret Code ###
portcullis_code = random.randint(0, 7)
#switch_dict['big_red_button']['success_value'] = portcullis_code
port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
stateful_dict['descript_updates']['messy_handwriting'] = port_code_txt

# instantiated objects added to list
master_obj_lst = [rusty_letters, dwarven_runes, messy_handwriting, dark_castle, backpack, burt, fist, conscience, alcove, control_panel, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, wooden_chest, front_gate, iron_portcullis, entrance, main_hall, antechamber, stateful_dict]

### if, when the game is done, I want to load variables from pickle ###
### (rather than declare openly as in dc3_init ### 
### then re-enable default_obj_pickly dump ###
### and call start_me_up() from dce_startup  in main ### 

# with open('default_obj_pickle', 'wb') as f:
#		pickle.dump(master_obj_lst, f)

# list written to pickle
with open('save_obj_pickle2', 'wb') as f:
		pickle.dump(master_obj_lst, f)



