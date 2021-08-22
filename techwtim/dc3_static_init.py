# program: dark castle v3.30
# name: Tom Snellgrove
# date: Aug 17, 2021
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
		'introduction' : "Greetings brave adventurer!\n\nYou are Burt-the-Boneheaded, the only adventurer brave - or foolish - enough to enter the Dark Castle in search of treasure.\n\nType 'help' for help.\n\n",
		'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'one-word-commands', 'verbs', 'abbreviations', 'adjectives', prepositions', 'articles'.",
		'credits' : "Written and programmed by Tom. Thanks to Toby, Joshua, JoyEllen, Milo, Gideon, Franco, Karl, Andy, Ken and Alec for advice and playtesting!!",
		
		### help subsystem - non-objects ###
		'help_basics' : "You can 'take' one object into your hand at a time. Your other hand is holding your light source. If you are already holding an item when you take something, the first item you were holding goes into your backpack. You can view what you're carying using 'inventory'. Type 'quit' to quit.  Start multi-word commands with a verb.",
		'help_adjectives' : "Nearly all nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
		'help_prepositions' : "The only available preposition is 'in' and it is only used with the verb 'put'. This allows you to put items in containers. Example: 'put the rusty key in the wooden chest'",
		
		### universal objects ###
		'backpack' : "Your trusty, well-worn leather backpack",
		'burt' : "Yep, that's you Burt. A fine specimen of a man. If not for the drooling and the farting I don't know how you'd fend off the ladies.",
		'fist' : "Yep, that's your fist. Still bruised from the last time you swung and missed and hit a wall...", 
		'conscience' : "Burt, Dark Castle is quite murky enough without pondering your prodigal and Hal-esque misspent youth!",
		'faded_tapestries' : "The Main Hall Faded Tapestries are vast and elaborate, covering both the east and the west walls. They appear to depict an unkempt figure breaking into a solitary white house and from there pillaging a Great Underground Empire. Strangely, there is a looming figure near the top of the west tapestry who appears to be tapping with his fingers on a many-buttoned plank and staring intently into a window filled with text. For some reason the figure disconcerts you.. his presence in the Faded Tapestries fills you with existential dread and forces you to question your agency and the very nature of your being... BURT!! Get hold of yourself man! You're a mangey, pub-crawling adventurer who lives in his mom's basement. You don't even know what half those words mean. Stop staring at tapestries and get out there and find the treasure you fool!!",

		### writing objects ###
		'rusty_lettering' : "'ABANDON HOPE ALL YE WHO EVEN THINK ABOUT IT'",
		'dwarven_runes' : "'Goblin Wallopper'",

		'messy_handwriting' : "...ode is X...",
		
		### ViewOnly objects ###
		'dark_castle' : "Dark Castle looms over you. Its facade of blackened turrets and cracked walls is dour and singlularly univiting. It's hard to imagine but your great grandma Nana used to tell wonderous stories of the old days when the castle gleamed brightly on its hill and was a beacon of order and goodness for the land. Maybe it's because of the stories but you've always had a bit of an itch to venture inside. The place has somehow called to you - almost daring you to enter - and now that a round of beer and your alehouse repuation as a fearless ruffian are on the line you intend to answer the call!",		
		'moat' : "You know Burt, you've never heard anyone say 'It's a hot out - I think I'll go for a swim in the Dark Castle moat'... and now you know why. The dark and muddy water is singularly uninviting and it swirls in a way that makes you suspect there's something down there you'd rather not meet.",
		'alcove' : "A small indentation in the west wall near the Iron Portcullis. It is just deep enough to hold one Control Panel and one Goblin.",
		'control_panel' : "The Control Panel contains three levers: a Left Lever, a Middle Lever, and a Right Lever. The control panel also contains a Big-Red-Button. There are no directions posted as to what the controls are for or how to use them (a clear ISO lapse if ever you've seen one Burt).",
		
		### item objects ###
		'rusty_key' : "An old Rusty Key... the one they gave you at the pub when you swore to pillage the Dark Castle. What could you possibly do with it?",
		'shiny_sword' : "The Shiny Sword glitters even in the dim light. Despite its age, the edge is keen and looks ready for action. There are Dwarven Runes engraved upon the blade.",

		'brass_key' : "The key is brass.",
		'bubbly_potion' : "The cork-stopperd glass vial contains a bubbly green potion.",
		'torn_note' : "The note is ragged and torn. On it there is some messy handwriting.", 
		
		### container objects ###
		'wooden_chest' : "An old wooden chest.",
		
		### door objects ###
		'front_gate' : "The Front Gate is just north of the Dark Castle's drawbridge. It is 10 feet tall and reenforced with steel bands. Imposing indeed! There is Rusty Lettering across the top of the gate and a rusty keyhole next to a handle.",
		
		'iron_portcullis' : "Beyond the iron portcullis you can dimly make out the next room.",
		
		### room objects ###
		'entrance' : "*** Entrance ***\n\nYou are standing atop the drawbridge before the daunting entrance of Dark Castle. To the north is the Front Gate. To the south the way back home. To the east and west and below you is the Moat.",
		'main_hall' : "*** Main Hall ***\n\nYou are standing in what was once the sumptuous main hall of the castle. Faded Tapestries hang on the east and west walls. The Front Gate is to the south. And a foreboding archway leads to the north.",

		'antechamber' :"*** Antechamber ***\n\nYou are standing in a what feels more like a wide, tall-ceilinged corridor than a room. Apparently this is the room-before-the-room, the pre-room before the really, really grand room that comes after it. If so, the next room must be quite something because back in it's day this spot was clearly impressive. Alas, like all of the castle it has fallen on dark times and now feels more sinister than grand. The east and west walls are bare stone. To the south is an open passageway leading to the Main Hall and to the north there is an Iron Portcullis that guards the path to the grand chamber beyond. Near the Iron Portcullis on the west wall there is a small Alcove. It appears to have a Control Panel with some levers and a Big-Red-Button on it but you can't see it very well due to the dim light. The whole north end of the room is cloaked in shadows that make you uneasy."
}

