# program: dark castle v3.47
# name: Tom Snellgrove
# date: Oct 16, 2021
# description: updates score based on post-command execution game state


# import statements
import sys
from dc3_static_init import *


def score(active_gs):
		room_obj = active_gs.get_room()
		hand_lst = active_gs.get_hand_lst()

		# increment item scores
		for score_key in item_score_lst:
				if len(hand_lst) > 0 and hand_lst[0].name == score_key and active_gs.get_points_earned_state(score_key) == False:
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						active_gs.print_score()

		# increment room scores
		for score_key in room_score_lst:
				if room_obj.name == score_key and active_gs.get_points_earned_state(score_key) == False:
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						active_gs.print_score()

		return
