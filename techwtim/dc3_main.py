# import statements
import sys
#import pickle
#from itertools import islice
#from dc3_static_init import *
#from dc3_classes import *
# from dc3_init import *
#from dc3_helper import *
from dc3_startup import startup
#from  dc3_obj_init2 import *
## from dc3_interp_helper import *
#import gc # only used for troubleshooting
## from dc3_obj_init import obj_init
from dc3_demo import interpreter

# main routine
start_of_game = True
end_of_game = False
while end_of_game == False:
		if start_of_game:
##				user_input = "xyzzy42" # the magic word!!
				output = startup()
				start_of_game = False
		else:
				user_input = input('Type your command: ')
				end_of_game, output = interpreter(user_input)
##		end_of_game, output = wrapper(user_input)
##		end_of_game, output = wrapper(user_input, stateful_dict)
		print(output)
print("THANKS FOR PLAYING!!")
