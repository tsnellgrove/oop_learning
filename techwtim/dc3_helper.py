# program: dark castle v3.44
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: helper function module


### imports ###
from dc3_static_init import *


### NOT IN USE ###
def set_difference(a,b):
    return list(set(a)-set(b))

def change_desc(self, new_desc):
		self.desc = new_desc


### Only Used by Helper Functions ###
def open_cont_scan(stateful_dict, room_containers):
		open_cont_obj_lst = []
		for obj in room_containers:
				if len(obj.contains) > 0 and obj.open_state == True:
						open_cont_obj_lst = open_cont_obj_lst + obj.contains
		return open_cont_obj_lst

def scope_list(stateful_dict):
		room_obj = stateful_dict['room']
		hand_lst = stateful_dict['hand']
		backpack_lst = stateful_dict['backpack']
		universal_lst = stateful_dict['universal']
		room_obj_lst = room_obj.room_obj_lst
		features_lst = room_obj.features
		scope_lst = (room_obj_lst + hand_lst + backpack_lst 
						+ universal_lst + features_lst)
		room_containers = []
		for obj in scope_lst:
				if hasattr(obj, 'contains'):
						room_containers.append(obj)
		open_cont_obj_lst = open_cont_scan(stateful_dict, room_containers)
		scope_lst = scope_lst + open_cont_obj_lst
		scope_lst.append(room_obj)
		return scope_lst

### Called by Other Modules ###
def buffer(stateful_dict, output_str):
		out_buff = stateful_dict['out_buff']
		out_buff = out_buff + "\n" + output_str + "\n"
		stateful_dict['out_buff'] = out_buff

def obj_lst_to_str(obj_lst):
		if not isinstance(obj_lst, list):
				raise ValueError("is not a list")
		elif len(obj_lst) == 0:
				lst_str = "nothing"
		else:
				lst_str = ""
				for obj in obj_lst:
						lst_str = lst_str + obj.full_name + ", "
				lst_str = lst_str[:-2]
		return lst_str

def scope_check(obj, stateful_dict):
		scope_lst = scope_list(stateful_dict)
		return obj in scope_lst

def writing_check(writing, stateful_dict):
		scope_lst = scope_list(stateful_dict)
		writing_found = False
		for obj in scope_lst:
				if obj.writing == writing:
						writing_found = True
		return writing_found

def print_score(stateful_dict, active_gs):
		output1 = ("Your score is now " + str(active_gs.get_score()))
		output2 = (" out of " + str(static_dict['max_score']))
		buffer(stateful_dict, output1 + output2)

def inventory(stateful_dict):
		hand_obj_lst = stateful_dict['hand']
		hand_str = obj_lst_to_str(hand_obj_lst)
		buffer(stateful_dict, "In your hand you are holding: " + hand_str)

		backpack_obj_lst = stateful_dict['backpack']
		backpack_str = obj_lst_to_str(backpack_obj_lst)
		buffer(stateful_dict, "In your backpack you have: " + backpack_str)

def move_dec(stateful_dict): # was originally in interp_helper
		stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1

