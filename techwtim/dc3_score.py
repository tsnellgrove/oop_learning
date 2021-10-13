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


def score(stateful_dict, active_gs):
		room_obj = stateful_dict['room']
#		hand_lst = stateful_dict['hand']
		hand_lst = active_gs.get_hand_lst()

		# increment item scores
		for score_key in item_score_lst:
				if len(hand_lst) > 0 and hand_lst[0].name == score_key and active_gs.get_points_earned_state(score_key) == False:
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						print_score(stateful_dict, active_gs)

		# increment room scores
		for score_key in room_score_lst:
				if room_obj.name == score_key and active_gs.get_points_earned_state(score_key) == False:
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						print_score(stateful_dict, active_gs)

		return 



