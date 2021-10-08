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

print("define_class_gs - start")

class GameState(object):
		def __init__(self, name, dynamic_desc_dict, map_dict, static_obj_dict, state_dict):
				self._name = name
				self._dynamic_desc_dict = dynamic_desc_dict
				self._map_dict = map_dict
				self._static_obj_dict = static_obj_dict
				self._state_dict = state_dict

		def dynamic_desc_key_exists(self, dynamic_desc_key):
				return dynamic_desc_key in self._dynamic_desc_dict

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
#				return direction in game_state._map_dict[room_obj.name]
				return direction in self._map_dict[room_obj.name]

		def get_next_room(self, room_obj, direction):
#				next_room = game_state._map_dict[room_obj.name][direction]
				next_room = self._map_dict[room_obj.name][direction]

				print("get_next_room: next room id is " + str(id(next_room)))
				print("The active_gs id of antechamber (from main_hall) is " + str(id(self._map_dict['main_hall']['north'])))

				return next_room

		def __repr__(self):
				return f'Object { self._name } is of class { type(self).__name__ } '

