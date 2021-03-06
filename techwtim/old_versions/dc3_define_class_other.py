# NO LONGER IN USE IN v3.42

# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 5, 2021
# description: class deffinition module


# import
import sys
import random
from dc3_static_init import *
from dc3_helper import *
import gc

# classes

print("define_class_other - start")

class Writing(object):
		def __init__(self, name, full_name, root_name, descript_key):
				self._name = name
				self._full_name = full_name
				self._root_name = root_name
				self._descript_key = descript_key

#		global game_state

		@property
		def name(self):
				return self._name

		@property
		def full_name(self):
				return self._full_name

		@property
		def root_name(self):
				return self._root_name

		@property
		def descript_key(self):
				return self._descript_key

		def get_descript_str(self, stateful_dict):
#		def get_descript_str(self):
#				if active_gs.dynamic_desc_key_exists(self.descript_key):
#						descript_str = active_gs.get_dynamic_desc_dict(self.descript_key)
				try:
						descript_str = stateful_dict['dynamic_desc_dict'][self.descript_key]
#				else:
				except:
						descript_str = descript_dict[self.descript_key]
				return descript_str

		def is_container(self):
					return hasattr(self, 'contains')

		def	print_contents_str(self, stateful_dict):
				if self.is_container() and self.open_state == True:
						container_str = obj_lst_to_str(self.contains)
						buffer(stateful_dict, "The " + self.full_name + " contains: " + container_str)

		def read(self, stateful_dict):
				buffer(stateful_dict, self.get_descript_str(stateful_dict))

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

class ViewOnly(Writing):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key)
				self._writing = writing

		@property
		def writing(self):
				return self._writing

		def has_writing(self):
				return (self.writing is not None)

		def examine(self, stateful_dict):
				buffer(stateful_dict, self.get_descript_str(stateful_dict))
				if self.has_writing():
						output = "On the " + self.full_name + " you see: " + self.writing.full_name
						buffer(stateful_dict, output)

class Room(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, features, room_obj_lst, door_paths):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._features = features # list of non-items in room (can be examined but not taken)
				self._room_obj_lst = room_obj_lst # list of obj in the room that the player can interact with
				self._door_paths = door_paths # dictionary of {direction1 : door1}

		@property
		def features(self):
				return self._features

		@property
		def room_obj_lst(self):
				return self._room_obj_lst

		@property
		def door_paths(self):
				return self._door_paths
		
		def	door_in_path(self, direction):
				return direction in self.door_paths

		def get_door(self, direction):
				return self.door_paths[direction]

		def examine(self, stateful_dict):
				super(Room, self).examine(stateful_dict)
				room_str = obj_lst_to_str(self.room_obj_lst)
				buffer(stateful_dict, "The room contains: " + room_str)
				for obj in self.room_obj_lst:
						obj.print_contents_str(stateful_dict)

		def go(self, direction, stateful_dict, active_gs):
#		def go(self, direction, stateful_dict):
				room_obj = stateful_dict['room']
#				if direction not in stateful_dict['paths'][room_obj.name]:
				if not active_gs.is_valid_map_direction(room_obj, direction):
						num = random.randint(0, 4)
						wrong_way_key = 'wrong_way_' + str(num)
						buffer(stateful_dict, descript_dict[wrong_way_key])
				elif self.door_in_path(direction):
						door_obj = self.get_door(direction)
						door_open = door_obj.open_state
						if not door_open:
								buffer(stateful_dict, "The " +  door_obj.full_name + " is closed.")
						else:
#								next_room_obj = stateful_dict['paths'][room_obj.name][direction]
								next_room_obj = active_gs.get_next_room(room_obj, direction)
								print(next_room_obj) # troubleshooting
								print(id(next_room_obj))
								stateful_dict['room'] = next_room_obj
								next_room_obj.examine(stateful_dict)
				else:
#						next_room_obj = stateful_dict['paths'][room_obj.name][direction]
						next_room_obj = active_gs.get_next_room(room_obj, direction)
						print(next_room_obj) # troubleshooting
						print(id(next_room_obj))
						stateful_dict['room'] = next_room_obj
						next_room_obj.examine(stateful_dict)

class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, takable):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self.takable = takable

		def take(self, stateful_dict):
				room_obj = stateful_dict['room']
				hand_lst = stateful_dict['hand']
				backpack_lst = stateful_dict['backpack']
				room_obj_lst = room_obj.room_obj_lst
				if self in hand_lst:
						buffer(stateful_dict, "You're already holding the " + self.full_name)
				elif self.takable == False:
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
								room_obj.room_obj_lst.remove(self)
						else:
								for obj in room_obj_lst: # else remove item from container it's in
										if obj.is_container():
												if self in obj.contains:
														obj.contains.remove(self)

		def drop(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				room_obj = stateful_dict['room']
				if self not in hand_lst:
						output = "You're not holding the " + self.full_name + " in your hand."
						buffer(stateful_dict, output)
				else:
						hand_lst.remove(self)
						stateful_dict['hand'] = hand_lst
						room_obj.room_obj_lst.append(self)
						buffer(stateful_dict, "Dropped")

class Door(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, open_state, unlock_state, key):
				super().__init__(name, full_name, root_name, descript_key, writing)
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

		def unlock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if self.unlock_state == True:
						buffer(stateful_dict, "The " + self.full_name + " is already unlocked.")
				elif self.key is None:
						buffer(stateful_dict, "You don't see a keyhole for this door.")
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				else:
						buffer(stateful_dict, "Unlocked")
						self.unlock_state = True

		def open(self, stateful_dict):
				if self.open_state == True:
						buffer(stateful_dict, "The " + self.full_name + " is already open.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is locked.")
				else:
						self.open_state = True
						buffer(stateful_dict, "Openned")

		def close(self, stateful_dict):
				if self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is already closed.")
				elif self.unlock_state == False: # for Iron Portcullis
						buffer(stateful_dict, "The " + self.full_name + " is locked.")
				else:
						self.open_state = False
						buffer(stateful_dict, "Closed")

		def lock(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if self.open_state == True:
						buffer(stateful_dict, "You can't lock something that's open.")						
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is already locked.")
				else:
						buffer(stateful_dict, "Locked")
						self.unlock_state = False

class Container(Door):
		def __init__(self, name, full_name, root_name, descript_key, writing, open_state, unlock_state, key, takable, contains):
				super().__init__(name, full_name, root_name, descript_key, writing, open_state, unlock_state, key)
				self.takable = takable # can the container be taken? Note: As Room class is currently coded, containers CANNOT be taken
				self.contains = contains # list of items in the container

		def examine(self, stateful_dict):
				super(Container, self).examine(stateful_dict)
				self.print_contents_str(stateful_dict)

		def open(self, stateful_dict):
				super(Container, self).open(stateful_dict)
				self.print_contents_str(stateful_dict)

		def put(self, obj, stateful_dict):
				hand_lst = stateful_dict['hand']
				if obj not in hand_lst:
						buffer(stateful_dict, "You aren't holding the " + obj.full_name)
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is closed.")
				elif obj.is_container():
						buffer(stateful_dict, "You can't put a container in a container")
				else:
						hand_lst.remove(obj)
						stateful_dict['hand'] = hand_lst
						self.contains.append(obj)
						buffer(stateful_dict, "Done")
						
class Food(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, takable, eat_desc_key):
				super().__init__(name, full_name, root_name, descript_key, writing, takable)
				self.eat_desc_key = eat_desc_key # keys to description of eating food (stored in descript_dict)

		def eat(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if self not in hand_lst:
						output = "You're not holding the " + self.full_name + " in your hand."
						buffer(stateful_dict, output)
				else:
						hand_lst.remove(self)
						stateful_dict['hand'] = hand_lst
						buffer(stateful_dict, "Eaten. The " + self.full_name + " " + descript_dict[self.eat_desc_key])

class Jug(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, takable, open_state, contains):
				super().__init__(name, full_name, root_name, descript_key, writing, takable)
				self.open_state = open_state # is the jug uncapped?
				self.contains = contains # obj in the jug

		def examine(self, stateful_dict):
				super(Jug, self).examine(stateful_dict)
				self.print_contents_str(stateful_dict)

class Beverage(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, drink_descript_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self.drink_desc_key = drink_descript_key # key to description of drinking the beverage (stored in descript_dict)

		def drink(self, stateful_dict):
				hand_lst = stateful_dict['hand']
				if (len(hand_lst) == 0) or (hand_lst[0].is_container() == False):
						output = "You don't seem to be holding a container of " + self.full_name + " in your hand."
						buffer(stateful_dict, output)
				elif self not in hand_lst[0].contains:
						output = "The container in your hand doesn't contain " + self.full_name + "."
						buffer(stateful_dict, output)
				else:
						hand_lst[0].contains.remove(self)
						buffer(stateful_dict, "Drunk. The " + self.full_name + " " + descript_dict[self.drink_desc_key])

print("defin_class_other - end")
