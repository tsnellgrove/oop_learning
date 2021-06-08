# program: dark castle v3
# name: Tom Snellgrove
# date: May 7, 2021
# description: interpreter function module for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter


### NOTE: MODULE NOT IN USE; NOT BEING CALLED ###


# import statements
from dc3_helper import buffer
from dc3_helper import open_cont_scan
from dc3_helper import objlst_to_strlst
##from dc3_demo import str_to_class
import dc3_config


#interpreter vocab
one_word_only_lst = ['score', 'version', 'inventory', 'look', 'quit', 'xyzzy42']
articles_lst = ['a', 'an', 'the']
verbs_lst = ['examine', 'read', 'go', 'take', 'drop', 'unlock', 'open', 'close', 'lock']
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
one_word_convert_dict = {
		'help' : 'examine',
		'credits' : 'examine',
		'north' : 'go',
		'south' : 'go',
		'east' : 'go',
		'west' : 'go'
}

descript_dict = {
		'introduction' : "This is the introduction [to be written]",
		"help" : "Detailed help text for new players [to be written]",
		"entrance" : "Entrance\nYou stand before the daunting gate of Dark Castle. In front of you is the gate"
}


### support functions ###
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
##		print(scope_lst)

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
		

### main interpreter function ###
def interpreter(stateful_dict, user_input):
		stateful_dict['move_counter'] = stateful_dict['move_counter'] + 1 
		room_obj = stateful_dict['room']
		lst = []
		lst.append(user_input)
		user_input_lst = lst[0].split() # convert user input string into word list

		# convert all words to lower case and substitute abreviations
		n = 0 
		for word in user_input_lst:
				word = word.lower()	
				if word in abreviations_dict:
						word = abreviations_dict[word]
				user_input_lst[n] = word
				n += 1

		# strip out articles
		for article in articles_lst:
				user_input_lst = [word for word in user_input_lst if word != article]
 
 		# no input or the only input is articles
		if len(user_input_lst) < 1: 
				buffer(stateful_dict, "I have no idea what you're talking about Burt!")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return 		

		# handle true one-word commands
		if len(user_input_lst) == 1:
				word1 = user_input_lst[0]
				if word1 in one_word_only_lst:
						if word1 == 'xyzzy42':
								buffer(stateful_dict, descript_dict["introduction"])
								buffer(stateful_dict, descript_dict["help"])
								buffer(stateful_dict, descript_dict["entrance"])
##								help.examine(stateful_dict)
								buffer(stateful_dict, "")
###								entrance.examine(stateful_dict)
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
						
				# convert one-word commands that are implicit two-word commands 
				elif word1 in one_word_convert_dict:
						user_input_lst.append(word1)
						user_input_lst[0] = one_word_convert_dict[word1]
						word1 = user_input_lst[0]

				# if not a known true or convertable one-word command, must be an error
				else:
						buffer(stateful_dict, "I don't understand what you're trying to say?")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return 

		# multi-word commands
		if len(user_input_lst) > 1:
				word1 = user_input_lst[0].lower()
				word2 = user_input_lst[1].lower()
		else:

				# commnd len ! > 1 should already be errored out
				buffer(stateful_dict, "HOW DID WE GET HERE???")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return

		# all commands longer than one word should start with a verb
		if word1 not in verbs_lst:
				buffer(stateful_dict, "Please start your sentence with a verb!")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
				return
	
		# convert 3-word verb-adj-noun command into verb-obj_name
		if len(user_input_lst) == 3:
				word3 = user_input_lst[2].lower()
				user_input_lst[1] = word2 + "_" + word3
				word2 = user_input_lst[1]
				del user_input_lst[2]

		# error out commands longer than two words
		if len(user_input_lst) > 2:
				buffer(stateful_dict, "Can you state that more simply? Burt's a man of few words!")
				return 

		# handle 2-word commands
		if word1 == 'go':
				getattr(room_obj, word1)(word2, stateful_dict)
				return # newly added
		
		# check to see if word2 is a known obj_name
		try:
##				word2_obj = str_to_class(word2)
				word2_obj = getattr(sys.modules[__name__], word2)
		except:
				# check to see if the word2 is a root_name; convert to obj_name if valid
				root_count, obj_name = root_word_count(stateful_dict, word2)
				if root_count < 1:
						buffer(stateful_dict, "I don't see a " + word2 + " here.")
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return
				elif root_count > 1:
						output = "I see more than one " + word2 + ". Please use the full name."
						buffer(stateful_dict, output)
						stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1
						return
				else:
##						word2_obj = str_to_class(obj_name)
						word2_obj = getattr(sys.modules[__name__], obj_name)

		# attempt to proces 2-word command
		try:
				getattr(word2_obj, word1)(stateful_dict)
		except:
				buffer(stateful_dict, "You can't " + word1 + " with the " + word2 + ".")
				stateful_dict['move_counter'] = stateful_dict['move_counter'] - 1

