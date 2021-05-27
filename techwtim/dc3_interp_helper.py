# program: dark castle v3
# name: Tom Snellgrove
# date: May 25, 2021
# description: interpreter-specific helper function module for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter

### imports ###
import sys
from dc3_helper import *
from dc3_classes import *
from dc3_init import *


### interpreter function vocab ###
articles_lst = ['a', 'an', 'the']
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

#interpreter local vocab
one_word_only_lst = ['score', 'version', 'inventory', 'look', 'quit', 'xyzzy42']
one_word_convert_dict = {
		'help' : 'examine',
		'credits' : 'examine',
		'north' : 'go',
		'south' : 'go',
		'east' : 'go',
		'west' : 'go'
}
verbs_lst = ['examine', 'read', 'go', 'take', 'drop', 'unlock', 'open', 'close', 'lock', 'put']
prep_lst = {
		'in'
}

# description dict
descript_dict = {
		'introduction' : "This is the introduction [to be written]"
}


### interpreter-specific helper functions ###
def str_to_class(str):
		return getattr(sys.modules[__name__], str)

def move_dec(stateful_dict):
		stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1

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
	
# convert user_input str to lst, lower, convert abreviations, remove articles
def input_cleanup(user_input):
		# first, convert user input string into word list
		lst = []
		lst.append(user_input)
		user_input_lst = lst[0].split()
		# next, convert all words to lower case and substitute abreviations
		n = 0 
		for word in user_input_lst:
				word = word.lower()	
				if word in abreviations_dict:
						word = abreviations_dict[word]
				user_input_lst[n] = word
				n += 1
		# finally, strip out articles
		for article in articles_lst:
				user_input_lst = [word for word in user_input_lst if word != article]
		return user_input_lst

def true_one_word(stateful_dict, word1, room_obj):
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

def noun_handling(stateful_dict, user_input_lst):
		exit_state = False
		word2_obj = rusty_key
		word2 = user_input_lst[1]

		# convert 3-word verb-adj-noun commands into verb-obj_name commands
		if len(user_input_lst) == 3:
				word3 = user_input_lst[2]
				user_input_lst[1] = word2 + "_" + word3
				word2 = user_input_lst[1]
				del user_input_lst[2]

		# error out commands that are still longer than two words
		if len(user_input_lst) > 2:
				output = "Can you state that more simply? Burt's a man of few words!"
				buffer(stateful_dict, output)
				move_dec(stateful_dict)
				exit_state = True
				return exit_state, word2_obj
		
		# check to see if word2 is a known obj_name
		try:
				word2_obj = str_to_class(word2)
		except:
				# check to see if the word2 is a root_name; convert to obj_name if valid
				root_count, obj_name = root_word_count(stateful_dict, word2)
				if root_count < 1:
						buffer(stateful_dict, "I don't see a " + word2 + " here.")
						move_dec(stateful_dict)
						exit_state = True
						return exit_state, word2_obj
				elif root_count > 1:
						output = "I see more than one " + word2 + ". Please use the full name."
						buffer(stateful_dict, output)
						move_dec(stateful_dict)
						exit_state = True
						return exit_state, word2_obj
				else:
						word2_obj = str_to_class(obj_name)
		return exit_state, word2_obj
