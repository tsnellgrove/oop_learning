# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 5, 2021
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

#def objlst_to_strlst(obj_lst):
#		str_lst = []
#		for obj in obj_lst:
#				str_lst.append(obj.full_name)
#		return str_lst

def obj_lst_to_str(obj_lst):
		if not isinstance(obj_lst, list):
				raise ValueError("is not a list")
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

def print_score(stateful_dict):
		output1 = ("Your score is " + str(stateful_dict['current_score']))
		output2 = (" out of " + str(static_dict['max_score']))
		buffer(stateful_dict, output1 + output2)

def move_dec(stateful_dict): # was originally in interp_helper
		stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1


### end routine ###
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
		print_score(stateful_dict)
#		buffer("Your title is: " + title)
		if game_ending == 'won':
				buffer(stateful_dict, credits.examine(stateful_dict))
		stateful_dict['end_of_game'] = True
		return


