# program: dark castle v3.11
# name: Tom Snellgrove
# date: July 27, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
import pickle
from itertools import islice
from dc3_static_init import *
from dc3_classes import *
# from dc3_init import *
from dc3_helper import *
## from dc3_interp_helper import *
import gc # only used for troubleshooting
## from dc3_obj_init import obj_init


### interpreter-specific helper functions ###
def str_to_class(str):
		return getattr(sys.modules[__name__], str)

def root_word_count(stateful_dict, word2):
		room_obj = stateful_dict['room']
		hand_lst = stateful_dict['hand']
		backpack_lst = stateful_dict['backpack']
		universal_lst = stateful_dict['universal']
		room_obj_lst = room_obj.room_items + room_obj.room_doors + room_obj.room_containers
		features_lst = room_obj.features
		open_cont_obj_lst = open_cont_scan(stateful_dict, room_obj.room_containers)
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

def help(stateful_dict, option):
		if option == 'basics':
				buffer(stateful_dict, descript_dict['help_basics'])
		elif option == 'verbs':
				buffer(stateful_dict, "Available verbs include: " + ', '.join(verbs_lst))
		elif option == 'one-word-commands':
				user_one_word_lst = one_word_only_lst
				user_one_word_lst.pop()
				output = ("Available one word commands include: "
								+ ', '.join(user_one_word_lst))
				buffer(stateful_dict, output)
		elif option == 'articles':
				output = ("The following articles are supported but not required: "
								+ ', '.join(articles_lst))
				buffer(stateful_dict, output)
		elif option == 'adjectives':
					buffer(stateful_dict, descript_dict['help_adjectives'])
		elif  option == 'abbreviations':
				pre_out = "Available abbreviations include: "
				for key in abbreviations_dict:
						pre_out = pre_out + key + " = " + abbreviations_dict[key] + ", "
				output = pre_out[:-2]
				buffer(stateful_dict, output)
		elif option == 'prepositions':
					buffer(stateful_dict, descript_dict['help_prepositions'])
		else:
				buffer(stateful_dict, descript_dict['help'])

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

def true_one_word(stateful_dict, word1, room_obj):
		if word1 == 'xyzzy42':
				buffer(stateful_dict, descript_dict["introduction"])
				entrance.examine(stateful_dict)
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
				move_dec(stateful_dict)
				move_dec(stateful_dict)
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


# interpreter
def interpreter(user_input):
##def interpreter(stateful_dict, user_input):

		if user_input == "xyzzy42":
				import dc3_obj_init
		else:
				import dc3_obj_init2


#		master_obj_lst = []
#		if user_input == "xyzzy42":
#				with open('default_obj_pickle', 'rb') as f:
#						master_obj_lst = pickle.load(f)
##				print(master_obj_lst)
#		else:
#				with open('save_obj_pickle', 'rb') as f:
#						master_obj_lst = pickle.load(f)

#		rusty_letters, dwarven_runes, dark_castle, backpack, burt, fist, conscience, rusty_key, shiny_sword, brass_key, bubbly_potion, wooden_chest, front_gate, entrance, main_hall, stateful_dict = master_obj_lst


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


		with open('save_obj_pickle', 'wb') as f:
				pickle.dump(master_obj_lst, f)

		return stateful_dict['end_of_game'], stateful_dict['out_buff']

### test ###
# rusty_letters.read(stateful_dict)
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)


# wrapper code - sets up game state and calls interpreter
## def wrapper(user_input, stateful_dict):
def wrapper(user_input): # version without stateful_dict

#		master_obj_lst = []
#		if user_input == "xyzzy42":
#				with open('default_obj_pickle', 'rb') as f:
#						master_obj_lst = pickle.load(f)
##				print(master_obj_lst)
#		else:
#				with open('save_obj_pickle', 'rb') as f:
#						master_obj_lst = pickle.load(f)
		
#		rusty_letters, dwarven_runes, dark_castle, backpack, burt, fist, conscience, rusty_key, shiny_sword, brass_key, bubbly_potion, wooden_chest, front_gate, entrance, main_hall, stateful_dict = master_obj_lst

##		print(rusty_letters)
##		obj_init(master_obj_lst)

#		interpreter(stateful_dict, user_input)
		interpreter(user_input)

		### troubleshooting code ###
		print(front_gate)
		print(front_gate.open_state)
		print(stateful_dict['room'].room_doors)
		print(stateful_dict['room'].room_doors[0].open_state)
		for obj in gc.get_objects():
				if isinstance(obj, Door):
						print(obj, obj.open_state, id(obj))
		### troubleshooting code ###

#		with open('save_obj_pickle', 'wb') as f:
#				pickle.dump(master_obj_lst, f)

#		return stateful_dict['end_of_game'], stateful_dict['out_buff']


# main routine
start_of_game = True
end_of_game = False
while end_of_game == False:
		if start_of_game:
				user_input = "xyzzy42" # the magic word!!
				start_of_game = False
		else:
				user_input = input('Type your command: ')
		end_of_game, output = interpreter(user_input)
##		end_of_game, output = wrapper(user_input)
##		end_of_game, output = wrapper(user_input, stateful_dict)
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

