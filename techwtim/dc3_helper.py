# program: dark castle v3
# name: Tom Snellgrove
# date: May 13, 2021
# description: helper function module for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter

# import statements
## import dc3_config


### NOT IN USE ###
def set_difference(a,b):
    return list(set(a)-set(b))

def change_desc(self, new_desc):
		self.desc = new_desc


### Only Used by Helper Functions ###
def open_cont_scan(stateful_dict, room_obj_lst):
		open_cont_obj_lst = []
		for obj in room_obj_lst:
				if hasattr(obj, 'contains') \
								and len(obj.contains) > 0 \
								and obj.open_state == True:
						open_cont_obj_lst = open_cont_obj_lst + obj.contains
		return open_cont_obj_lst


### Called by Other Modules ###
def buffer(stateful_dict, output_str):
		out_buff = stateful_dict['out_buff']
		out_buff = out_buff + output_str + "\n"
		stateful_dict['out_buff'] = out_buff

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

def container_desc(cont_obj, stateful_dict):
		if len(cont_obj.contains) == 0:
				buffer(stateful_dict, "The " + cont_obj.full_name + " is empty.")
		else:
				cont_str_lst = objlst_to_strlst(cont_obj.contains)
				output = "The " + cont_obj.full_name + " contains: "  + ', '.join(cont_str_lst)
				buffer(stateful_dict, output)


### interpreter centric ###
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
						obj_name = obj.name
				if obj.writing is not None:
						if obj.writing.root_name == word2:
								root_count += 1
								obj_name = obj.writing.name
		return root_count, obj_name

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


### Not working ###
## def str_to_class(str):
##		return getattr(sys.modules[__name__], str)