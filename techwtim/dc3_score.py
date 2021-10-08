# program: dark castle v3.44
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!


# import statements
import sys
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *


def score(stateful_dict):
		room_obj = stateful_dict['room']
		hand_lst = stateful_dict['hand']

		# increment item scores
		for score_key in item_score_lst:
				if len(hand_lst) > 0 and hand_lst[0].name == score_key and stateful_dict['points_earned_dict'][score_key] == False:
						stateful_dict['current_score'] = stateful_dict['current_score'] + score_val_dict[score_key]
						stateful_dict['points_earned_dict'][score_key] = True
						print_score(stateful_dict)

		# increment room scores
		for score_key in room_score_lst:
				if room_obj.name == score_key and stateful_dict['points_earned_dict'][score_key] == False:
						stateful_dict['current_score'] = stateful_dict['current_score'] + score_val_dict[score_key]
						stateful_dict['points_earned_dict'][score_key] = True
						print_score(stateful_dict)

		return 


