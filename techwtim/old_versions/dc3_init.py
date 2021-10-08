# NO LONGER IN USE IN v3.42

# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 5, 2021
# description: object instantiation module


# import statements
import sys
import pickle
from dc3_classes import *
import random
import gc


# object instantiation - starting state
rusty_lettering = Writing('rusty_lettering', 'Rusty Lettering', "lettering", 'rusty_lettering')
dwarven_runes = Writing('dwarven_runes', 'Dwarven Runes', "runes", 'dwarven_runes')
messy_handwriting = Writing('messy_handwriting', 'Messy Handwriting', 'handwriting', 'messy_handwriting')
small_print = Writing('small_print', 'Small Print', 'print', 'small_print')
illuminated_letters = Writing('illuminated_letters', 'Illuminated Letters', 'letters', 'illuminated_letters')
calligraphy = Writing('calligraphy', 'Calligraphy', 'calligraphy', 'calligraphy')
trademark = Writing('trademark', 'Trademark', 'trademark', 'trademark')

dark_castle = ViewOnly('dark_castle', "Dark Castle", "castle", 'dark_castle', None)
moat = ViewOnly('moat', 'Moat', 'moat', 'moat', None)
backpack = ViewOnly('backpack', "Backpack", "backpack", 'backpack', None)
burt = ViewOnly('burt', 'Burt', "burt", 'burt', None)
fist = ViewOnly('fist', 'Fist', "fist", 'fist', None)
conscience = ViewOnly('conscience', 'Conscience', "conscience", 'conscience', None)
faded_tapestries = ViewOnly('faded_tapestries', 'Faded Tapestries', 'tapestries', 'faded_tapestries', None)
alcove = ViewOnly('alcove', 'Alcove', 'alcove', 'alcove', None)
stone_coffer = ViewOnly('stone_coffer', 'Stone Coffer', 'coffer', 'stone_coffer', None)
family_tree = ViewOnly('family_tree', 'Family Tree', 'tree', 'family_tree', None)

rusty_key = Item('rusty_key', 'Rusty Key', "key", 'rusty_key', None, True)
shiny_sword = Item('shiny_sword', 'Shiny Sword', "sword", 'shiny_sword', dwarven_runes, True)
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None, True) # test object
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'bubbly_potion', None, True) # test object
torn_note = Item('torn_note', 'Torn Note', 'note', 'torn_note', messy_handwriting, True)
grimy_axe = Item('grimy_axe', 'Grimy Axe', 'axe', 'grimy_axe', small_print, True)
silver_key = Item('silver_key', 'Silver Key', 'key', 'silver_key', None, True)
kinging_scroll = Item('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', illuminated_letters, True)

cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None, True, 'cheese_eat')
stale_biscuits = Food('stale_biscuits', 'Stale Biscuits', 'biscuits', 'stale_biscuits', trademark, True, 'biscuit_eat')

fresh_water = Beverage('fresh_water', 'Fresh Water', 'water', 'fresh_water', None, 'water_drink')

wooden_chest = Container('wooden_chest', 'wooden chest', "chest", 'wooden_chest', None,
				False, False, brass_key, False, [bubbly_potion]) # test object
crystal_box = Container('crystal_box', 'Crystal Box', 'box', 'crystal_box', calligraphy,
				False, False, silver_key, False, [kinging_scroll])
# giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])

glass_bottle = Jug('glass_bottle', 'Glass Bottle', 'bottle', 'glass_bottle', None, True, True, [fresh_water])

front_gate = Door('front_gate', 'Front Gate', "gate", 'front_gate', rusty_lettering, False, False, rusty_key)
# screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)
iron_portcullis = Door('iron_portcullis', 'Iron Portcullis', 'portcullis', 'iron_portcullis', None, True, False, None)

control_panel = ViewOnly('control_panel', 'Control Panel', 'panel', 'control_panel', None)
throne = ViewOnly('throne', 'Throne', 'throne', 'throne', None)

entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, [dark_castle, moat],
				[front_gate], {'north' : front_gate})
main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
				[shiny_sword, front_gate], {'south' : front_gate})
antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None, [alcove, control_panel],
				[torn_note, grimy_axe, iron_portcullis], {'north' : iron_portcullis})
throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
				[throne, silver_key, crystal_box, iron_portcullis], {'south' : iron_portcullis})

print("init pre game_state declarations")
for obj in gc.get_objects():
		if isinstance(obj, GameState):
				print(obj, id(obj), sys.getrefcount(obj))
		if isinstance(obj, Room):
				print(obj, id(obj), sys.getrefcount(obj))

game_state._name = 'game_state2'
game_state._dynamic_desc_dict = {'messy_handwriting' : ""}
game_state._map_dict = {
				'entrance' : {'north' : main_hall},
				'main_hall' : {'south' : entrance, 'north' : antechamber},
				'antechamber' : {'south' : main_hall, 'north' : throne_room},
				'throne_room' : {'south' : antechamber}
				}
game_state._static_obj_dict = {'universal' : [backpack, burt, fist, conscience]}
game_state._state_dict = {}

#game_state = GameState(
#				'game_state2',
#				{'messy_handwriting' : ""},
#				{
#						'entrance' : {'north' : main_hall},
#						'main_hall' : {'south' : entrance, 'north' : antechamber},
#						'antechamber' : {'south' : main_hall, 'north' : throne_room},
#						'throne_room' : {'south' : antechamber}
#				},
#				{'universal' : [backpack, burt, fist, conscience]},
#				{}
#)


print("init post game_state declarations")
for obj in gc.get_objects():
		if isinstance(obj, GameState):
				print(obj, id(obj), sys.getrefcount(obj))
		if isinstance(obj, Room):
				print(obj, id(obj), sys.getrefcount(obj))

#print(game_state._map_dict)
#print("id(game_state._map_dict['entrance']['north']) = " + id(game_state._map_dict['entrance']['north']))

#### dictionary of variables passed to all functions ###
#### any object variable that is passed to helper() must be in this dict ###
stateful_dict = {
		'hand' : [], 
		'backpack' : [rusty_key, cheese_wedge, stale_biscuits, glass_bottle],
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
				'antechamber' : {'south' : main_hall, 'north' : throne_room},
				'throne_room' : {'south' : antechamber}
				},
		}

#print(stateful_dict['paths'])
#print(id(stateful_dict['paths']['entrance']['north']))
print("dc3_init: The id of " + antechamber.name + " is " + str(id(antechamber)))
print("dc3_init: The game_state id of antechamber (from main_hall) is " + str(id(game_state._map_dict['main_hall']['north'])))
print("dc3_init: The stateful_dict['paths']['main_hall']['north'] id is " + str(id(stateful_dict['paths']['main_hall']['north'])))


### Assign Random Secret Code ###
portcullis_code = random.randint(0, 7)
port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
game_state.set_dynamic_desc_dict('messy_handwriting', port_code_txt)

#switch_dict['big_red_button']['success_value'] = portcullis_code


# instantiated objects added to list
master_obj_lst = [rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, game_state, stateful_dict]

### if, when the game is done, I want to load variables from pickle ###
### (rather than declare openly as in dc3_init ### 
### then re-enable default_obj_pickly dump ###
### and call start_me_up() from dce_startup  in main ### 

# with open('default_obj_pickle', 'wb') as f:
#		pickle.dump(master_obj_lst, f)

# list written to pickle
with open('save_obj_pickle2', 'wb') as f:
		pickle.dump(master_obj_lst, f)

print("pickle dump")

# del(game_state) # troubleshooting
				
#del(game_state) # troubleshooting

for obj in  master_obj_lst:
		print(obj, id(obj), sys.getrefcount(obj))
#		print("deleting object")
#		del(obj)


print("init post dump")
for obj in gc.get_objects():
		if isinstance(obj, GameState):
				print(obj, id(obj), sys.getrefcount(obj))
		if isinstance(obj, Room):
				print(obj, id(obj), sys.getrefcount(obj))
