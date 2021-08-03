# program: dark castle v3.11
# name: Tom Snellgrove
# date: Aug 1, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!

# import statements
import sys
from dc3_startup import start_me_up
#from dc3_demo import interpreter
from dc3_demo import wrapper

# main routine
start_of_game = True
end_of_game = False
output = ""
while end_of_game == False:
		if start_of_game:
				output = start_me_up()
				start_of_game = False
		else:
				user_input = input('Type your command: ')
#				end_of_game, output = interpreter(user_input)
				end_of_game, output = wrapper(user_input)
		print(output)
print("THANKS FOR PLAYING!!")
