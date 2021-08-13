# program: dark castle v3.20
# name: Tom Snellgrove
# date: Aug 6, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!

# import statements
import sys
import dc3_init
from dc3_startup import start_me_up

# main
start_me_up()
from dc3_demo import wrapper
end_of_game = False

while end_of_game == False:
		user_input = input('Type your command: ')
		end_of_game, output = wrapper(user_input)
		print(output)
print("THANKS FOR PLAYING!!")