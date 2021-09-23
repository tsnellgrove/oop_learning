# program: dark castle v3.40
# name: Tom Snellgrove
# date: Sept 5, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!

# import statements
import sys
import dc3_init
from dc3_demo import wrapper
###from dc3_static_init import *

# main
###print(descript_dict["introduction"])
###print(descript_dict["entrance"])
###print()

end_of_game = False
start_of_game = True
while end_of_game == False:
		if start_of_game:
				user_input = "xyzzy42"
				start_of_game = False
		else:
				user_input = input('Type your command: ')
		end_of_game, output = wrapper(user_input)
		print(output)
print("THANKS FOR PLAYING!!")
