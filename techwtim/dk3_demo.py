# program: dark castle v3
# name: Tom Snellgrove
# date: feb 24, 2021
# description: a zork-like text adventure game written in object-oriented python

# to-dos

# NEXT: Tom Example
# inheritance
# Create Door as child of Item [DONE]
# Create ViewOnly as parent to Item [DONE]
# Create Container as child to door [DONE]
# Create take & drop methods for Item [DONE]
# Create unlock method for Door & Container [DONE]
# Create open method for Door [DONE]
# Create a Room child class of view_only... focus on inventory only - not movement [DONE]
# Exercise inventory management using Room.room_objects and hand and take and drop [IN-PROC]
	# Update Room examine, take, and drop [DONE]
	# DONE: Test implementation
	#DONE: add takability to the 'take item' method
# DONE: More tutorials before this gets out of hand!
# Note: I think I'm doing something wrong... 
#		inventory management with objects is not as elegant as I was expecting

# DONE: Too many calsses already... think about consolidation
# Decision: Inheritance is complicated, Multi-Inheritance is more complicated, 
#		and multi inheritance from inherited classes... is just right out!
# DONE: So => make 'takable' a local attribute of container

# Idea: Rooms are really just conneectd containers...
# DONE: Link travel to doors or to rooms? For now deciding on rooms
# DONE: Troubleshooting movement
# DONE: Implemnt doors in rooms

# DONE: Implement While True input loop
# DONE: Fix input conversion
# DONE: Fix go command - interpreter
# DONE: Description of new room on change rooms
# DONE: Enforce room.examine() based on location
# DONE: Implement 'look'
# DONE: Update room based on go (try global room)
# DONE: Pass room variable to class methods (state_dict)
#	DONE: Troubleshoot "examine gate"... maybe implemnt room across all methods first??

# DONE: Think through writing attribute for ViewOnly 
#		(i.e. should be read dwarven_runes instead of read sword)
# IDEA: Maybe what I want to do is create a method that can put one item *on* another... 
#		so that I can put the writing *on* the item?
# IDEA: Similar problem to a container... need a list of things that can be *on* the item - 
# IDEA: should be at the ViewOnly level since many objects can have writing on them...
# IDEA: nead a name... maybe 'features'
# IDEA: this could also be used for control panel

# DONE: Extend examine() for class Door to include open or close state
# DONE: Fix read_writing => read
# DONE: Implement 'close'
# DONE: Implement 'lock'

# DONE: Implement features
# DONE: Writing as class
# DONE: Implement read for ViewOnly class
# DONE: Extend examine method for classes Room and Door (vs. replace)
# DONE: Test read for Door class
# DONE: Move 'features' to Room class (since we only examine room features)
# DONE: Re-add 'features' to ViewOnly class - 
#		because otherwise there is no way to include it in examine_lst
# DONE: Add presence checking for examine on Door and Room classes

# DONE: Implement containers
# DONE: Decide how container contents should be presented and added to examine and take scope
# DEC: Show container contents with hasattr upon open and then add to room objects
# DONE: Implement 'open' case for containers (troubleshoot and implement case of empty containers)
# DONE: Implement / Troubleshoot 'close' case for containers
# NOTE: Implemented close reduction of room_objects via sets which leads to re-order

# DONE: Reconsider restricting 'features' to class Room using hasattr
# DONE: dis-allow locking when Door / Container object is open?
# DONE: Represent container elements as sub elements of container in room
# NOTE: Now I have a few more container problems:
# DONE: First I need to make items in containers takable... 
#		but not list them in the room_objects inventory... 
#		perhaps I have an open_container_obj list? 
#		Or perhaps better yet, 
#		dynamically add contents of open containers to takeable scope? [YES!!]
# IDEA: Next, when I take the item from the container,
#		I need to remove it from <container>.contains
# DONE: I think this in turn means 
#		that the *item* needs to know what container it's in (like writing)?...
#		No... let's keep items 'dumb'... 
#		it's the room's job to know what's in the room 
#		and it's the container's job to know what's in the container... 
#		to implement this we just reverse the take scope process... 
#		we start with a for loop of open containers and remove from there if possible
#		else remove from room_objects
# NOTE: I didn't have these issues in the old Dark Castle 
#		because I had no 'close' command... 
#		so I could safely dump the contents of any container 
#		into room_obj the moment the container was openned. 
#		Now that containers can be closed I need to actually solve this problem.
# NOTE2: Should writing work this same way?
#		No - I think it makes sense for writing to know what it's on..
#		Because the two are entwined... 
#		the writing on one object can never move to another
# DONE: Add 'the container is empty' description for empty containers
# DONE: Can't examine items in open containers... 
#		need to add open container contents to examine_lst

# DONE: Redirect prints to buffer
# DONE: Create stateful_dict['out_buff']
# DONE: Create buffer() helper function
#	DONE: "Bufferize" classes ViewOnly and Writing
# DONE: "Bufferize" classes Room and Item
# DONE: "Bufferize" class Door method examine
# DONE: "Bufferize" class Door remaining methods

# DONE: functionalize interpreter
# DONE: "Bufferize" interpreter

# DONE: Added open containers to read scope 
#	DONE: Functionalize container scan, perhaps look in room first


# At this point, STOP(!!!), and start researching how others have implemented OOP text adventures
#		DONE: Watch this non-oop text adventure tutorial: https://youtu.be/miuHrP2O7Jw
#			Basic but good start
#		DONE: OOP text adv tut: https://youtu.be/VxhZZHnig8U
#			I can't stand this instructor's code style - more lessons after this one but can't face them
#		DONE: 2013 advanced OOP Txt Adv: https://youtu.be/8CDePunJlck
#			Great lesson! But all about console so need to pick and choose ideas
#		NOTE: Did a bit of research - looks like cmd can be used with Flask; need to learn more about NLTK
#		DONE: NLTK vid: https://youtu.be/1taCGR3_jlA
#		DONE: Found Jeffery Armstrong from 2013 PyOhio Text Adv: https://github.com/ArmstrongJ?tab=overview&from=2021-03-01&to=2021-03-06
#		NEXT: Understand robotadventure code better... learn about interpreter, DB, and JSON descriptions

# new ideas:
#		use a display_intro function
# 	import pprtint from pprint | pprint(vars(<object>))
#		check https://github.com/ArmstrongJ/pyohio2013
#		get to know cmd module - can cmd be used with flask??
# 	rooms to have lists of neighbors, objects, characters
#		store rooms in json using json module? (import json) [see adv OOP at 15:30]
#		room descriptions in json but then json-based rooms in sql DB??
#		read through 2013 code in detail!!!
#		make a copy of game DB for each player - enables "saved game"... 
#		but will still need to differentiate static from stateful?
#		modules for making file copy: tempfile, shutil
#		curses module for status bar ??
#		"nltk" (?) for interpreter??
#		sqlite3 for DB?
#		check out "robotadventure" from end of 2013 presentation
#		how to eliminate eval()

# Decisions:
#		No need for curses in a flask app
#		Don't use nltk - is overkill (and besides, I want to write me own interpreter)
#		For now, don't use cmd - want more practice with classes
#		Do figure out how to avoid using eval()

# To Decide:
#		Rooms in JSON?
#		How to use DB??
#			- Since I'm designing a web game, I need to separate stateful and static

# Next to dos
# DONE: Figure out how to replace eval() w/ getattr() => use str_to_class() snippet
# DONE: Replace eval() usage w/ str_to_class()
# DONE: 'take' is broken post eval() remove
# DONE: 'take' removal logic doesn't check for item_obj being in container before attempting to remove it
# DONE: Why does close need to remove container items from room_obj? Old legacy logic
# DONE: Wouldn't it be a lot simpler if we just stored room_obj in stateful_dict rather than room_str ?
	# DONE: Try using .name property of Room instead of tracking room in stateful_dict
# DONE: Simplify open_cont_scan

# IN-PROC: new naming convention to clarify between room_obj and room_objects ?? Need a new term for "objects"
#		DONE: Sort out whole naming convention of name_type vs. name_objects (containter too)
#		DONE: room_objects => room_elements
#		DONE: items in room_elements loop => elements
#		IN-PROC: room_element => objects?
#			DONE: Initial troubleshooting in entrance
#			DONE: unlock, lock, open, close
#			DONE: Containers
#			DONE: What about directions / doors
#			TBD: Testing & Clean-up
# 	TBD: Maybe only for lst, dict, and obj?

# TBD: if type() => hasattrib
# TBD: Should hand and room_objects also contain actual objects instead of text? 
# TBD: Make examine scope check a function
# TBD: Can I buffer at the end of each method??
# TBD: Inventory command!!
# TBD: Put command

# Some Day Maybe
# TBD: Implment container.put(item) ???
# TBD: Is the Item class worth having???


# ****** Interpreter Thoughts #

# 0) DONE: Functionalize Interpreter and use out_buff
# 0.5) fix 'quit'
# 0.7 fix 'start'
# 1) Every noun as an obj_name, full_name, root_name
# 2) All one_word commands => 1_word function
# 3) use lists to identify words as nouns, verbs, adjectives, articles, and prepositions
# 4) if sentence does not start with a verb => please start with a verb
# 5) if multiple nouns, verbs, articles, or preps in a row => I don't undderstand that setence error
# 6) Convert adjectives + noun => obj_name
# 7) If no prep => verb_noun function
# 8) If prep: Identify direct object and => prep_sentence function
# NOTE: All room-based validation happens in the method - the Interpreter just converts English to method calls


# import statements
import cmd
import sys


# helper functions
def set_difference(a,b):
    return list(set(a)-set(b))

def buffer(stateful_dict, output):
		out_buff = stateful_dict['out_buff']
		out_buff = out_buff + output + "\n"
		stateful_dict['out_buff'] = out_buff

def open_cont_scan(stateful_dict, room_elements):
		container_lst = []
##		for element in room_elements:
		for element_obj in room_elements:
##				element_obj = str_to_class(element)
				if type(element_obj) == type(chest) \
								and len(element_obj.contains) > 0 \
								and element_obj.open_state == True:
						container_lst = container_lst + element_obj.contains
		return container_lst

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def objlst_to_strlst(obj_lst):
		str_lst = [] # new code for room_elements = objects
		for obj in obj_lst:
				str_lst.append(obj.name)
		return str_lst

# classes
class ViewOnly(object):
		def __init__(self, name, desc, writing):
				self.name = name
				self.desc = desc
				self.writing = writing

		def examine(self, stateful_dict):
				room_obj = stateful_dict['room_obj'] # room_obj
				hand = stateful_dict['hand']
				room_elements = room_obj.room_elements
				examine_lst = room_elements + hand
##				examine_lst.append(room_obj.name)
				examine_lst.append(room_obj)
				if hasattr(room_obj, 'features'):
						features = room_obj.features
						examine_lst = examine_lst + features
#				print(examine_lst) # used for troubleshooting

				container_obj = open_cont_scan(stateful_dict, room_elements)
				examine_lst = examine_lst + container_obj

##				if str(self.name) in examine_lst:
				if self in examine_lst:
						output = self.desc
						buffer(stateful_dict, output)
						if self.writing != 'null':
								output = "On the " + self.name + " you see: " + self.writing
								buffer(stateful_dict, output)
				else:
						output = "You can't see a " + self.name + " here."
						buffer(stateful_dict, output)
		
		def change_desc(self, new_desc):
				self.desc = new_desc

class Writing(ViewOnly):
		def __init__(self, name, desc, writing, written_on):
				super().__init__(name, desc, writing)
				self.written_on = written_on

		def read(self, stateful_dict):
				hand = stateful_dict['hand']
				room_obj = stateful_dict['room_obj']
				room_elements = room_obj.room_elements
				features = room_obj.features
				read_lst = room_elements + hand + features

				container_obj = open_cont_scan(stateful_dict, room_elements)
				read_lst = read_lst + container_obj

				if self.written_on in read_lst:
						output = self.desc
						buffer(stateful_dict, output)

class Room(ViewOnly):
		def __init__(self, name, desc, writing, features, room_elements, valid_paths, door_paths):
				super().__init__(name, desc, writing)
				self.features = features # list of non-items in room (can be examined but not taken)
				self.room_elements = room_elements # list of elements in room
				self.valid_paths = valid_paths # dictionary of {direction1 : room1, direction2 : room2}
				self.door_paths = door_paths # dictionary of {direction1 : door1}
			
		def examine(self, stateful_dict):
				super(Room, self).examine(stateful_dict)
				if stateful_dict['room_obj'] == self:
						room_lst = objlst_to_strlst(self.room_elements)
###						output = "The room contains: " + ', '.join(self.room_elements)
						output = "The room contains: " + ', '.join(room_lst)
						buffer(stateful_dict, output)

##				for element in self.room_elements:
				for element_obj in self.room_elements:
##						element_obj = str_to_class(element)
						if type(element_obj) == type(chest) \
										and len(element_obj.contains) > 0 \
										and element_obj.open_state == True:
								contains_lst = objlst_to_strlst(element_obj.contains)
###								contains_lst = [] # new code for room_elements = objects
###								for container_obj in element_obj:
###										contains_lst.append(element_obj.name)
##								output = "The " + element + " contains: " + ', '.join(element_obj.contains)
								output = "The " + element_obj.name + " contains: " + ', '.join(contains_lst)
								buffer(stateful_dict, output)

		def go(self, direction, stateful_dict):
				room_obj = stateful_dict['room_obj']
				if direction not in self.valid_paths:
						output = "You can't go that way."
						buffer(stateful_dict, output)
				elif direction in self.door_paths:
##						door_obj = str_to_class(self.door_paths[direction])
						door_obj = self.door_paths[direction]
						door_open = door_obj.open_state
						if not door_open:
##								output = "The " +  self.door_paths[direction] + " is closed."
								output = "The " +  self.door_paths[direction].name + " is closed."
								buffer(stateful_dict, output)
						else:
##								next_room = self.valid_paths[direction]
								next_room_obj = self.valid_paths[direction]
##								next_room_obj = str_to_class(next_room)
								stateful_dict['room_obj'] = next_room_obj # room_obj
								next_room_obj.examine(stateful_dict)


class Item(ViewOnly):
		def __init__(self, name, desc, writing, takeable):
				super().__init__(name, desc, writing)
				self.takeable = takeable
				
		def take(self, stateful_dict):
				room_obj = stateful_dict['room_obj']
				hand = stateful_dict['hand']
				room_elements = room_obj.room_elements
				can_take = room_elements

				container_obj = open_cont_scan(stateful_dict, room_elements)
				can_take = can_take + container_obj

##				if self.name in can_take and self.takeable:
				if self in can_take and self.takeable:
						if len(hand) == 0:
##								hand.append(self.name)
								hand.append(self)

								taken_from_container = False
##								for element in room_elements:
								for element_obj in room_elements:
##										element_obj = str_to_class(element)
										if type(element_obj) == type(chest) \
														and len(element_obj.contains) > 0 \
														and element_obj.open_state == True:
##												if self.name in element_obj.contains:
												if self in element_obj.contains:
##														element_obj.contains.remove(self.name)
														element_obj.contains.remove(self)
														taken_from_container = True

								if taken_from_container == False:
##										room_obj.room_elements.remove(self.name)
										room_obj.room_elements.remove(self)

								output = "Taken"
								buffer(stateful_dict, output)
						else:
								output = "Your hand is full."
								buffer(stateful_dict, output)
				else:
						output = "There's no " + self.name + " to take here!"
						buffer(stateful_dict, output)

		def drop(self, stateful_dict):
				room_obj = stateful_dict['room_obj']
				hand = stateful_dict['hand']
##				if self.name in hand:
				if self in hand:
##						hand.remove(self.name)
						hand.remove(self)
##						room_obj.room_elements.append(self.name)
						room_obj.room_elements.append(self)
						output = "Dropped"
						buffer(stateful_dict, output)
				else:
						output = "You're not holding the " + self.name + " in your hand."
						buffer(stateful_dict, output)

class Door(ViewOnly):
		def __init__(self, name, desc, writing, open_state, unlock_state, key):
				super().__init__(name, desc, writing)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key

		def examine(self, stateful_dict):
				super(Door, self).examine(stateful_dict)
				room_obj = stateful_dict['room_obj'] # room_obj
				room_elements = room_obj.room_elements
##				if self.name in room_elements:
				if self in room_elements:
						if self.open_state:
								output = "The " + self.name + " is open."
								buffer(stateful_dict, output)
								if hasattr(self, 'contains'):
										if len(self.contains) == 0:
												output = "The " + self.name + " is empty."
												buffer(stateful_dict, output)
										else:
												contains_lst = objlst_to_strlst(self.contains)
##												output = "The " + self.name + "contains: "  + ', '.join(self.contains)
												output = "The " + self.name + "contains: "  + ', '.join(contains_lst)
												buffer(stateful_dict, output)
						else:
								output = "The " + self.name + " is closed."
								buffer(stateful_dict, output)

		def unlock(self, stateful_dict):
				hand = stateful_dict['hand']
				if self.unlock_state == False:
						if self.key in hand:
								output = "Unlocked"
								buffer(stateful_dict, output)
								self.unlock_state = True
						else:
								output = "You aren't holding the key."
								buffer(stateful_dict, output)
				else:
						output = "The " + self.name + " is already unlocked."
						buffer(stateful_dict, output)

		def open(self, stateful_dict):
				if self.open_state == False:
						if self.unlock_state == True:
								self.open_state = True
								output = "Openned"
								buffer(stateful_dict, output)
								if hasattr(self, 'contains'):
										if len(self.contains) == 0:
												output = "The " + self.name + " is empty."
												buffer(stateful_dict, output)
										else:
												contains_lst = objlst_to_strlst(self.contains)
##												output = "The " + self.name + " contains: " + ', '.join(self.contains)
												output = "The " + self.name + " contains: " + ', '.join(contains_lst)
												buffer(stateful_dict, output)
						else:
								output = "The " + self.name + " is locked."
								buffer(stateful_dict, output)
				else:
						output = "The " + self.name + " is already open."
						buffer(stateful_dict, output)

		def close(self, stateful_dict):
				if self.open_state:
						self.open_state = False
						output = "Closed"
						buffer(stateful_dict, output)
				else:
						output = "The " + self.name + " is already closed."
						buffer(stateful_dict, output)

		def lock(self, stateful_dict):
				if self.open_state == False:
						hand = stateful_dict['hand']
						if self.key in hand:
								if self.unlock_state:
										output = "Locked"
										buffer(stateful_dict, output)
										self.unlock_state = False
								else:
										output = "The " + self.name + " is already locked."
										buffer(stateful_dict, output)
						else:
								output = "You aren't holding the key."
								buffer(stateful_dict, output)
				else:
						output = "You can't lock something that's open."
						buffer(stateful_dict, output)

class Container(Door):
		def __init__(self, name, desc, writing, open_state, unlock_state, key, takeable, contains):
				super().__init__(name, desc, writing, open_state, unlock_state, key)
				self.takeable = takeable # can the container be taken?
				self.contains = contains # list of items in the container


# object instantiation
dark_castle = ViewOnly('dark_castle', 'The evil Dark Castle looms above you', 'null')

rusty_key = Item('rusty_key', 'The key is rusty', 'null', True)
sword = Item('sword','The sword is shiny.', 'dwarven_runes', True)
brass_key = Item('brass_key', 'The key is brass', 'null', True)
potion = Item('potion', 'The cork-stopperd glass vial contains a bubbly green potion', 'null', True)

chest = Container('chest', 'An old wooden chest', 'null',
		False, False, brass_key, False, [potion])
# giftbox = Container('giftbox', 'A pretty gift box', 'null',
#		False, True, 'none', True, [necklace])

gate = Door('gate', 'The front gate is massive and imposing',
		'rusty_letters', False, False, rusty_key)
#screen_door = Door('screen_door', "You should never be able to examine the screen_door",
#		'null', False, False, chrome_key)

rusty_letters = Writing('rusty_letters', 'Abandon Hope All Ye Who Even Thank About It', 'null', gate)
dwarven_runes = Writing('dwarven_runes', "Goblin Wallopper", 'null', sword)

entrance = Room('entrance',
		'Entrance\nYou stand before the daunting gate of Dark Castle. In front of you is the gate',
		'null', [dark_castle], [rusty_key, gate], {'north' : 'main_hall'}, {'north' : gate})
main_hall = Room('main_hall',
		'Main Hall\nA vast and once sumptuous chamber. The main gate is south. There is a passage going north.',
		'null', [], [sword, gate, brass_key, chest], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : gate})

# next room definitions after room definitions to avoid undefined variables
entrance.valid_paths['north'] = main_hall
main_hall.valid_paths['south'] = entrance


# stateful dictionary of persistent values
stateful_dict = {
		'hand' : [], 
		'backpack' : [],
		'room_obj' : entrance,
		'out_buff' : ""
		}


# interpreter function
def interpreter(stateful_dict, user_input):
		room_obj = stateful_dict['room_obj']
		lst = []
		lst.append(user_input)
		user_input_lst = lst[0].split()
		word1 = user_input_lst[0].lower()
		if len(user_input_lst) > 1:
				word2 = user_input_lst[1].lower()
		else:
				word2 = "blank"
		if word1 == 'go':
				getattr(room_obj, word1)(word2, stateful_dict)
		elif word1 == 'look':
				room_obj.examine(stateful_dict)
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
# print("TEST: " + stateful_dict['room_obj'].desc)
# rusty_key.take(stateful_dict)


# start text
entrance.examine(stateful_dict)
print("START: " + stateful_dict['out_buff'])
# gate.lock(stateful_dict) # troubleshooting text


# main loop
while True:
#    print(stateful_dict) # troubleshooting text
		stateful_dict['out_buff'] = ""
		user_input = input('Type your command: ')
		if user_input == "quit":
				print("Goodbye!")
				break
		interpreter(stateful_dict, user_input)
		print("BUFFER: " + stateful_dict['out_buff'])


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
# print(eval(room).room_elements)


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

