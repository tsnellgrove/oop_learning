# program: dark castle v3.10
# name: Tom Snellgrove
# date: June 8, 2021
# description: object instantiation module


# import statements
from dc3_classes import *


# object instantiation
rusty_letters = Writing('rusty_letters', 'rusty letters', "letters")
dwarven_runes = Writing('dwarven_runes', 'dwarven runes', "runes")

dark_castle = ViewOnly('dark_castle', "dark castle", "castle", None)
backpack = ViewOnly('backpack', "backpack", "backpack", None)
burt = ViewOnly('burt', 'burt', "burt", None)
fist = ViewOnly('fist', 'fist', "fist", None)
conscience = ViewOnly('conscience', 'conscience', "conscience", None)

rusty_key = Item('rusty_key', 'rusty key', "key", None, True)
shiny_sword = Item('shiny_sword', 'shiny sword', "sword", dwarven_runes, True)
brass_key = Item('brass_key', 'brass key', "key", None, True)
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", None, True)

wooden_chest = Container('wooden_chest', 'wooden chest', "chest", None,
				False, False, brass_key, False, [bubbly_potion])
# giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])

front_gate = Door('front_gate', 'front gate', "gate", rusty_letters, False, False, rusty_key)
# screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)

entrance = Room('entrance', 'entrance', "entrance", None, [dark_castle],
				[], [front_gate], [], {'north' : front_gate})
main_hall = Room('main_hall', 'main hall', "hall", None, [],
				[shiny_sword, brass_key], [front_gate], [wooden_chest], {'south' : front_gate})

## dictionary of variables passed to all functions ##
## any object variable that is passed to helper() must be in this dict ##
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
				'main_hall' : {'south' : entrance}
				}
		}


#writing_obj_lst = [rusty_letters, dwarven_runes]
#viewonly_obj_lst = [dark_castle, backpack, burt, fist, conscience]
#item_obj_lst = [rusty_key, shiny_sword, brass_key, bubbly_potion]
#container_obj_lst = [wooden_chest]
#door_obj_lst = [front_gate]
#room_obj_lst = [entrance, main_hall]
#obj_lst_lst = [writing_obj_lst, viewonly_obj_lst, item_obj_lst, container_obj_lst, door_obj_lst, room_obj_lst]

