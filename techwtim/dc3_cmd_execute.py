# program: dark castle v3.47
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
import random
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *
from dc3_class_deff import *


def true_one_word(stateful_dict, active_gs, word1, room_obj):
		if word1 == 'score':
				print_score(stateful_dict, active_gs)
		elif word1 == 'version':
				buffer(stateful_dict, static_dict['version'])
		elif word1 == 'help':
				buffer(stateful_dict, descript_dict['help'])
		elif word1 == 'credits':
				buffer(stateful_dict, descript_dict['credits'])
		elif word1 == 'inventory':
				inventory(stateful_dict)
		elif word1 == 'look':
				room_obj.examine(stateful_dict, active_gs)
		elif word1 == 'quit':
				active_gs.set_game_ending('quit') # triggers call end() from wrapper()
				active_gs.move_dec() # quitting is not deemed to be an actual move
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
		room_obj = stateful_dict['room']

		if case == 'help':
				word2 = word_lst[0]
				help(stateful_dict, word2)
		elif  case == 'tru_1word':
				word1 = word_lst[0]
				true_one_word(stateful_dict, active_gs, word1, room_obj)
		elif case == 'error':
				if word_lst[0] == "random error":
						num = random.randint(0, 4)
						interp_error_key = 'interp_error_' + str(num)
						output = descript_dict[interp_error_key]
				else:
						output = word_lst[0]
				buffer(stateful_dict, output)
				active_gs.move_dec()
		elif case == 'go':
				room_obj, word1, word2 = word_lst
				getattr(room_obj, word1)(word2, stateful_dict, active_gs)
		elif case == '2word':
				word2_obj, word1 = word_lst
				if word1 == 'read' and  writing_check(word2_obj, stateful_dict, active_gs) == False:
						if scope_check(word2_obj, stateful_dict, active_gs) == False:
								buffer(stateful_dict, "You can't see a " + word2_obj.full_name + " here.")
								return
						else:
								buffer(stateful_dict, "You can't read the " + word2_obj.full_name + ".")
								return
				elif (word1 != 'read') and (scope_check(word2_obj, stateful_dict, active_gs) == False):
						buffer(stateful_dict, "You can't see a " + word2_obj.full_name + " here.")
				else:
#						if word1 in ['read', 'eat', 'drink', 'take', 'drop', 'lock', 'unlock', 'close', 'open', 'examine']: # gradual introduce of active_gs
#								try:
#										print("migrated method") # troubleshoot
#										getattr(word2_obj, word1)(stateful_dict, active_gs)
#								except:
#										num = random.randint(0, 4)
#										interp_error_key = 'interp_error_' + str(num)
#										buffer(stateful_dict, descript_dict[interp_error_key])
#										active_gs.move_dec()
##										buffer(stateful_dict, "You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
#						else:
						try:
								getattr(word2_obj, word1)(stateful_dict, active_gs)
						except:
								num = random.randint(0, 4)
								interp_error_key = 'interp_error_' + str(num)
								buffer(stateful_dict, descript_dict[interp_error_key])
								active_gs.move_dec()
##										buffer(stateful_dict, "You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
		else: # case == 'put'
				dirobj_obj, word1, noun_obj = word_lst
				if scope_check(noun_obj, stateful_dict, active_gs) == False:
						buffer(stateful_dict, "You can't see a " + noun_obj.full_name + " here.")
						return
				elif scope_check(dirobj_obj, stateful_dict, active_gs) == False:
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


