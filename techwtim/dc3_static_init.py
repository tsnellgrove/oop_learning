# program: dark castle v3
# name: Tom Snellgrove
# date: June 4, 2021
# description: static dictionary initialization function module for a zork-like text adventure game
# goals vs. dc2: oop, modular, db integration, improved interpreter


### static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => helper => classes => init) ###
static_dict = {
		'version' : '3.01',
		'max_score' : 75,
}

