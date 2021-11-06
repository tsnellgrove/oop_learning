# program: dark castle v3.48
# name: Tom Snellgrove
# date: Oct 22, 2021
# description: presents end of game text 


### imports ###
from dc3_static_init import descript_dict


### end routine ###
def end(active_gs):
		moves = active_gs._state_dict['move_counter']
		game_ending = active_gs.get_game_ending()

#		if score < 0:
#				title_score = -10
#		elif score == 0:
#				title_score = 0
#		else:
#				title_score = math.ceil(score / 10) * 10
#		title = static_dict['titles_dict'][title_score]

		if game_ending == 'death':
				active_gs.buffer("You have died.")
		elif game_ending == 'quit':
				active_gs.buffer("You have quit.")
		elif game_ending == 'won':
				active_gs.buffer("You have won!")
		active_gs.buffer("Your adventure ended after " + str(moves) + " moves.")
		active_gs.print_score()
##		buffer("Your title is: " + title)
		if game_ending == 'won':
				active_gs.buffer(descript_dict['credits'])
		active_gs.set_end_of_game(True)

		return
