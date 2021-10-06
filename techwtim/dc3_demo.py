# program: dark castle v3.42
# name: Tom Snellgrove
# date: Oct 3, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
#import pickle
import random
from itertools import islice
from dc3_static_init import * # variables declared in import = global to module
#from dc3_classes import *
#from dc3_classes2 import declare_classes
from dc3_helper import *
from dc3_class_deff import *
import gc
###from dc3_obj_init2 import *
#from dc3_start_me_up import start_me_up


### interpreter-specific helper functions ###
def str_to_class(str):
		return getattr(sys.modules[__name__], str)




def root_word_count(stateful_dict, word2_txt):
		scope_lst = scope_list(stateful_dict)
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

# convert user_input str to lst, lower, convert abbreviations, remove articles
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

# handle nouns and adjectives
def noun_handling(master_obj_lst, user_input_lst):
		stateful_dict = master_obj_lst[0]
		active_gs = master_obj_lst[1]
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
		for obj in master_obj_lst[2:]:
				if obj.name == word2_txt:
						word2_txt_known = True
						word2_obj = obj

		# check to see if the word2 is a root_name; convert to obj_name if valid
		if not word2_txt_known:
				root_count, obj_name = root_word_count(stateful_dict, word2_txt)
				if root_count < 1:
						error_msg = "I don't see a " + word2_txt + " here."
						error_state = True
						return error_state, error_msg, word2_obj
				elif root_count > 1:
						error_msg = "I see more than one " + word2_txt + ". Please use the full name."
						error_state = True
						return error_state, error_msg, word2_obj
				else:
						for obj in master_obj_lst[2:]:
								if obj.name == obj_name:
										word2_obj = obj
		return error_state, error_msg, word2_obj

# interpreter
def interpreter(user_input, master_obj_lst):

		print("interpreter - start")

		stateful_dict = master_obj_lst[0]
		active_gs = master_obj_lst[1]
		room_obj = stateful_dict['room']
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
						output = word1 + " what?"
				else:
						num = random.randint(0, 4)
						interp_error_key = 'interp_error_' + str(num)
						output = descript_dict[interp_error_key]
				return 'error', [output]

		# all commands longer than one word should start with a verb
		if word1 not in verbs_lst:
				return 'error', ["Please start your sentence with a known verb!"]

		# handle 2-word commands (special cases first else general case)
		if word1 == 'go':
				word2 = user_input_lst[1]
				return 'go', [room_obj, word1, word2]
		elif word1 == 'help':
				word2 = user_input_lst[1]
				return 'help', [word2]
		elif word1 == 'put':
				if 'in' not in user_input_lst:
						return 'error', ["I don't see the word 'in' in that sentence"]
				else:
						in_position = user_input_lst.index('in')
						v_n_lst = list(islice(user_input_lst, in_position))
						p_p_lst = list(islice(user_input_lst, in_position, None))
						noun_error_state, error_msg, noun_obj = noun_handling(master_obj_lst, v_n_lst)
						dir_obj_error_state, error_msg, dirobj_obj = noun_handling(master_obj_lst, p_p_lst)
						if noun_error_state or dir_obj_error_state:
								return 'error', [error_msg]
						else:
								return 'put', [dirobj_obj, word1, noun_obj]
		else:
				error_state, error_msg, word2_obj = noun_handling(master_obj_lst, user_input_lst)
				if error_state:
						return 'error', [error_msg]
				else:
						return '2word', [word2_obj, word1]





def true_one_word(stateful_dict, word1, room_obj):
		if word1 == 'score':
				print_score(stateful_dict)
		elif word1 == 'version':
				buffer(stateful_dict, static_dict['version'])
		elif word1 == 'help':
				buffer(stateful_dict, descript_dict['help'])
		elif word1 == 'credits':
				buffer(stateful_dict, descript_dict['credits'])
		elif word1 == 'inventory':
				inventory(stateful_dict)
		elif word1 == 'look':
				room_obj.examine(stateful_dict)
		elif word1 == 'quit':
				stateful_dict['game_ending'] = "quit"
				move_dec(stateful_dict) # quitting is not deemed to be an actual move
				end(stateful_dict) # maybe move to wrapper?
		return

def help(stateful_dict, option):
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
		buffer(stateful_dict, output)

def cmd_execute(stateful_dict, active_gs, case, word_lst):

		print("cmd_execute - start")
		
		room_obj = stateful_dict['room']

		if case == 'help':
				word2 = word_lst[0]
				help(stateful_dict, word2)
		elif  case == 'tru_1word':
				word1 = word_lst[0]
				true_one_word(stateful_dict, word1, room_obj)
		elif case == 'error':
				buffer(stateful_dict, word_lst[0])
				move_dec(stateful_dict)
		elif case == 'go':
				room_obj, word1, word2 = word_lst
				getattr(room_obj, word1)(word2, stateful_dict, active_gs)
		elif case == '2word':
				word2_obj, word1 = word_lst
				if word1 == 'read' and  writing_check(word2_obj, stateful_dict) == False:
						if scope_check(word2_obj, stateful_dict) == False:
								buffer(stateful_dict, "You can't see a " + word2_obj.full_name + " here.")
								return
						else:
								buffer(stateful_dict, "You can't read the " + word2_obj.full_name + ".")
								return
				elif (word1 != 'read') and (scope_check(word2_obj, stateful_dict) == False):
						buffer(stateful_dict, "You can't see a " + word2_obj.full_name + " here.")
				else:
						try:
								getattr(word2_obj, word1)(stateful_dict)
						except:
								num = random.randint(0, 4)
								interp_error_key = 'interp_error_' + str(num)
								buffer(stateful_dict, descript_dict[interp_error_key])
#								buffer(stateful_dict, "You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
								move_dec(stateful_dict)
		else: # case == 'put'
				dirobj_obj, word1, noun_obj = word_lst
				if scope_check(noun_obj, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + noun_obj.full_name + " here.")
						return
				elif scope_check(dirobj_obj, stateful_dict) == False:
						buffer(stateful_dict, "You can't see a " + dirobj_obj.full_name + " here.")
						return 
				else:
						try:
								getattr(dirobj_obj, word1)(noun_obj, stateful_dict)
						except:
								num = random.randint(0, 4)
								interp_error_key = 'interp_error_' + str(num)
								buffer(stateful_dict, descript_dict[interp_error_key])
								move_dec(stateful_dict)


# wrapper code - calls interpreter and saves game state
# NO LONGER IN USE AFTER v3.42
# wapper now called from dedicated dc3_wrapper module
#def wrapper(user_input):


#		print("old wrapper start - SHOULD NEVER PRINT") # troubleshooting

#		if user_input == "xyzzy42":
#				end_of_game, out_buff = start_me_up()
#		else:
##				from dc3_define_class_gs import GameState
##				from dc3_define_class_other import Writing, ViewOnly, Room, Item, Door, Container, Food, Jug, Beverage

#				print("wrapper post-declare_classes pre-pickle-load - SHOULD NEVER PRINT")
#				for obj in gc.get_objects():
#						if isinstance(obj, GameState):
#								print(obj, id(obj))

				# object list loaded from pickle
#				with open('save_obj_pickle2', 'rb') as f:
#						master_obj_lst = pickle.load(f)

				# object vatiables declared / instantiated from un-pickled list
#				rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, active_gs, stateful_dict = master_obj_lst

#				print("wrapper - post-pickle load - SHOULD NEVER PRINT")

#				stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1
#				stateful_dict['out_buff'] = "" # resets buffer

				### test commands ###
##				stale_biscuits.take(stateful_dict)
##				fresh_water.drink(stateful_dict)
##				torn_note.examine(stateful_dict)
				### test commands ###

				#	troubleshooting
#				print("wrapper - pre interpreter - SHOULD NEVER PRINT")
#				for obj in gc.get_objects():
#						if isinstance(obj, GameState):
#								print(obj, id(obj), sys.getrefcount(obj))
#						if isinstance(obj, Room):
#								print(obj, id(obj), sys.getrefcount(obj))

#				case, word_lst = interpreter(user_input, master_obj_lst)
###			case, word_lst = interpreter(stateful_dict, user_input)
				# pre-action triggers will go here
#				if case in ['go', 'put', '2word']:
#						cmd_execute(stateful_dict, active_gs, case, word_lst)
				# post-action triggers will go here

#				master_obj_lst = [rusty_lettering, dwarven_runes, messy_handwriting, small_print, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance, main_hall, antechamber, throne_room, active_gs, stateful_dict]

#				with open('save_obj_pickle2', 'wb') as f:
#						pickle.dump(master_obj_lst, f) # Why are list elements updated? But works!
		
#				print("wrapper - pickle dump - SHOULD NEVER PRINT")
				
#				end_of_game = stateful_dict['end_of_game']
#				out_buff = stateful_dict['out_buff']
		
#		return end_of_game, out_buff
