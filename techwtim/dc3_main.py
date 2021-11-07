# program: dark castle v3.48
# name: Tom Snellgrove
# date: Oct 22, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								integrate triggers, replicate full original, add more puzzles!

### import statements
import sys
from dc3_wrapper import wrapper

### main routine
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
