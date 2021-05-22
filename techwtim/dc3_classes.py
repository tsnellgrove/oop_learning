# program: dark castle v3
# name: Tom Snellgrove
# date: May 13, 2021
# description: class deffinition module for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter


# import
from dc3_helper import *


# classes
class ViewOnly(object):
		def __init__(self, name, full_name, root_name, desc, writing):
				self.name = name
				self.full_name = full_name
				self.root_name = root_name
				self.desc = desc
				self.writing = writing

		def __str__(self): # DOESN'T WORK
				return '{self.name}'.format(self=self)

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
						stateful_dict['hand'] = hand_lst
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

		def put(self, obj, stateful_dict):
				hand_lst = stateful_dict['hand']
				if len(hand_lst) > 0:
						hand_str = hand_lst[0].name
				print(hand_lst)
				print(self, obj)
				print(hand_str)
				if scope_check(self, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + self.full_name + " here.")
				elif scope_check(obj, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + obj.full_name + " here.")
				elif len(hand_lst) == 0:
						buffer(stateful_dict, "Your hand is empty")
				elif obj != hand_str:
						buffer(stateful_dict, "You aren't holding the " + obj.full_name)
##				elif obj in hand_lst == False:
##						buffer(stateful_dict, "You aren't holding the " + obj.full_name)
				elif self.open_state == False:
						buffer(stateful_dict, "The " + self.full_name + " is closed.")
				elif hasattr(obj, 'contains'):
						buffer(stateful_dict, "You can't put a container in a container")
				else:
						hand_lst.remove(obj)
						stateful_dict['hand'] = hand_lst
						self.contains.append(obj)
						buffer(stateful_dict, "Done")
						

