# program: dark castle v3.42
# name: Tom Snellgrove
# date: Oct 2, 2021
# description: main and interpreter modules for a zork-like text adventure game
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								db integration, avoid external triggers, 
#								replicate full original, add more puzzles!

# import statements
print("main - start")

import sys
#from dc3_demo import wrapper
from dc3_wrapper import wrapper

print("main post imports") # troubleshooting

end_of_game = False
start_of_game = True
while end_of_game == False:

		print("main while loop start") # troubleshooting

		if start_of_game:
				user_input = "xyzzy42"
				start_of_game = False
		else:
				user_input = input('Type your command: ')
		end_of_game, output = wrapper(user_input)
		print(output)
print("THANKS FOR PLAYING!!")

print("main end") # troubleshooting
