# program: dark castle v3
# name: Tom Snellgrove
# date: May 2, 2021
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
				str_lst.append(obj.full_name)
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

def root_word_count(stateful_dict, word2):
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

		root_count = 0
		obj_name = ""
		for obj in scope_lst:
				if obj.root_name == word2:
						root_count += 1
						obj_name = obj.name # could simplify by just returning obj
		return root_count, obj_name

def container_desc(cont_obj, stateful_dict):
		if len(cont_obj.contains) == 0:
				buffer(stateful_dict, "The " + cont_obj.full_name + " is empty.")
		else:
				cont_str_lst = objlst_to_strlst(cont_obj.contains)
				output = "The " + cont_obj.full_name + " contains: "  + ', '.join(cont_str_lst)
				buffer(stateful_dict, output)

def inventory(stateful_dict):
		hand_obj_lst = stateful_dict['hand']
		backpack_str_lst = objlst_to_strlst(stateful_dict['backpack'])

		if len(hand_obj_lst) == 0:
				hand_str = "nothing"
		else:
				hand_str = "the " + stateful_dict['hand'][0].full_name
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
				buffer(stateful_dict, "You have died.")
		elif game_ending == 'quit':
				buffer(stateful_dict, "You have quit.")
		elif game_ending == 'won':
				buffer(stateful_dict, "You have won!")
		buffer(stateful_dict, "Your adventure ended after " + str(moves) + " moves.")
#    print_score(state_dict, static_dict)
#		buffer("Your title is: " + title)
		if game_ending == 'won':
				buffer(stateful_dict, credits.examine(stateful_dict))
		stateful_dict['end_of_game'] = True
		return


# classes
class ViewOnly(object):
		def __init__(self, name, full_name, root_name, desc, writing):
				self.name = name
				self.full_name = full_name
				self.root_name = root_name
				self.desc = desc
				self.writing = writing

		def examine(self, stateful_dict):
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				else:
						buffer(stateful_dict, self.desc)
						if self.writing is not None:
								output = "On the " + self.full_name + " you see: " + self.writing.full_name
								buffer(stateful_dict, output)

class Writing(ViewOnly):
		def __init__(self, name, full_name, root_name, desc, writing, written_on):
				super().__init__(name, full_name, root_name, desc, writing)
				self.written_on = written_on

		def read(self, stateful_dict):
				if scope_check(self.written_on, stateful_dict) == False:
						buffer(stateful_dict, "You can't see any " + self.full_name + " here.")
				else:
						buffer(stateful_dict, self.desc)

class Room(ViewOnly):
		def __init__(self, name, full_name, root_name, desc, writing, features, room_stuff, valid_paths, door_paths):
				super().__init__(name, full_name, root_name, desc, writing)
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
								buffer(stateful_dict, "The " +  door_obj.full_name + " is closed.")
						else:
								next_room_obj = self.valid_paths[direction]
								stateful_dict['room'] = next_room_obj
								next_room_obj.examine(stateful_dict)

class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, desc, writing, takeable):
				super().__init__(name, full_name, root_name, desc, writing)
				self.takeable = takeable

		def take(self, stateful_dict):
				room_obj = stateful_dict['room']
				hand_lst = stateful_dict['hand']
				backpack_lst = stateful_dict['backpack']
				room_obj_lst = room_obj.room_stuff
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif self.takeable == False:
						buffer(stateful_dict, "You can't take the " + self.full_name)
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
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif self not in hand_lst:
						output = "You're not holding the " + self.full_name + " in your hand."
						buffer(stateful_dict, output)
				else:
						hand_lst.remove(self)
						room_obj.room_stuff.append(self)
						buffer(stateful_dict, "Dropped")

class Door(ViewOnly):
		def __init__(self, name, full_name, root_name, desc, writing, open_state, unlock_state, key):
				super().__init__(name, full_name, root_name, desc, writing)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key

		def examine(self, stateful_dict):
				super(Door, self).examine(stateful_dict)
				if scope_check(self, stateful_dict) == False:
						pass
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is closed.")
				else:
						buffer(stateful_dict, "The " + self.full_name + " is open.")
						if hasattr(self, 'contains'):
								container_desc(self, stateful_dict)

		def unlock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif self.unlock_state == True:
						buffer(stateful_dict, "The " + self.full_name + " is already unlocked.")
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				else:
						buffer(stateful_dict, "Unlocked")
						self.unlock_state = True

		def open(self, stateful_dict):
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif self.open_state == True:
						buffer(stateful_dict, "The " + self.full_name + " is already open.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is locked.")
				else:
						self.open_state = True
						buffer(stateful_dict, "Openned")
						if hasattr(self, 'contains'):
								container_desc(self, stateful_dict)

		def close(self, stateful_dict):
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is already closed.")
				else:
						self.open_state = False
						buffer(stateful_dict, "Closed")

		def lock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif self.open_state == True:
						buffer(stateful_dict, "You can't lock something that's open.")						
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is already locked.")
				else:
						buffer(stateful_dict, "Locked")
						self.unlock_state = False

class Container(Door):
		def __init__(self, name, full_name, root_name, desc, writing, open_state, unlock_state, key, takeable, contains):
				super().__init__(name, full_name, root_name, desc, writing, open_state, unlock_state, key)
				self.takeable = takeable # can the container be taken?
				self.contains = contains # list of items in the container


# object instantiation
dark_castle = ViewOnly('dark_castle', "dark castle", "castle", 'The evil Dark Castle looms above you', None)
backpack = ViewOnly('backpack', "backpack", "backpack", "Your trusty, well-worn leather backpack", None)
burt = ViewOnly('burt', 'burt', "burt", "Yep, that's you Burt. A bit mangy and odd but undeniably lovable", None)
fist = ViewOnly('fist', 'fist', "fist", "That is indeed your very own fist", None)
conscience = ViewOnly('conscience', 'conscience', "conscience", "A tad murky Burt - what would your dear old Nana say?", None)
help = ViewOnly('help', 'help', "help", "Detailed help text for new players [to be written]", None)
credits = ViewOnly('credits', 'credits', "credits", "Standard credits from dkv2 + my 4 playtesters!", None)

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
		'Entrance\nYou stand before the daunting gate of Dark Castle. In front of you is the gate',
		None, [dark_castle], [front_gate], {'north' : 'main_hall'}, {'north' : front_gate})
main_hall = Room('main_hall', 'main hall', "hall", 
		'Main Hall\nA vast and once sumptuous chamber. The main gate is south. There is a passage going north.',
		None, [], [shiny_sword, front_gate, brass_key, wooden_chest], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : front_gate})

# next room definitions after room definitions to avoid undefined variables
entrance.valid_paths['north'] = main_hall
main_hall.valid_paths['south'] = entrance

# writton on deffinitions after variable assignments to avoid undefined variables
rusty_letters.written_on = front_gate
dwarven_runes.written_on = shiny_sword

# stateful dictionary of persistent values
stateful_dict = {
		'hand' : [], 
		'backpack' : [rusty_key],
		'universal' : [backpack, burt, fist, conscience, help, credits],
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
one_word_only_lst = ['score', 'version', 'inventory', 'look', 'quit', 'xyzzy42']
articles_lst = ['a', 'an', 'the']
verbs_lst = ['examine', 'read', 'go', 'take', 'drop', 'unlock', 'open', 'close', 'lock']
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

descript_dict = {
		'introduction' : "This is the introduction [to be written]"
}

# interpreter function
def interpreter(stateful_dict, user_input):
		stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1 
		room_obj = stateful_dict['room']
		lst = []
		lst.append(user_input)
		user_input_lst = lst[0].split() # convert user input string into word list

		# convert all words to lower case and substitute abreviations
		n = 0 
		for word in user_input_lst:
				word = word.lower()	
				if word in abreviations_dict:
						word = abreviations_dict[word]
				user_input_lst[n] = word
				n += 1

		# strip out articles
		for article in articles_lst:
				user_input_lst = [word for word in user_input_lst if word != article]
 
 		# no input or the only input is articles
		if len(user_input_lst) < 1: 
				buffer(stateful_dict, "I have no idea what you're talking about Burt!")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return 		

		# handle true one-word commands
		if len(user_input_lst) == 1:
				word1 = user_input_lst[0]
				if word1 in one_word_only_lst:
						if word1 == 'xyzzy42':
								buffer(stateful_dict, descript_dict["introduction"])
								help.examine(stateful_dict)
								buffer(stateful_dict, "")
								entrance.examine(stateful_dict)
						elif word1 == 'score':
								buffer(stateful_dict, "Your score is " + str(stateful_dict['score']))
						elif word1 == 'version':
								buffer(stateful_dict, stateful_dict['version'])
						elif word1 == 'inventory':
								inventory(stateful_dict)
						elif word1 == 'look':
								room_obj.examine(stateful_dict)
						elif word1 == 'quit':
								stateful_dict['game_ending'] = "quit"
								stateful_dict['move_counter'] = stateful_dict['move_counter'] - 2
								end(stateful_dict)
						return
						
				# convert one-word commands that are implicit two-word commands 
				elif word1 in one_word_convert_dict:
						user_input_lst.append(word1)
						user_input_lst[0] = one_word_convert_dict[word1]
						word1 = user_input_lst[0]

				# if not a known true or convertable one-word command, must be an error
				else:
						buffer(stateful_dict, "I don't understand what you're trying to say?")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return 

		# multi-word commands
		if len(user_input_lst) > 1:
				word1 = user_input_lst[0].lower()
				word2 = user_input_lst[1].lower()
		else:

				# commnd len ! > 1 should already be errored out
				buffer(stateful_dict, "HOW DID WE GET HERE???")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return

		# all commands longer than one word should start with a verb
		if word1 not in verbs_lst:
				buffer(stateful_dict, "Please start your sentence with a verb!")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return
	
		# convert 3-word verb-adj-noun command into verb-obj_name
		if len(user_input_lst) == 3:
				word3 = user_input_lst[2].lower()
				user_input_lst[1] = word2 + "_" + word3
				word2 = user_input_lst[1]
				del user_input_lst[2]

		# error out commands longer than two words
		if len(user_input_lst) > 2:
				buffer(stateful_dict, "Can you state that more simply? Burt's a man of few words!")
				return 

		# handle 2-word commands
		if word1 == 'go':
				getattr(room_obj, word1)(word2, stateful_dict)
				return # newly added
		
		# check to see if word2 is a known obj_name
		try:
				word2_obj = str_to_class(word2)
		except:
				root_count, obj_name = root_word_count(stateful_dict, word2)
				if root_count < 1:
						buffer(stateful_dict, "I don't see a " + word2 + " here.")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return
				elif root_count > 1:
						output = "I see more than one " + word2 + ". Please use the full name."
						buffer(stateful_dict, output)
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return
				else:
						word2_obj = str_to_class(obj_name)

		# check to see if the word2 is a root_name; convert to obj_name if valid

		# attempt to proces 2-word command
		try:
				getattr(word2_obj, word1)(stateful_dict)
		except:
				buffer(stateful_dict, "You can't " + word1 + " with the " + word2 + ".")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1


##		else:
##				try:
##						word2_obj = str_to_class(word2)
##						try:
##								getattr(word2_obj, word1)(stateful_dict)
##						except:
##								output = "You can't " + word1 + " with the " + word2 + "."
##								buffer(stateful_dict, output)
##								stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
##				except:
##						output = "There's no " + word2 + " here."
##						buffer(stateful_dict, output)
##						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1


# test
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
# sword.examine(stateful_dict)
# chest.unlock(stateful_dict)


# main loop
start_of_game = True
while stateful_dict['end_of_game'] == False:
		stateful_dict['out_buff'] = "" # resets buffer
		if start_of_game:
				user_input = "xyzzy42" # the magic word!!
				start_of_game = False
		else:
				user_input = input('Type your command: ')
		interpreter(stateful_dict, user_input)
		print(stateful_dict['out_buff'])
print("THANKS FOR PLAYING!!")


# entrance.examine()
# print(entrance.valid_paths)
# entrance.go('south')
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

