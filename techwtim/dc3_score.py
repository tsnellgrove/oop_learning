# program: dark castle v3.46
# name: Tom Snellgrove
# date: Oct 15, 2021
# description: updates score based on post-command execution game state


# import statements
import sys
from dc3_static_init import * # variables declared in import = global to module
from dc3_helper import *


def score(stateful_dict, active_gs):
		room_obj = active_gs.get_room()
		hand_lst = active_gs.get_hand_lst()

		# increment item scores
		for score_key in item_score_lst:
				if len(hand_lst) > 0 and hand_lst[0].name == score_key and active_gs.get_points_earned_state(score_key) == False:
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						print_score(active_gs)

		# increment room scores
		for score_key in room_score_lst:
				if room_obj.name == score_key and active_gs.get_points_earned_state(score_key) == False:
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						print_score(active_gs)

		return
