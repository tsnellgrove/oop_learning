# program: dark castle v3
# name: Tom Snellgrove
# date: Apr 17, 2021
# description: a zork-like text adventure game written in object-oriented python


# import statements
import cmd
import sys


# NOT IN USE
def set_difference(a,b):
    return list(set(a)-set(b))

def change_desc(self, new_desc):
		self.desc = new_desc


# helper functions
def buffer(stateful_dict, output_str):
		out_buff = stateful_dict['out_buff']
		out_buff = out_buff + output_str + "\n"
		stateful_dict['out_buff'] = out_buff

def open_cont_scan(stateful_dict, room_obj_lst):
		open_cont_obj_lst = []
		for obj in room_obj_lst:
				if hasattr(obj, 'contains') \
								and len(obj.contains) > 0 \
								and obj.open_state == True:
						open_cont_obj_lst = open_cont_obj_lst + obj.contains
		return open_cont_obj_lst

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def objlst_to_strlst(obj_lst):
		str_lst = []
		for obj in obj_lst:
				str_lst.append(obj.name)
		return str_lst

def scope_check(obj, stateful_dict):
		room_obj = stateful_dict['room']
		hand_lst = stateful_dict['hand']
		backpack_lst = stateful_dict['backpack']
		universal_lst = stateful_dict['universal']
		room_obj_lst = room_obj.room_stuff
		features_lst = room_obj.features
		open_cont_obj_lst = open_cont_scan(stateful_dict, room_obj_lst)
		scope_lst = (room_obj_lst + hand_lst + backpack_lst 
						+ universal_lst + features_lst + open_cont_obj_lst)
		scope_lst.append(room_obj)
		return obj in scope_lst

def container_desc(cont_obj, stateful_dict):
		if len(cont_obj.contains) == 0:
				buffer(stateful_dict, "The " + cont_obj.name + " is empty.")
		else:
				cont_str_lst = objlst_to_strlst(cont_obj.contains)
				output = "The " + cont_obj.name + " contains: "  + ', '.join(cont_str_lst)
				buffer(stateful_dict, output)

def inventory(stateful_dict):
		hand_obj_lst = stateful_dict['hand']
		backpack_str_lst = objlst_to_strlst(stateful_dict['backpack'])

		if len(hand_obj_lst) == 0:
				hand_str = "nothing"
		else:
				hand_str = "the " + stateful_dict['hand'][0].name
		buffer(stateful_dict, "In your hand you are holding " + hand_str)

		if len(backpack_str_lst) == 0:
				backpack_str = "nothing"
		else:
				backpack_str = ', '.join(backpack_str_lst)
		buffer(stateful_dict, "In your backpack you have: " + backpack_str)

def end(stateful_dict):

		score = stateful_dict['current_score']
		moves = stateful_dict['move_counter']
		game_ending = stateful_dict['game_ending']

#		if score < 0:
#				title_score = -10
#		elif score == 0:
#				title_score = 0
#		else:
#				title_score = math.ceil(score / 10) * 10
#		title = static_dict['titles_dict'][title_score]

		if game_ending == 'death':
				buffer("You have died.")
		elif game_ending == 'quit':
				buffer("You have quit.")
		elif game_ending == 'won':
				buffer("You have won!")
		buffer("Your adventure ended after " + str(moves) + " moves.")
#    print_score(state_dict, static_dict)
#		buffer("Your title is: " + title)
		if game_ending == 'won':
				buffer(credits.examine(stateful_dict))
		state_dict['end_of_game'] = True
		return


# classes
class ViewOnly(object):
		def __init__(self, name, desc, writing):
				self.name = name
				self.desc = desc
				self.writing = writing

		def examine(self, stateful_dict):
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				else:
						buffer(stateful_dict, self.desc)
						if self.writing is not None:
								output = "On the " + self.name + " you see: " + self.writing.name
								buffer(stateful_dict, output)

class Writing(ViewOnly):
		def __init__(self, name, desc, writing, written_on):
				super().__init__(name, desc, writing)
				self.written_on = written_on

		def read(self, stateful_dict):
				if scope_check(self.written_on, stateful_dict) == False:
						buffer(stateful_dict, "You can't see any " + self.name + " here.")
				else:
						buffer(stateful_dict, self.desc)

class Room(ViewOnly):
		def __init__(self, name, desc, writing, features, room_stuff, valid_paths, door_paths):
				super().__init__(name, desc, writing)
				self.features = features # list of non-items in room (can be examined but not taken)
				self.room_stuff = room_stuff # list of stuff in room
				self.valid_paths = valid_paths # dictionary of {direction1 : room1, direction2 : room2}
				self.door_paths = door_paths # dictionary of {direction1 : door1}
			
		def examine(self, stateful_dict):
				super(Room, self).examine(stateful_dict)
				if stateful_dict['room'] == self:
						room_str_lst = objlst_to_strlst(self.room_stuff)
						output = "The room contains: " + ', '.join(room_str_lst)
						buffer(stateful_dict, output)
				for obj in self.room_stuff:
						if hasattr(obj, 'contains') and obj.open_state == True:
								container_desc(obj, stateful_dict)

		def go(self, direction, stateful_dict):
				room_obj = stateful_dict['room']
				if direction not in self.valid_paths:
						buffer(stateful_dict, "You can't go that way.")
				elif direction in self.door_paths:
						door_obj = self.door_paths[direction]
						door_open = door_obj.open_state
						if not door_open:
								buffer(stateful_dict, "The " +  door_obj.name + " is closed.")
						else:
								next_room_obj = self.valid_paths[direction]
								stateful_dict['room'] = next_room_obj
								next_room_obj.examine(stateful_dict)

class Item(ViewOnly):
		def __init__(self, name, desc, writing, takeable):
				super().__init__(name, desc, writing)
				self.takeable = takeable

		def take(self, stateful_dict):
				room_obj = stateful_dict['room']
				hand_lst = stateful_dict['hand']
				backpack_lst = stateful_dict['backpack']
				room_obj_lst = room_obj.room_stuff
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				elif self.takeable == False:
						buffer(stateful_dict, "You can't take the " + self.name)
				else:
						if len(hand_lst) > 0: # if hand not empty move item to backpack
								stateful_dict['backpack'].append(hand_lst[0])
								stateful_dict['hand'].remove(hand_lst[0])
						hand_lst.append(self) # put taken item in hand
						buffer(stateful_dict, "Taken")
						if self in backpack_lst: # if taken from backpack, remove from backpack
								stateful_dict['backpack'].remove(self)								
						elif self in room_obj_lst: # if taken from room, remove from room
								room_obj.room_stuff.remove(self)
						else:
								for obj in room_obj_lst: # eles remove item from the container it's in
										if hasattr(obj, 'contains') \
														and len(obj.contains) > 0 \
														and obj.open_state == True:
												if self in obj.contains:
														obj.contains.remove(self)

		def drop(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				room_obj = stateful_dict['room']
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				elif self not in hand_lst:
						output = "You're not holding the " + self.name + " in your hand."
						buffer(stateful_dict, output)
				else:
						hand_lst.remove(self)
						room_obj.room_stuff.append(self)
						buffer(stateful_dict, "Dropped")

class Door(ViewOnly):
		def __init__(self, name, desc, writing, open_state, unlock_state, key):
				super().__init__(name, desc, writing)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key

		def examine(self, stateful_dict):
				super(Door, self).examine(stateful_dict)
				if scope_check(self, stateful_dict) == False:
						pass
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.name + " is closed.")
				else:
						buffer(stateful_dict, "The " + self.name + " is open.")
						if hasattr(self, 'contains'):
								container_desc(self, stateful_dict)

		def unlock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				elif self.unlock_state == True:
						buffer(stateful_dict, "The " + self.name + " is already unlocked.")
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				else:
						buffer(stateful_dict, "Unlocked")
						self.unlock_state = True

		def open(self, stateful_dict):
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				elif self.open_state == True:
						buffer(stateful_dict, "The " + self.name + " is already open.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.name + " is locked.")
				else:
						self.open_state = True
						buffer(stateful_dict, "Openned")
						if hasattr(self, 'contains'):
								container_desc(self, stateful_dict)

		def close(self, stateful_dict):
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.name + " is already closed.")
				else:
						self.open_state = False
						buffer(stateful_dict, "Closed")

		def lock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.name + " here.")
				elif self.open_state == True:
						buffer(stateful_dict, "You can't lock something that's open.")						
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.name + " is already locked.")
				else:
						buffer(stateful_dict, "Locked")
						self.unlock_state = False

class Container(Door):
		def __init__(self, name, desc, writing, open_state, unlock_state, key, takeable, contains):
				super().__init__(name, desc, writing, open_state, unlock_state, key)
				self.takeable = takeable # can the container be taken?
				self.contains = contains # list of items in the container


# object instantiation
dark_castle = ViewOnly('dark_castle', 'The evil Dark Castle looms above you', None)
backpack = ViewOnly('backpack', "Your trusty, well-worn leather backpack", None)
burt = ViewOnly('Burt', "Yep, that's you Burt. A bit mangy and odd but undeniably lovable", None)
hand = ViewOnly('hand', "That is indeed your very own hand", None)
conscience = ViewOnly('conscience', "A tad murky Burt - what would your dear old Nana say?", None)
help = ViewOnly('help', "Detailed help text for new players [to be written]", None)
credits = ViewOnly('credits', "Standard credits from dkv2 + my 4 playtesters!", None)

rusty_letters = Writing('rusty_letters', 'Abandon Hope All Ye Who Even Thank About It', None, 'gate')
dwarven_runes = Writing('dwarven_runes', "Goblin Wallopper", None, 'sword')

rusty_key = Item('rusty_key', 'The key is rusty', None, True)
sword = Item('sword','The sword is shiny.', dwarven_runes, True)
brass_key = Item('brass_key', 'The key is brass', None, True)
potion = Item('potion', 'The cork-stopperd glass vial contains a bubbly green potion', None, True)

chest = Container('chest', 'An old wooden chest', None,
				False, False, brass_key, False, [potion])
# giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])

gate = Door('gate', 'The front gate is massive and imposing', rusty_letters,
				False, False, rusty_key)
# screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)

entrance = Room('entrance',
		'Entrance\nYou stand before the daunting gate of Dark Castle. In front of you is the gate',
		None, [dark_castle], [gate], {'north' : 'main_hall'}, {'north' : gate})
main_hall = Room('main_hall',
		'Main Hall\nA vast and once sumptuous chamber. The main gate is south. There is a passage going north.',
		None, [], [sword, gate, brass_key, chest], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : gate})

# next room definitions after room definitions to avoid undefined variables
entrance.valid_paths['north'] = main_hall
main_hall.valid_paths['south'] = entrance

# writton on deffinitions after variable assignments to avoid undefined variables
rusty_letters.written_on = gate
dwarven_runes.written_on = sword

# stateful dictionary of persistent values
stateful_dict = {
		'hand' : [], 
		'backpack' : [rusty_key],
		'universal' : [backpack, burt, hand, conscience, help, credits],
		'room' : entrance,
		'out_buff' : "",
		'score' : 0, 
		'version' : '3.01',
		'end_of_game' : False,
		'current_score' : 0,
		'move_counter' : 0,
		'game_ending' : ""
		}

#interpreter vocab
one_word_only_lst = ['score', 'version', 'inventory', 'look', 'quit']
articles_lst = ['a', 'an', 'the']
abreviations_dict = {
		'n' : 'north',
		's' : 'south',
		'e' : 'east',
		'w' : 'west',
		'i' : 'inventory',
		'l' : 'look',
		'get' : 'take',
		'x' : 'examine',
		'q' : 'quit'
}
one_word_convert_dict = {
		'help' : 'examine',
		'credits' : 'examine',
		'north' : 'go',
		'south' : 'go',
		'east' : 'go',
		'west' : 'go'
}


# interpreter function
def interpreter(stateful_dict, user_input):
		room_obj = stateful_dict['room']
		lst = []
		lst.append(user_input)
		user_input_lst = lst[0].split() # convert user input string into word list

		n = 0 # convert all words to lower case and substitute abreviations
		for word in user_input_lst:
				word = word.lower()	
				if word in abreviations_dict:
						word = abreviations_dict[word]
				user_input_lst[n] = word
				n += 1

		for article in articles_lst: # strip out articles
				user_input_lst = [word for word in user_input_lst if word != article]
 
		if len(user_input_lst) < 1: # handle case where the _only_ input is articles
				buffer(stateful_dict, "I have no idea what you're talking about Burt!")
				return 

		word1 = user_input_lst[0]

		# handle true one-word commands
		if len(user_input_lst) == 1 and word1 in one_word_only_lst:
				if word1 == 'score':
						buffer(stateful_dict, "Your score is " + str(stateful_dict['score']))
				elif word1 == 'version':
						buffer(stateful_dict, stateful_dict['version'])
				elif word1 == 'inventory':
						inventory(stateful_dict)
				elif word1 == 'look':
						room_obj.examine(stateful_dict)
				elif word1 == 'quit':
						end(stateful_dict)
				return

		else:
				# convert implicit one-word commands into explecit two-word commands
				if len(user_input_lst) == 1 and word1 in one_word_convert_dict:
						user_input_lst.append(word1)
						user_input_lst[0] = one_word_convert_dict[word1]
						word1 = user_input_lst[0]

				if len(user_input_lst) > 1:
						word2 = user_input_lst[1].lower()
				else:
						word2 = "blank"
				if word1 == 'go':
						getattr(room_obj, word1)(word2, stateful_dict)
				else:
						try:
								word2_obj = str_to_class(word2)
								try:
										getattr(word2_obj, word1)(stateful_dict)
								except:
										output = "You can't " + word1 + " with the " + word2 + "."
										buffer(stateful_dict, output)
						except:
								output = "There's no " + word2 + " here."
								buffer(stateful_dict, output)


# test
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
# sword.examine(stateful_dict)
chest.unlock(stateful_dict)


# start text
entrance.examine(stateful_dict)
print("START: " + stateful_dict['out_buff'])
# gate.lock(stateful_dict) # troubleshooting text


# starting variables
## end_of_game = False # move to stateful_dict
start_of_game = True # move to stateful_dict

While stateful_dict['end_of_game'] == False:
		if start_of_game:
				user_input = "start of game"
				start_of_game = False
		else:
				user_input = input('Type your command: ')
				interpreter(stateful_dict, user_input)
				print(stateful_dict['out_buff'])
print("THANKS FOR PLAYING!!")


# main loop
##while True:
#    print(stateful_dict) # troubleshooting text
##		stateful_dict['out_buff'] = ""
##		user_input = input('Type your command: ')
##		if user_input == "quit":
##				print("Goodbye!")
##				break
##		interpreter(stateful_dict, user_input)
##		print(stateful_dict['out_buff'])


# entrance.examine()
# print(entrance.valid_paths)
#entrance.go('south')
# entrance.go('north')


# entrance.examine()
# dark_castle.examine()
# gate.examine()
# gate.read_writing()
# sword.examine()
# sword.take()
# print(hand)
# sword.take()
# sword.drop()
# gate.open()
# gate.unlock()
# rusty_key.examine()
# rusty_key.take()
# print(hand)
# gate.unlock()
# gate.open()
# gate.open()
# print(eval(room).room_stuff)


# sword = Item('sword','The sword is shiny.', True, 5)
# sword.examine()
# sword.change_desc('The sword is rusty.')
# sword.examine()
# print(sword.takeable)
# print(sword.weight)
# sword.add_writing('dwarven runes', 'Goblin Wallaper')
# sword.examine()
# sword.read_writing()
# gate = Door('front gate', 'The front gate is daunting', False, False)
# gate.examine()
# gate.change_desc('The front gate is HUGE!')
# gate.examine()
# gate.read_writing()
# gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
# gate.read_writing()

