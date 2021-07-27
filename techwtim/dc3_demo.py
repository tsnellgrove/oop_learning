# program: dark castle v3.11
# name: Tom Snellgrove
# date: July 27, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
from itertools import islice
from dc3_static_init import *
from dc3_classes import *
from dc3_init import *
from dc3_helper import *
from dc3_interp_helper import *
import gc # only used for troubleshooting


# interpreter
def interpreter(stateful_dict, user_input):
		stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1 
		room_obj = stateful_dict['room']
		stateful_dict['out_buff'] = "" # resets buffer

		user_input_lst = input_cleanup(user_input)
 		
		if len(user_input_lst) < 1: # no input or the only input is articles
				buffer(stateful_dict, "I have no idea what you're talking about Burt!")
				move_dec(stateful_dict)
				return

		# user_input_lst must have at least one word in it
		word1 = user_input_lst[0]

		# handle true one-word commands
		if len(user_input_lst) == 1 and word1 in one_word_only_lst:
				true_one_word(stateful_dict, word1, room_obj)
				return

		# convert one-word commands that are implicit two-word commands 
		elif len(user_input_lst) == 1 and word1 in one_word_convert_dict:
				user_input_lst.append(word1)
				user_input_lst[0] = one_word_convert_dict[word1]
				word1 = user_input_lst[0]

		# if not a known true or convertable one-word command, must be an error
		elif len(user_input_lst) == 1:
				if word1 in verbs_lst:
						buffer(stateful_dict, word1 + " what?")
						move_dec(stateful_dict)
				else:
						buffer(stateful_dict, "I don't understand what you're trying to say?")
						move_dec(stateful_dict)
				return 

		# all commands longer than one word should start with a verb
		if word1 not in verbs_lst:
				buffer(stateful_dict, "Please start your sentence with a verb!")
				move_dec(stateful_dict)
				return

		# handle 2-word commands (special cases first else general case)
		if word1 == 'go':
				word2 = user_input_lst[1]
				getattr(room_obj, word1)(word2, stateful_dict)
				return
		elif word1 == 'help':
				word2 = user_input_lst[1]
				help(stateful_dict, word2)
		elif word1 == 'put':
				if 'in' not in user_input_lst:
						buffer(stateful_dict, "I don't see the word 'in' in that sentence")
						move_dec(stateful_dict)
						return
				else:
						in_position = user_input_lst.index('in')
						v_n_lst = list(islice(user_input_lst, in_position))
						p_p_lst = list(islice(user_input_lst, in_position, None))
						exit_state, noun_obj = noun_handling(stateful_dict, v_n_lst)
						if exit_state:
								return
						exit_state, dirobj_obj = noun_handling(stateful_dict, p_p_lst)
						if exit_state:
								return
						try:
								getattr(dirobj_obj, word1)(noun_obj, stateful_dict)
						except:
								buffer(stateful_dict, "That doesn't work.")
								move_dec(stateful_dict)
						return 
		else:
				exit_state, word2_obj = noun_handling(stateful_dict, user_input_lst)
				if exit_state:
						return
				try:
						getattr(word2_obj, word1)(stateful_dict)
				except:
						buffer(stateful_dict, "You can't " + word1 + " with the " + word2_obj.full_name + ".")
						move_dec(stateful_dict)


### test ###
# rusty_letters.read(stateful_dict)
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)


# wrapper code - sets up game state and calls interpreter
def wrapper(user_input, stateful_dict):
## def wrapper(user_input): # version without stateful_dict

		if user_input == "xyzzy42":
				pass
		else:
				pass
		interpreter(stateful_dict, user_input)

		### troubleshooting code ###
		print(front_gate)
		print(front_gate.open_state)
		print(stateful_dict['room'].room_doors)
		print(stateful_dict['room'].room_doors[0].open_state)
		for obj in gc.get_objects():
				if isinstance(obj, Door):
						print(obj, obj.open_state, id(obj))
		### troubleshooting code ###

		return stateful_dict['end_of_game'], stateful_dict['out_buff']


# main routine
start_of_game = True
end_of_game = False
while end_of_game == False:
		if start_of_game:
				user_input = "xyzzy42" # the magic word!!
				start_of_game = False
		else:
				user_input = input('Type your command: ')
###		end_of_game, output = wrapper(user_input)
		end_of_game, output = wrapper(user_input, stateful_dict)
		print(output)
print("THANKS FOR PLAYING!!")


# entrance.examine()
# print(entrance.valid_paths)
# entrance.go('south')
# entrance.go('north')

# entrance.examine()
# dark_castle.examine()
# gate.examine()
# gate.read_writing()
# sword.examine()
# sword.take()
# print(hand)
# sword.take()
# sword.drop()
# gate.open()
# gate.unlock()
# rusty_key.examine()
# rusty_key.take()
# print(hand)
# gate.unlock()
# gate.open()
# gate.open()
# print(eval(room).room_stuff)

# sword = Item('sword','The sword is shiny.', True, 5)
# sword.examine()
# sword.change_desc('The sword is rusty.')
# sword.examine()
# print(sword.takeable)
# print(sword.weight)
# sword.add_writing('dwarven runes', 'Goblin Wallaper')
# sword.examine()
# sword.read_writing()
# gate = Door('front gate', 'The front gate is daunting', False, False)
# gate.examine()
# gate.change_desc('The front gate is HUGE!')
# gate.examine()
# gate.read_writing()
# gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
# gate.read_writing()

