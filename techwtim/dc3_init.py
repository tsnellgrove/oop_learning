# program: dark castle v3.01
# name: Tom Snellgrove
# date: June 5, 2021
# description: object instantiation module


# import statements
from dc3_classes import *


# object instantiation
dark_castle = ViewOnly('dark_castle', "dark castle", "castle", None)
backpack = ViewOnly('backpack', "backpack", "backpack", None)
burt = ViewOnly('burt', 'burt', "burt", None)
fist = ViewOnly('fist', 'fist', "fist", None)
conscience = ViewOnly('conscience', 'conscience', "conscience", None)

rusty_letters = Writing('rusty_letters', 'rusty letters', "letters", None, 'gate')
dwarven_runes = Writing('dwarven_runes', 'dwarven runes', "runes", None, 'sword')

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
				[front_gate], {'north' : 'main_hall'}, {'north' : front_gate})
main_hall = Room('main_hall', 'main hall', "hall", None, [],
				[shiny_sword, front_gate, brass_key, wooden_chest], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : front_gate})

# next room definitions after room definitions to avoid undefined variables
entrance.valid_paths['north'] = main_hall
main_hall.valid_paths['south'] = entrance

# writton on deffinitions after variable assignments to avoid undefined variables
rusty_letters.written_on = front_gate
dwarven_runes.written_on = shiny_sword


