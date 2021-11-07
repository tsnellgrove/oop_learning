# program: dark castle v3.48
# name: Tom Snellgrove
# date: Oct 22, 2021
# description: converts player input into game commands


### import statements
import sys
from itertools import islice
from dc3_class_deff import *

### interpreter function language static dictionaries & lists ###
articles_lst = ['a', 'an', 'the']

one_word_only_lst = ['help', 'credits', 'score', 'version', 'inventory', 'look', 'quit', 'xyzzy42']

verbs_lst = ['help', 'examine', 'read', 'go', 'take', 'drop', 'unlock', 'open', 'close', 'lock', 'put', 'eat', 'drink']

abbreviations_dict = {
		'n' : 'north',
		's' : 'south',
		'e' : 'east',
		'w' : 'west',
		'i' : 'inventory',
		'l' : 'look',
		'get' : 'take',
		'x' : 'examine',
		'q' : 'quit',
		'h' : 'help'
}

one_word_convert_dict = {
		'north' : 'go',
		'south' : 'go',
		'east' : 'go',
		'west' : 'go'
}

### help = print help info
def help(active_gs, option):
		if option == 'basics':
				output = descript_dict['help_basics']
		elif option == 'verbs':
				output = "Available verbs include: " + ', '.join(verbs_lst)
		elif option == 'one-word-commands':
				user_one_word_lst = one_word_only_lst
				user_one_word_lst.pop()
				output = ("Available one word commands include: "
								+ ', '.join(user_one_word_lst))
		elif option == 'articles':
				output = ("The following articles are supported but not required: "
								+ ', '.join(articles_lst))
		elif option == 'adjectives':
					output = descript_dict['help_adjectives']
		elif  option == 'abbreviations':
				pre_out = "Available abbreviations include: "
				for key in abbreviations_dict:
						pre_out = pre_out + key + " = " + abbreviations_dict[key] + ", "
				output = pre_out[:-2]
		elif option == 'prepositions':
					output = descript_dict['help_prepositions']
		elif option == 'read':
					output = descript_dict['help_read']
		else:
				output = descript_dict['help']
		active_gs.buffer(output)

### root_word_count - determines if user command contains root words
def root_word_count(active_gs, word2_txt):
		scope_lst = active_gs.scope_lst()
		root_count = 0
		obj_name = ""
		for obj in scope_lst:
				if obj.root_name == word2_txt:
						root_count += 1
						obj_name = obj.name
				if obj.has_writing():
						if obj.writing.root_name == word2_txt:
								root_count += 1
								obj_name = obj.writing.name
		return root_count, obj_name

### input_cleanup - convert user_input str to lst, lower, convert abbreviations, remove articles
def input_cleanup(user_input):
		# first, convert user input string into word list
		lst = []
		lst.append(user_input)
		user_input_lst = lst[0].split()
		# next, convert all words to lower case and substitute abbreviations
		n = 0 
		for word in user_input_lst:
				word = word.lower()	
				if word in abbreviations_dict:
						word = abbreviations_dict[word]
				user_input_lst[n] = word
				n += 1
		# finally, strip out articles
		for article in articles_lst:
				user_input_lst = [word for word in user_input_lst if word != article]
		return user_input_lst

### handle nouns and adjectives
def noun_handling(master_obj_lst, user_input_lst):
		active_gs = master_obj_lst[0]
		error_state = False
		error_msg = ""
		word2_obj = ""
		word2_txt = user_input_lst[1]

		# convert 3-word verb-adj-noun commands into verb-obj_name commands
		if len(user_input_lst) == 3:
				word3_txt = user_input_lst[2]
				user_input_lst[1] = word2_txt + "_" + word3_txt
				word2_txt = user_input_lst[1]
				del user_input_lst[2]

		# error out commands that are still longer than two words
		if len(user_input_lst) > 2:
				error_msg = "Can you state that more simply? Burt's a man of few words!"
				error_state = True
				return error_state, error_msg, word2_obj
		
		# check to see if word2 is a known obj_name
		word2_txt_known = False
		for obj in master_obj_lst[1:]:
				if obj.name == word2_txt:
						word2_txt_known = True
						word2_obj = obj

		# check to see if the word2 is a root_name; convert to obj_name if valid
		if not word2_txt_known:
				root_count, obj_name = root_word_count(active_gs, word2_txt)
				if root_count < 1:
						error_msg = "I don't see a " + word2_txt + " here."
						error_state = True
						return error_state, error_msg, word2_obj
				elif root_count > 1:
						error_msg = "I see more than one " + word2_txt + ". Please use the full name."
						error_state = True
						return error_state, error_msg, word2_obj
				else:
						for obj in master_obj_lst[1:]:
								if obj.name == obj_name:
										word2_obj = obj
		return error_state, error_msg, word2_obj

### interpreter - determine user intent
def interpreter(user_input, master_obj_lst):
		active_gs = master_obj_lst[0]
		room_obj = active_gs.get_room()
		user_input_lst = input_cleanup(user_input)

		# error if no input or the only input is articles 
		if len(user_input_lst) < 1:
				return 'error', ["I have no idea what you're talking about Burt!"]

		# len(user_input_lst) is not < 1 so user_input_lst must have at least one word in it
		word1 = user_input_lst[0]

		# handle true one-word commands
		if len(user_input_lst) == 1 and word1 in one_word_only_lst:
				return 'tru_1word', [word1]

		# convert one-word commands that are implicit two-word commands 
		elif len(user_input_lst) == 1 and word1 in one_word_convert_dict:
				user_input_lst.append(word1)
				user_input_lst[0] = one_word_convert_dict[word1]
				word1 = user_input_lst[0]

		# if not a known true or convertable one-word command, must be an error
		elif len(user_input_lst) == 1:
				if word1 in verbs_lst:
						error_msg = word1 + " what?"
				else:
						error_msg = "random error"
				return 'error', [error_msg]

		# all commands longer than one word should start with a verb
		if word1 not in verbs_lst:
				return 'error', ["Please start your sentence with a known verb!"]

		# handle 2-word commands (special cases first else general case)
		if word1 == 'go':
				word2 = user_input_lst[1]
				return 'go', [room_obj, word1, word2]
		elif word1 == 'help':
				word2 = user_input_lst[1]
				help(active_gs, word2)
				return 'help', [word2]
		elif word1 == 'put':
				if 'in' not in user_input_lst:
						return 'error', ["I don't see the word 'in' in that sentence"]
				else:
						in_position = user_input_lst.index('in')
						v_n_lst = list(islice(user_input_lst, in_position))
						p_p_lst = list(islice(user_input_lst, in_position, None))
						noun_error_state, noun_error_msg, noun_obj = noun_handling(master_obj_lst, v_n_lst)
						dir_obj_error_state, dir_obj_error_msg, dirobj_obj = noun_handling(master_obj_lst, p_p_lst)
						if noun_error_state:
								return 'error', [noun_error_msg]
						elif dir_obj_error_state:
								return 'error', [dir_obj_error_msg]
						else:
								return 'put', [dirobj_obj, word1, noun_obj]
		else: # '2word' case
				error_state, error_msg, word2_obj = noun_handling(master_obj_lst, user_input_lst)
				if error_state:
						return 'error', [error_msg]
				else:
						return '2word', [word2_obj, word1]

