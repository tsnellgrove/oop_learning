# program: dark castle v3
# name: Tom Snellgrove
# date: May 13, 2021
# description: object instantiation routine for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter


# import statements
from dc3_classes import *


# object instantiation
dark_castle = ViewOnly('dark_castle', "dark castle", "castle", 'The evil Dark Castle looms above you', None)
backpack = ViewOnly('backpack', "backpack", "backpack", "Your trusty, well-worn leather backpack", None)
burt = ViewOnly('burt', 'burt', "burt", "Yep, that's you Burt. A bit mangy and odd but undeniably lovable", None)
fist = ViewOnly('fist', 'fist', "fist", "That is indeed your very own fist", None)
conscience = ViewOnly('conscience', 'conscience', "conscience", "A tad murky Burt - what would your dear old Nana say?", None)

rusty_letters = Writing('rusty_letters', 'rusty letters', "letters", 'Abandon Hope All Ye Who Even Thank About It', None, 'gate')
dwarven_runes = Writing('dwarven_runes', 'dwarven runes', "runes", "Goblin Wallopper", None, 'sword')

rusty_key = Item('rusty_key', 'rusty key', "key", 'The key is rusty', None, True)
shiny_sword = Item('shiny_sword', 'shiny sword', "sword", 'The sword is shiny.', dwarven_runes, True)
brass_key = Item('brass_key', 'brass key', "key", 'The key is brass', None, True)
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'The cork-stopperd glass vial contains a bubbly green potion', None, True)

wooden_chest = Container('wooden_chest', 'wooden chest', "chest", 'An old wooden chest', None,
				False, False, brass_key, False, [bubbly_potion])
# giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])

front_gate = Door('front_gate', 'front gate', "gate", 'The front gate is massive and imposing', rusty_letters,
				False, False, rusty_key)
# screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)

entrance = Room('entrance', 'entrance', "entrance", 
		'*** Entrance ***\n\nYou stand before the daunting gate of Dark Castle. In front of you is the gate.',
		None, [dark_castle], [front_gate], {'north' : 'main_hall'}, {'north' : front_gate})
main_hall = Room('main_hall', 'main hall', "hall", 
		'*** Main Hall ***\n\nA vast and once sumptuous chamber. The main gate is south. There is a passage going north.',
		None, [], [shiny_sword, front_gate, brass_key, wooden_chest], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : front_gate})

# next room definitions after room definitions to avoid undefined variables
entrance.valid_paths['north'] = main_hall
main_hall.valid_paths['south'] = entrance

# writton on deffinitions after variable assignments to avoid undefined variables
rusty_letters.written_on = front_gate
dwarven_runes.written_on = shiny_sword


