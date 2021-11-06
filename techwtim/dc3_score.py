# program: dark castle v3.48
# name: Tom Snellgrove
# date: Oct 22, 2021
# description: updates score based on post-command execution game state


# import statements
import sys
from dc3_static_init import item_score_lst, room_score_lst, score_val_dict


def score(active_gs):
		room_obj = active_gs.get_room()
		hand_lst = active_gs.get_hand_lst()

		# increment item scores
		for score_key in item_score_lst:
				if not active_gs.hand_empty and hand_lst[0].name == score_key and active_gs.get_points_earned_state(score_key) == False:
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
