# program: dark castle v3.44
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: class deffinition module


# import
import sys
import random
from dc3_static_init import *
from dc3_helper import *


# classes
class GameState(object):
		def __init__(self, name, dynamic_desc_dict, map_dict, points_earned_dict, static_obj_dict, state_dict):
				self._name = name
				self._dynamic_desc_dict = dynamic_desc_dict
				self._map_dict = map_dict
				self._points_earned_dict = points_earned_dict
				self._static_obj_dict = static_obj_dict
				self._state_dict = state_dict

		def get_dynamic_desc_dict(self, dynamic_desc_key):
				if dynamic_desc_key not in self._dynamic_desc_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._dynamic_desc_dict[dynamic_desc_key]

		def set_dynamic_desc_dict(self, dynamic_desc_key, dynamic_desc_str):
				if dynamic_desc_key not in self._dynamic_desc_dict:
						raise KeyError("key does not exist in dict")
				else:
						self._dynamic_desc_dict[dynamic_desc_key] = dynamic_desc_str

		def is_valid_map_direction(self, room_obj, direction):
				return direction in self._map_dict[room_obj.name]

		def get_next_room(self, room_obj, direction):
				next_room = self._map_dict[room_obj.name][direction]
				return next_room

		def get_points_earned_state(self, score_key):
				if score_key not in self._points_earned_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._points_earned_dict[score_key]

		def set_points_earned_state(self, score_key, value):
				if score_key not in self._points_earned_dict:
						raise KeyError("key does not exist in dict")
				else:
						self._points_earned_dict[score_key] = value

		def update_score(self, points):
				self._state_dict['score'] += points 

		def get_score(self):
				return self._state_dict['score']

		def move_inc(self):
				self._state_dict['move_counter'] += 1

		def move_dec(self):
				self._state_dict['move_counter'] -= 1

		def get_moves(self):
				return self._state_dict['move_counter']

		def get_end_of_game(self):
				return self._state_dict['end_of_game']

		def set_end_of_game(self, value):
				self._state_dict['end_of_game'] = value

		def get_game_ending(self):
				return self._state_dict['game_ending']

		def set_game_ending(self, value):
				self._state_dict['game_ending'] = value

		def get_backpack_lst(self):
				return self._state_dict['backpack']

		def backpack_lst_append_item(self, item):
				self._state_dict['backpack'].append(item)

		def backpack_lst_remove_item(self, item):
				self._state_dict['backpack'].remove(item)

		def get_hand_lst(self):
				return self._state_dict['hand']

		def hand_lst_append_item(self, item):
				self._state_dict['hand'].append(item)

		def hand_lst_remove_item(self, item):
				self._state_dict['hand'].remove(item)

		def get_static_obj(self, static_key):
				if static_key not in self._static_obj_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._static_obj_dict[static_key]

		def get_room(self):
				return self._state_dict['room']

		def set_room(self, value):
				self._state_dict['room'] = value

		def get_buff(self):
				return self._state_dict['out_buff']

		def buffer(self, output_str):
				out_buff_old = self._state_dict['out_buff']
				out_buff_new = out_buff_old + "\n" + output_str + "\n"
				self._state_dict['out_buff'] = out_buff_new

		def reset_buff(self):
				self._state_dict['out_buff'] = ""

		def __repr__(self):
				return f'Object { self._name } is of class { type(self).__name__ } '

class Writing(object):
		def __init__(self, name, full_name, root_name, descript_key):
				self._name = name
				self._full_name = full_name
				self._root_name = root_name
				self._descript_key = descript_key

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

		def get_descript_str(self, stateful_dict, active_gs):
				try:
						descript_str = active_gs.get_dynamic_desc_dict(self.descript_key)
				except:
						descript_str = descript_dict[self.descript_key]
				return descript_str

		def is_container(self):
					return hasattr(self, 'contains')

		def	print_contents_str(self, stateful_dict, active_gs):
				if self.is_container() and self.open_state == True:
						container_str = obj_lst_to_str(self.contains)
						active_gs.buffer("The " + self.full_name + " contains: " + container_str)
#						buffer(stateful_dict, "The " + self.full_name + " contains: " + container_str)

		def read(self, stateful_dict, active_gs):
				descript_str = self.get_descript_str(stateful_dict, active_gs)
#				buffer(stateful_dict, descript_str)
				active_gs.buffer(descript_str)

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

		def examine(self, stateful_dict, active_gs):
				descript_str = self.get_descript_str(stateful_dict, active_gs)
#				buffer(stateful_dict, descript_str)
				active_gs.buffer(descript_str)
				if self.has_writing():
						output = "On the " + self.full_name + " you see: " + self.writing.full_name
#						buffer(stateful_dict, output)
						active_gs.buffer(output)

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

		def examine(self, stateful_dict, active_gs):
				super(Room, self).examine(stateful_dict, active_gs)
				room_str = obj_lst_to_str(self.room_obj_lst)
#				buffer(stateful_dict, "The room contains: " + room_str)
				active_gs.buffer("The room contains: " + room_str)
				for obj in self.room_obj_lst:
						obj.print_contents_str(stateful_dict, active_gs)

		def go(self, direction, stateful_dict, active_gs):
				room_obj = active_gs.get_room()
				if not active_gs.is_valid_map_direction(room_obj, direction):
						num = random.randint(0, 4)
						wrong_way_key = 'wrong_way_' + str(num)
#						buffer(stateful_dict, descript_dict[wrong_way_key])
						active_gs.buffer(descript_dict[wrong_way_key])
				elif self.door_in_path(direction):
						door_obj = self.get_door(direction)
						door_open = door_obj.open_state
						if not door_open:
#								buffer(stateful_dict, "The " +  door_obj.full_name + " is closed.")
								active_gs.buffer("The " +  door_obj.full_name + " is closed.")
						else:
								next_room_obj = active_gs.get_next_room(room_obj, direction)
								active_gs.set_room(next_room_obj)
								next_room_obj.examine(stateful_dict, active_gs)
				else:
						next_room_obj = active_gs.get_next_room(room_obj, direction)
						active_gs.set_room(next_room_obj)
						next_room_obj.examine(stateful_dict, active_gs)

class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, takable):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self.takable = takable

		def take(self, stateful_dict, active_gs):
				room_obj = active_gs.get_room()
				hand_lst = active_gs.get_hand_lst()
				backpack_lst = active_gs.get_backpack_lst()
				room_obj_lst = room_obj.room_obj_lst
				if self in hand_lst:
#						buffer(stateful_dict, "You're already holding the " + self.full_name)
						active_gs.buffer("You're already holding the " + self.full_name)
				elif self.takable == False:
#						buffer(stateful_dict, "You can't take the " + self.full_name)
						active_gs.buffer("You can't take the " + self.full_name) # eliminate Takable attribute?
				else:
						if len(hand_lst) > 0: # if hand not empty move item to backpack
								active_gs.backpack_lst_append_item(hand_lst[0])
								active_gs.hand_lst_remove_item(hand_lst[0])
						active_gs.hand_lst_append_item(self) # put taken item in hand
#						buffer(stateful_dict, "Taken")
						active_gs.buffer("Taken")
						if self in backpack_lst: # if taken from backpack, remove from backpack
								active_gs.backpack_lst_remove_item(self)					
						elif self in room_obj_lst: # if taken from room, remove from room
								room_obj.room_obj_lst.remove(self)
						else:
								for obj in room_obj_lst: # else remove item from container it's in
										if obj.is_container():
												if self in obj.contains:
														obj.contains.remove(self)

		def drop(self, stateful_dict, active_gs):
				hand_lst = active_gs.get_hand_lst()
				room_obj = active_gs.get_room()
				if self not in hand_lst:
						output = "You're not holding the " + self.full_name + " in your hand."
#						buffer(stateful_dict, output)
						active_gs.buffer(output)
				else:
						active_gs.hand_lst_remove_item(self)
						room_obj.room_obj_lst.append(self)
#						buffer(stateful_dict, "Dropped")
						active_gs.buffer("Dropped")

class Door(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, open_state, unlock_state, key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key

		def examine(self, stateful_dict, active_gs):
				super(Door, self).examine(stateful_dict, active_gs)
				if self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is closed.")
				else:
						buffer(stateful_dict, "The " + self.full_name + " is open.")

		def unlock(self, stateful_dict, active_gs):
				hand_lst = active_gs.get_hand_lst()
				if self.unlock_state == True:
						buffer(stateful_dict, "The " + self.full_name + " is already unlocked.")
				elif self.key is None:
						buffer(stateful_dict, "You don't see a keyhole for this door.")
				elif self.key not in hand_lst:
						buffer(stateful_dict, "You aren't holding the key.")
				else:
						buffer(stateful_dict, "Unlocked")
						self.unlock_state = True

		def open(self, stateful_dict, active_gs):
				if self.open_state == True:
						buffer(stateful_dict, "The " + self.full_name + " is already open.")
				elif self.unlock_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is locked.")
				else:
						self.open_state = True
						buffer(stateful_dict, "Openned")

		def close(self, stateful_dict, active_gs):
				if self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is already closed.")
				elif self.unlock_state == False: # for Iron Portcullis
						buffer(stateful_dict, "The " + self.full_name + " is locked.")
				else:
						self.open_state = False
						buffer(stateful_dict, "Closed")

		def lock(self, stateful_dict, active_gs):
				hand_lst = active_gs.get_hand_lst()
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

		def examine(self, stateful_dict, active_gs):
				super(Container, self).examine(stateful_dict, active_gs)
				self.print_contents_str(stateful_dict, active_gs)

		def open(self, stateful_dict, active_gs):
				super(Container, self).open(stateful_dict, active_gs)
				self.print_contents_str(stateful_dict, active_gs)

		def put(self, obj, stateful_dict, active_gs):
				hand_lst = active_gs.get_hand_lst()
				if obj not in hand_lst:
						buffer(stateful_dict, "You aren't holding the " + obj.full_name)
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is closed.")
				elif obj.is_container():
						buffer(stateful_dict, "You can't put a container in a container")
				else:
						active_gs.hand_lst_remove_item(obj)
						self.contains.append(obj)
						buffer(stateful_dict, "Done")
						
class Food(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, takable, eat_desc_key):
				super().__init__(name, full_name, root_name, descript_key, writing, takable)
				self.eat_desc_key = eat_desc_key # keys to description of eating food (stored in descript_dict)

		def eat(self, stateful_dict, active_gs):
				hand_lst = active_gs.get_hand_lst()
				if self not in hand_lst:
						output = "You're not holding the " + self.full_name + " in your hand."
						buffer(stateful_dict, output)
				else:
						active_gs.hand_lst_remove_item(self)
						buffer(stateful_dict, "Eaten. The " + self.full_name + " " + descript_dict[self.eat_desc_key])

class Jug(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, takable, open_state, contains):
				super().__init__(name, full_name, root_name, descript_key, writing, takable)
				self.open_state = open_state # is the jug uncapped?
				self.contains = contains # obj in the jug

		def examine(self, stateful_dict, active_gs):
				super(Jug, self).examine(stateful_dict, active_gs)
				self.print_contents_str(stateful_dict, active_gs)

class Beverage(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, drink_descript_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self.drink_desc_key = drink_descript_key # key to description of drinking the beverage (stored in descript_dict)

		def drink(self, stateful_dict, active_gs):
				hand_lst = active_gs.get_hand_lst()
				if (len(hand_lst) == 0) or (hand_lst[0].is_container() == False):
						output = "You don't seem to be holding a container of " + self.full_name + " in your hand."
						buffer(stateful_dict, output)
				elif self not in hand_lst[0].contains:
						output = "The container in your hand doesn't contain " + self.full_name + "."
						buffer(stateful_dict, output)
				else:
						hand_lst[0].contains.remove(self)
						buffer(stateful_dict, "Drunk. The " + self.full_name + " " + descript_dict[self.drink_desc_key])

