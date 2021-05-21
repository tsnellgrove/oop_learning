# program: dark castle v3
# name: Tom Snellgrove
# date: May 13, 2021
# description: main routine for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter


# import statements
## import cmd   # not in use
import sys
from itertools import islice
from dc3_helper import *
from dc3_classes import *
from dc3_init import *


# local helper functions
def str_to_class(str):
		return getattr(sys.modules[__name__], str)


# stateful dictionary of persistent values
stateful_dict = {
		'hand' : [], 
		'backpack' : [rusty_key],
		'universal' : [backpack, burt, fist, conscience, credits, help],
		'room' : entrance,
		'out_buff' : "",
		'score' : 0, 
		'version' : '3.01',
		'end_of_game' : False,
		'current_score' : 0,
		'move_counter' : 0,
		'game_ending' : ""
		}

#interpreter function vocab
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
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				buffer(stateful_dict, output)
				exit_state = True
				return exit_state, user_input_lst, word2, word2_obj
		
		# check to see if word2 is a known obj_name
		try:
				word2_obj = str_to_class(word2)
		except:
				# check to see if the word2 is a root_name; convert to obj_name if valid
				root_count, obj_name = root_word_count(stateful_dict, word2)
				if root_count < 1:
						buffer(stateful_dict, "I don't see a " + word2 + " here.")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						exit_state = True
						return exit_state, user_input_lst, word2, word2_obj
				elif root_count > 1:
						output = "I see more than one " + word2 + ". Please use the full name."
						buffer(stateful_dict, output)
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						exit_state = True
						return exit_state, user_input_lst, word2, word2_obj
				else:
						word2_obj = str_to_class(obj_name)

		return exit_state, user_input_lst, word2, word2_obj


# interpreter function
def interpreter(stateful_dict, user_input):
		stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1 
		room_obj = stateful_dict['room']

		user_input_lst = input_cleanup(user_input)
 		
		if len(user_input_lst) < 1: # no input or the only input is articles
				buffer(stateful_dict, "I have no idea what you're talking about Burt!")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
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
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				else:
						buffer(stateful_dict, "I don't understand what you're trying to say?")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return 

		# all commands longer than one word should start with a verb
		if word1 not in verbs_lst:
				buffer(stateful_dict, "Please start your sentence with a verb!")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return

		# there must be at least 2 words in user_input_lst
		word2 = user_input_lst[1] # can drop this now that it's in function?

		# handle special case 2-word commands
		if word1 == 'go':
				getattr(room_obj, word1)(word2, stateful_dict)
				return
		elif word1 == 'put':
				if 'in' not in user_input_lst:
						buffer(stateful_dict, "I don't see the word 'in' in that sentence")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return
				else:
						in_position = user_input_lst.index('in')
						v_n_lst = list(islice(user_input_lst, in_position))
						p_p_lst = list(islice(user_input_lst, in_position, None))
						exit_state, v_n_lst2, noun, noun_obj = noun_handling(stateful_dict, v_n_lst)
						if exit_state:
								return
						exit_state, p_p_lst2, dirobj, dirobj_obj = noun_handling(stateful_dict, p_p_lst)
						if exit_state:
								return
##						else:
##						getattr(dirobj_obj, word1)(noun_obj, stateful_dict)
						try:
								getattr(dirobj_obj, word1)(noun_obj, stateful_dict)
						except:
								buffer(stateful_dict, "That doesn't work.")
								stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return 
		else:
				exit_state, user_input_lst, word2, word2_obj = noun_handling(stateful_dict, user_input_lst)
				if exit_state:
						return

		# attempt to proces general 2-word commands
		try:
				getattr(word2_obj, word1)(stateful_dict)
		except:
				buffer(stateful_dict, "You can't " + word1 + " with the " + word2 + ".")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1


# test
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
# sword.examine(stateful_dict)
# chest.unlock(stateful_dict)
# wooden_chest.put(shiny_sword, stateful_dict)


# main routine
start_of_game = True
while stateful_dict['end_of_game'] == False:
		stateful_dict['out_buff'] = "" # resets buffer
		if start_of_game:
				user_input = "xyzzy42" # the magic word!!
				start_of_game = False
		else:
				user_input = input('Type your command: ')
		interpreter(stateful_dict, user_input)
		print(stateful_dict['out_buff'])
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

