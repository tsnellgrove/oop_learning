# program: dark castle v3.44
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: end function module


### imports ###
from dc3_static_init import *
from dc3_helper import *


### end routine ###
def end(stateful_dict, active_gs):
#		score = stateful_dict['current_score']
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
		print_score(stateful_dict, active_gs)
#		buffer("Your title is: " + title)
		if game_ending == 'won':
##				buffer(stateful_dict, credits.examine(stateful_dict))
				buffer(stateful_dict, descript_dict['credits'])
		stateful_dict['end_of_game'] = True

		return
