# program: dark castle v3.01
# name: Tom Snellgrove
# date: June 5, 2021
# description: static dictionary initialization function module


### this module declares static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => helper => classes => init) ###

### static dictionary ###
static_dict = {
		'version' : '3.01',
		'max_score' : 75,
}


### description dict ###
descript_dict = {
		'introduction' : "Greetings brave adventurer!\n\nYou are Burt-the-Boneheaded, the only adventurer brave - or foolish - enough to enter the Dark Castle in search of treasure.\n\nType 'help' for help.",
		'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'one-word-commands', 'verbs', 'abbreviations', 'adjectives', prepositions', 'articles'.",
		'credits' : "Written and programmed by Tom. Thanks to Toby, Joshua, JoyEllen, Milo, Gideon, Franco, Karl, Andy, Ken and Alec for advice and playtesting!!",
		'help_basics' : "You can 'take' one object into your hand at a time. Your other hand is holding your light source. If you are already holding an item when you take something, the first item you were holding goes into your backpack. You can view what you're carying using 'inventory'. Type 'quit' to quit.  Start multi-word commands with a verb.",
		'help_adjectives' : "Nearly all nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
		'help_prepositions' : "The only available preposition is 'in' and it is only used with the verb 'put'. This allows you to put items in containers. Example: 'put the rusty key in the wooden chest'"
}
