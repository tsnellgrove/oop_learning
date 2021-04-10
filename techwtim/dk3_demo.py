# program: dark castle v3
# name: Tom Snellgrove
# date: Apr 10, 2021
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

def scope_check(obj, stateful_dict, do_output):
		room_obj = stateful_dict['room']
		hand_lst = stateful_dict['hand']
		room_obj_lst = room_obj.room_stuff
		open_cont_obj_lst = open_cont_scan(stateful_dict, room_obj_lst)
		scope_lst = room_obj_lst + hand_lst + open_cont_obj_lst
		scope_lst.append(room_obj)
		if hasattr(room_obj, 'features'):
				features_lst = room_obj.features
				scope_lst = scope_lst + features_lst
		if obj in scope_lst:
				in_scope = True
		else:
				in_scope = False
				if do_output:
						buffer(stateful_dict, "You can't see a " + obj.name + " here.")
		return in_scope

def container_desc(cont_obj, stateful_dict):
		if len(cont_obj.contains) == 0:
				buffer(stateful_dict, "The " + cont_obj.name + " is empty.")
		else:
				cont_str_lst = objlst_to_strlst(cont_obj.contains)
				output = "The " + cont_obj.name + " contains: "  + ', '.join(cont_str_lst)
				buffer(stateful_dict, output)


# classes
class ViewOnly(object):
		def __init__(self, name, desc, writing):
				self.name = name
				self.desc = desc
				self.writing = writing

		def examine(self, stateful_dict):
				if scope_check(self, stateful_dict, do_output=True):
						buffer(stateful_dict, self.desc)
						if self.writing is not None:
								output = "On the " + self.name + " you see: " + self.writing.name
								buffer(stateful_dict, output)

class Writing(ViewOnly):
		def __init__(self, name, desc, writing, written_on):
				super().__init__(name, desc, writing)
				self.written_on = written_on

		def read(self, stateful_dict):
				if scope_check(self.written_on, stateful_dict, do_output=False):
						buffer(stateful_dict, self.desc)
				else:
						buffer(stateful_dict, "You can't see any " + self.name + " here.")

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
				room_obj_lst = room_obj.room_stuff

				if scope_check(self, stateful_dict, do_output=True):
						if self.takeable:
								if len(hand_lst) == 0:
										hand_lst.append(self)
										if self in room_obj_lst:
												room_obj.room_stuff.remove(self)
										else:
												for obj in room_obj_lst:
														if hasattr(obj, 'contains') \
																		and len(obj.contains) > 0 \
																		and obj.open_state == True:
																if self in obj.contains:
																		obj.contains.remove(self)
										buffer(stateful_dict, "Taken")
								else:
										buffer(stateful_dict, "Your hand is full.")
						else:
								buffer(stateful_dict, "You can't take the " + self.name)

		def drop(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				room_obj = stateful_dict['room']
				if scope_check(self, stateful_dict, do_output=True):
						if self in hand_lst:
								hand_lst.remove(self)
								room_obj.room_stuff.append(self)
								buffer(stateful_dict, "Dropped")
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
				if scope_check(self, stateful_dict, do_output=False):
						if self.open_state:
								buffer(stateful_dict, "The " + self.name + " is open.")
								if hasattr(self, 'contains'):
										container_desc(self, stateful_dict)
						else:
								buffer(stateful_dict, "The " + self.name + " is closed.")

		def unlock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if scope_check(self, stateful_dict, do_output=True):
						if self.unlock_state == False:
								if self.key in hand_lst:
										buffer(stateful_dict, "Unlocked")
										self.unlock_state = True
								else:
										buffer(stateful_dict, "You aren't holding the key.")
						else:
								buffer(stateful_dict, "The " + self.name + " is already unlocked.")

		def open(self, stateful_dict):
				if scope_check(self, stateful_dict, do_output=True):
						if self.open_state == False:
								if self.unlock_state == True:
										self.open_state = True
										buffer(stateful_dict, "Openned")
										if hasattr(self, 'contains'):
												container_desc(self, stateful_dict)
								else:
										buffer(stateful_dict, "The " + self.name + " is locked.")
						else:
								buffer(stateful_dict, "The " + self.name + " is already open.")

		def close(self, stateful_dict):
				if scope_check(self, stateful_dict, do_output=True):
						if self.open_state:
								self.open_state = False
								buffer(stateful_dict, "Closed")
						else:
								buffer(stateful_dict, "The " + self.name + " is already closed.")

		def lock(self, stateful_dict):
				if scope_check(self, stateful_dict, do_output=True):
						if self.open_state == False:
								hand_lst = stateful_dict['hand']
								if self.key in hand_lst:
										if self.unlock_state:
												buffer(stateful_dict, "Locked")
												self.unlock_state = False
										else:
												buffer(stateful_dict, "The " + self.name + " is already locked.")
								else:
										buffer(stateful_dict, "You aren't holding the key.")
						else:
								buffer(stateful_dict, "You can't lock something that's open.")

class Container(Door):
		def __init__(self, name, desc, writing, open_state, unlock_state, key, takeable, contains):
				super().__init__(name, desc, writing, open_state, unlock_state, key)
				self.takeable = takeable # can the container be taken?
				self.contains = contains # list of items in the container


# object instantiation
dark_castle = ViewOnly('dark_castle', 'The evil Dark Castle looms above you', None)

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
		None, [dark_castle], [rusty_key, gate], {'north' : 'main_hall'}, {'north' : gate})
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
		'backpack' : [],
		'room' : entrance,
		'out_buff' : ""
		}


# interpreter function
def interpreter(stateful_dict, user_input):
		room_obj = stateful_dict['room']
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
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
# sword.examine(stateful_dict)


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
		print(stateful_dict['out_buff'])


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

