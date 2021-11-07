# program: dark castle v3.48
# name: Tom Snellgrove
# date: Oct 22, 2021
# description: executes game commands


### import statements ###
import sys
import random
from dc3_static_init import descript_dict, static_dict
from dc3_class_deff import *

def rand_error():
		num = random.randint(0, 4)
		interp_error_key = 'interp_error_' + str(num)
		return descript_dict[interp_error_key]

def true_one_word(active_gs, word1, room_obj):
		if word1 == 'score':
				active_gs.print_score()
		elif word1 == 'version':
				active_gs.buffer(static_dict['version'])
		elif word1 == 'help':
				active_gs.buffer(descript_dict['help'])
		elif word1 == 'credits':
				active_gs.buffer(descript_dict['credits'])
		elif word1 == 'inventory':
				active_gs.inventory()
		elif word1 == 'look':
				room_obj.examine(active_gs)
		elif word1 == 'quit':
				active_gs.set_game_ending('quit') # triggers call end() from wrapper()
				active_gs.move_dec() # quitting is not deemed to be an actual move
		return

def special_error(active_gs, word2_obj, word1):
	if word1 == 'read' and  active_gs.writing_check(word2_obj) == False:
			if active_gs.scope_check(word2_obj) == False:
					active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
					return True
			else:
					output = "You can't read the " + word2_obj.full_name + ". Try using 'examine' instead."
					active_gs.buffer(output)
					return True
	elif (word1 == 'examine') and (active_gs.writing_check(word2_obj)) == True:
			output = "You can't examine the " + word2_obj.full_name + ". Try using 'read' instead."
			active_gs.buffer(output)
			return True
	elif (word1 != 'read') and (active_gs.scope_check(word2_obj) == False):
			active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
			return True
	elif (word1 == 'take') and (active_gs.scope_check(word2_obj)) and (word2_obj.is_beverage()):
			active_gs.buffer("You can't 'take' a beverage.")
			return True
	else:
			return False

def cmd_execute(active_gs, case, word_lst):
		room_obj = active_gs.get_room()

		if case == 'help':
##				word2 = word_lst[0] # help() now called from interpreter()
##				help(active_gs, word2) # help() now called from interpreter()
				pass
		elif  case == 'tru_1word':
				word1 = word_lst[0]
				true_one_word(active_gs, word1, room_obj)
		elif case == 'error':
				if word_lst[0] == "random error":
						output = rand_error()
				else:
						output = word_lst[0]
				active_gs.buffer(output)
				active_gs.move_dec()
		elif case == 'go':
				room_obj, word1, word2 = word_lst
				getattr(room_obj, word1)(word2, active_gs)
		elif case == '2word':
				word2_obj, word1 = word_lst
				if not special_error(active_gs, word2_obj, word1):
##						getattr(word2_obj, word1)(active_gs) # for troubleshooting
						try:
								getattr(word2_obj, word1)(active_gs)
						except:
								error_msg = rand_error()
								active_gs.buffer(error_msg)
								active_gs.move_dec()
##							active_gs.buffer("You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
		else: # case == 'put'
				dirobj_obj, word1, noun_obj = word_lst
				if active_gs.scope_check(noun_obj) == False:
						active_gs.buffer("You can't see a " + noun_obj.full_name + " here.")
						return
				elif active_gs.scope_check(dirobj_obj) == False:
						active_gs.buffer("You can't see a " + dirobj_obj.full_name + " here.")
						return 
				else:
						try:
								getattr(dirobj_obj, word1)(noun_obj, active_gs)
						except:
								error_msg = rand_error()
								active_gs.buffer(error_msg)
								active_gs.move_dec()


