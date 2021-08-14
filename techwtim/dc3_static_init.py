# program: dark castle v3.20
# name: Tom Snellgrove
# date: Aug 6, 2021
# description: static dictionary initialization function module


### this module declares static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => helper => classes => obj_init2) ###

### interpreter function language variables ###
articles_lst = ['a', 'an', 'the']
one_word_only_lst = ['help', 'credits', 'score', 'version', 'inventory', 'look', 'quit', 'xyzzy42']
verbs_lst = ['help', 'examine', 'read', 'go', 'take', 'drop', 'unlock', 'open', 'close', 'lock', 'put']
abbreviations_dict = {
		'n' : 'north',
		's' : 'south',
		'e' : 'east',
		'w' : 'west',
		'i' : 'inventory',
		'l' : 'look',
		'get' : 'take',
		'x' : 'examine',
		'q' : 'quit'
}
one_word_convert_dict = {
		'north' : 'go',
		'south' : 'go',
		'east' : 'go',
		'west' : 'go'
}

### static dictionary ###
static_dict = {
		'version' : '3.10',
		'max_score' : 75,
}

### description dict ###
descript_dict = {
		### one-word commands - non-objeects ###
		'introduction' : "Greetings brave adventurer!\n\nYou are Burt-the-Boneheaded, the only adventurer brave - or foolish - enough to enter the Dark Castle in search of treasure.\n\nType 'help' for help.",
		'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'one-word-commands', 'verbs', 'abbreviations', 'adjectives', prepositions', 'articles'.",
		'credits' : "Written and programmed by Tom. Thanks to Toby, Joshua, JoyEllen, Milo, Gideon, Franco, Karl, Andy, Ken and Alec for advice and playtesting!!",
		
		### help subsystem - non-objects ###
		'help_basics' : "You can 'take' one object into your hand at a time. Your other hand is holding your light source. If you are already holding an item when you take something, the first item you were holding goes into your backpack. You can view what you're carying using 'inventory'. Type 'quit' to quit.  Start multi-word commands with a verb.",
		'help_adjectives' : "Nearly all nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
		'help_prepositions' : "The only available preposition is 'in' and it is only used with the verb 'put'. This allows you to put items in containers. Example: 'put the rusty key in the wooden chest'",
		
		### universal objects ###
		'dark_castle' : "The evil Dark Castle looms above you",
		'backpack' : "Your trusty, well-worn leather backpack",
		'burt' : "Yep, that's you Burt. A bit mangy and odd but undeniably lovable",
		'fist' : "That is indeed your very own fist", 
		'conscience' : "A tad murky Burt - what would your dear old Nana say?",
		'alcove' : "A small indentation in the west wall near the iron_portcullis. It is just deep enough to hold one control panel and one goblin.",
		'control_panel' : "The control_panel contains three levers: a left lever, a middle lever, and a right lever. The control panel also contains a Big-Red-Button. There are no directions posted as to what the controls are for or how to use them (a clear ISO lapse is ever you've seen one Burt).",
		
		### writing objects ###
		'rusty_letters' : "'Abandon Hope All Ye Who Even Thank About It'",
		'dwarven_runes' : "'Goblin Wallopper'",
		'messy_handwriting' : "...ode is X...",
		
		### item objects ###
		'rusty_key' : "The key is rusty.",
		'shiny_sword' : "The sword is shiny.",
		'brass_key' : "The key is brass.",
		'bubbly_potion' : "The cork-stopperd glass vial contains a bubbly green potion.",
		'torn_note' : "The note is ragged and torn. On it there is some messy handwriting.", 
		
		### container objects ###
		'wooden_chest' : "An old wooden chest.",
		
		### door objects ###
		'front_gate' : "The front gate is massive and imposing.",
		'iron_portcullis' : "Beyond the iron portcullis you can dimly make out the next room.",
		
		### room objects ###
		'entrance' : "*** Entrance ***\n\nYou stand before the daunting front gate of Dark Castle. In front of you is the front gate.",
		'main_hall' : "*** Main Hall ***\n\nA vast and once sumptuous chamber. The main gate is south. There is a passage going north.",
		'antechamber' :"*** Antechamber ***\n\nYou are standing in a what feels more like a wide, tall-ceilinged corridor than a room. Apparently this is the room-before-the-room, the pre-room before the really, really grand room that comes after it. If so, the next room must be quite something because back in it's day this spot was clearly impressive. Alas, like all of the castle it has fallen on dark times and now feels more sinister than grand. The east and west walls are bare stone. To the south is an open passageway leading to the main_hall and to the north there is an iron portcullis that guards the path to the grand chamber beyond. Near the ironportcullis on the west wall there is a small alcove. It appears to have a control panel with some levers and a big red button on it but you can't see it very well due to the dim light. The whole north end of the room is cloaked in shadows that make you uneasy."
}

