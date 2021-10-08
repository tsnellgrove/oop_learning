# program: dark castle v3.44
# name: Tom Snellgrove
# date: Oct 7, 2021
# description: static dictionary initialization function module


### this module declares static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => helper => classes => obj_init2) ###

### interpreter function language variables ###
articles_lst = ['a', 'an', 'the']

one_word_only_lst = ['help', 'credits', 'score', 'version', 'inventory', 'look', 'quit', 'xyzzy42']

verbs_lst = ['help', 'examine', 'read', 'go', 'take', 'drop', 'unlock', 'open', 'close', 'lock', 'put', 'eat', 'drink']

abbreviations_dict = {
		'n' : 'north',
		's' : 'south',
		'e' : 'east',
		'w' : 'west',
		'i' : 'inventory',
		'l' : 'look',
		'get' : 'take',
		'x' : 'examine',
		'q' : 'quit',
		'h' : 'help'
}

one_word_convert_dict = {
		'north' : 'go',
		'south' : 'go',
		'east' : 'go',
		'west' : 'go'
}


### static dictionary ###
static_dict = {
		'version' : '3.42',
		'max_score' : 75,
}


### score dictionaries and lists ###
score_val_dict = {
		'rusty_key' : 5,
		'main_hall' : 10,
		'shiny_sword' : 10,
		'throne_room' : 10,
		'silver_key' : 5,
		'kinging_scroll' : 5
}

item_score_lst = [
		'rusty_key',
		'shiny_sword',
		'silver_key',
		'kinging_scroll'
]

room_score_lst = [
		'main_hall',
		'throne_room'
]


### description dict ###
descript_dict = {
		### one-word commands - non-objeects ###
		'introduction' : "Greetings brave adventurer!\n\nYou are Burt-the-Boneheaded, the only adventurer brave - or foolish - enough to enter the Dark Castle in search of treasure.\n\nType 'help' for help.\n\n",
		'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'one-word-commands', 'verbs', 'abbreviations', 'adjectives', prepositions', 'articles', 'read'.",
		'credits' : "Written and programmed by Tom. Thanks to Toby, Joshua, JoyEllen, Milo, Gideon, Franco, Karl, Andy, Ken and Alec for advice and playtesting!!",
		
		### help subsystem - non-objects ###
		'help_basics' : "Objects you can examine and interact with are capitalized. Use 'read' (not 'examine') to read text you find written on objects. You can 'take' one object into your hand at a time. Your other hand is holding your light source. In many cases you must be holding an object in your hand in order to act uppon it (e.g. 'unlock', drop', 'eat', 'put'). If you are already holding an item when you take something else, the original item you were holding is automatically transferred into your backpack. You can view what you're carying using 'inventory'. Use 'look' to get a description of the room you're in. Type 'quit' to quit.  Start all multi-word commands with a verb.",
		'help_adjectives' : "Most nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
		'help_prepositions' : "The only available preposition is 'in' and it is only used with the verb 'put'. This allows you to put items in containers. Example: 'put the rusty key in the wooden chest'",
		'help_read' :  "If you can't 'read' something (e.g. a note or a scroll) try 'examine' instead. The item may have some readable text written on it that you'll learn more about via 'examine'.",
		
		### universal objects ###
		'backpack' : "Your trusty, well-worn leather backpack",
		'burt' : "Yep, that's you Burt. A fine specimen of a man. If not for the drooling and the farting I don't know how you'd fend off the ladies.",
		'fist' : "Yep, that's your fist. Still bruised from the last time you swung and missed and hit a wall...", 
		'conscience' : "Burt, Dark Castle is quite murky enough without pondering your prodigal and Hal-esque misspent youth!",

		### wrong way errors ###
		'wrong_way_0' : "Ouch! Burt, stop walking into walls!",
		'wrong_way_1' : "Ouch! You have walked into a wall.",
		'wrong_way_2' : "There's no exit that way.",
		'wrong_way_3' : "You can't go that way.",
		'wrong_way_4' : "And exactly how do you propose to do that?",

		### interpreter errors ###
		'interp_error_0' : "Burt, I have no idea what you're talking about!",
		'interp_error_1' : "Burt, are you babbling again?",
		'interp_error_2' : "Burt, I'm just going to pretend I didn't hear that.",
		'interp_error_3' : "Burt, you've said some strange things over the years but that was a doosey!",
		'interp_error_4' : "Burt! What would your mother say if she heard you speaking like that!?",

		### writing objects ###
		'rusty_lettering' : "'ABANDON HOPE ALL YE WHO EVEN THINK ABOUT IT'",
		'dwarven_runes' : "'Goblin Wallopper'",
		'messy_handwriting' : "...ode is X. Don't tell anyo..",
#		'small_print' : "'ACME AXE: Effective at dispatching small dragons, large crocodiles, and even the most agressive of trees.'",
		'small_printing' : "'ACME AXE: Effective at dispatching small dragons, large crocodiles, and even the most agressive of trees.'",
		'illuminated_letters' : "First with great effort and then, surprisingly, with surety and confidence, you read out loud the text on the scroll. Your voice booms forth of its own accord - as if some part of your brain has been getting ready to say these words all your life. The rest of brain is struggling just to make sense of what you're saying with such confidence... it seems to be something along the lines of a recipe with ingredients... so if the 'heir to the true king' (whoever that might be)... reads 'this precious parchment'(you're pretty sure that means the scroll you're holding)... in the Throne Room (you've been there!)... while 'adorned with the gleaming headpiece of state' (whatever that means)... and also requiring that 'so long as the castle remains invested with a representative of our most noble heraldic charge seen ever upon our crest, seal, and glorious coat of arms' (even Ms. Lusk would have no clue what this means but she would notice that an awful lot of the Illuminated Letters in this sentence include a hedgehog with a sword and a key)... and then it finishes on a rather dramatic high note with the words 'upon the hour these conditions be met, a new King of Bright Castle shall shine forth and be proclaimed!'",
		'calligraphy' : "'The Kinging Scroll'",
		'trademark' : "'McVities'",
		
		### ViewOnly objects ###
		'dark_castle' : "Dark Castle looms over you. Its facade of blackened turrets and cracked walls is dour and singlularly univiting. It's hard to imagine but your great grandma Nana used to tell wonderous stories of the old days when the castle gleamed brightly on its hill and was a beacon of order and goodness for the land. Maybe it's because of the stories but you've always had a bit of an itch to venture inside. The place has somehow called to you - almost daring you to enter - and now that a round of beer and your alehouse repuation as a fearless ruffian are on the line you intend to answer the call!",		
		'moat' : "You know Burt, you've never heard anyone say 'It's a hot out - I think I'll go for a swim in the Dark Castle moat'... and now you know why. The dark and muddy water is singularly uninviting and it swirls in a way that makes you suspect there's something down there you'd rather not meet.",
		'alcove' : "A small indentation in the west wall near the Iron Portcullis. It is just deep enough to hold one Control Panel and one Goblin.",
		'faded_tapestries' : "The Main Hall Faded Tapestries are vast and elaborate, covering both the east and the west walls. They appear to depict an unkempt figure breaking into a solitary white house and from there pillaging a Great Underground Empire. Strangely, there is a looming figure near the top of the west tapestry who appears to be tapping with his fingers on a many-buttoned plank and staring intently into a window filled with text. For some reason the figure disconcerts you.. his presence in the Faded Tapestries fills you with existential dread and forces you to question your agency and the very nature of your being... BURT!! Get hold of yourself man! You're a mangey, pub-crawling adventurer who lives in his mom's basement. You don't even know what half those words mean. Stop staring at tapestries and get out there and find the treasure you fool!!",
		'stone_coffer' : "This is the sort of coffer that, in better days, was no doubt filled to the brim will brightly shining gold pieces. Unfortunately, as you'd begun to fear, those days are long past and now the coffer is filled only with a deep layer of dust.",
		'family_tree' : "It appears to show the family tree of the Flathead dynasty. Though generally agreed to have peaked (nadired?) during the reign of Dimwit Flathead and petered out shortly there-after during the inglorious rulership of Wurb Flathead, this Family Tree tells a different story. It claims that a remote uncle of Wurb continued the line for seven more generations and eventually ended with William 'The Wanderer' Flathead only a little over 100 years ago. The area below William is indistinct and feels incomplete.. as if there are details still waiting to be filled in.\n\nAt the very top of the family_tree you see a royal crest. Oddly enough, it appears to be a Hedgehog bearing a Shiny Sword and a Silver Key.",
		
		### item objects ###
		'rusty_key' : "An old Rusty Key... the one they gave you at the pub when you swore to pillage the Dark Castle. What could you possibly do with it?",
		'shiny_sword' : "The Shiny Sword glitters even in the dim light. Despite its age, the edge is keen and looks ready for action. There are Dwarven Runes engraved upon the blade.",
		'torn_note' : "This must have dropped from the Goblin's hand when you slew it. The Torn Note is ragged and only barely readable.", 
		'grimy_axe' : "A nasty looking weapon - and poorly maintained too. If you ever get out of this castle you should set aside some time to polish it. You notice uppon inspection that there is some Small Print on the handle.",
		'silver_key' : "The small silver_key glitters in the dim light. It certainly stands out in the otherwise dreary Dark Castle. If you find a glittering silver keyhole somewhere this is definitely the key for it!",
		'kinging_scroll' : "Wow this thing is fancy! Huge letters with little pictures inside them and all sorts of curvy flourish at the end of each and every letter. Burt, your humble biscuit-baking, pub-crawling brain doesn't even know what to call this thing but if it did you would call it an illuminated manuscript composed (of course) of Illuminated Letters. Thanks to the hard and thankless work of your first grade teacher, Ms. Lusk, you could probably just manage to read the Illuminated Letters.",

		### food objects ###
		'cheese_wedge' : "A small wedge of cheese you absconded with from the larder. It's very small - so small that a lone mouse could probably make off with the whole thing - but your mother was saving it for company so you suspect it's quite delicious.",
		'stale_biscuits' : "The Stale Biscuits are rather unappetizing. There is a Trademark baked into the biscuits.",

		### beverage objects ###
		'fresh_water' : "After your trudge up the hill to Dark Castle the Fresh Water looks invitingly refreshing.",

		### eat descriptions ###
		'cheese_eat' : "tastes delicious!",
		'biscuit_eat' : "taste like damp cardboard that's been run over by a cart. You rather regret eating them... especially as to some poor creature out there they might be a rare and wonderous delicacy.",

		### drink descriptions ###
		'water_drink' : "was refreshing!",

		### test objects ###
		'brass_key' : "The key is brass.",
		'bubbly_potion' : "The cork-stopperd glass vial contains a bubbly green potion.",
		'wooden_chest' : "An old wooden chest.",
				
		### container objects ###
		'crystal_box' : "Atop an ornate pillar to the left of the throne sits an intricate Crystal Box. The crystal panels are heavily leaded and skillfully carved such that you're unable to tell what may lie within. There is a silver keyhole on the front of the crystal_box that glitters brilliantly - much like the shiny_sword in fact - in the otherwise dark and brooding room. The top of the Crystal Box is engraved with Calligraphy.",
		
		### jug objects ###
		'glass_bottle' : "A clear glass bottle suitable for carrying a liquid. Alas, if only it was filled with ale...",
		
		### door objects ###
		'front_gate' : "The Front Gate is just north of the Dark Castle's drawbridge. It is 10 feet tall and reenforced with steel bands. Imposing indeed! There is Rusty Lettering across the top of the gate and a rusty keyhole next to a handle.",
		'iron_portcullis' : "Beyond the iron portcullis you can dimly make out the next room.",

		### machine objects ###
		'control_panel' : "The Control Panel contains three levers: a Left Lever, a Middle Lever, and a Right Lever. The control panel also contains a Big-Red-Button. There are no directions posted as to what the controls are for or how to use them (a clear ISO lapse if ever you've seen one Burt).",
		'throne' : "High-backed and intricately carved, the throne is secured to the floor and wedged against the castle wall behind it. It does not look entirely comfortable but it must have once been very grand indeed. Alas, like the rest of Dark Castle, it is now dingy and ominous with only faint hints of its past glory. It must have heard many secrets in its time... perhaps it still holds some?",
						
		### room objects ###
		'entrance' : "*** Entrance ***\n\nYou are standing atop the drawbridge before the daunting entrance of Dark Castle. To the north is the Front Gate. To the south the way back home. To the east and west and below you is the Moat.",
		'main_hall' : "*** Main Hall ***\n\nYou are standing in what was once the sumptuous main hall of the castle. Faded Tapestries hang on the east and west walls. The Front Gate is to the south. And a foreboding archway leads to the north.",

		'antechamber' :"*** Antechamber ***\n\nYou are standing in a what feels more like a wide, tall-ceilinged corridor than a room. Apparently this is the room-before-the-room, the pre-room before the really, really grand room that comes after it. If so, the next room must be quite something because back in it's day this spot was clearly impressive. Alas, like all of the castle it has fallen on dark times and now feels more sinister than grand. The east and west walls are bare stone. To the south is an open passageway leading to the Main Hall and to the north there is an Iron Portcullis that guards the path to the grand chamber beyond. Near the Iron Portcullis on the west wall there is a small Alcove. It appears to have a Control Panel with some levers and a Big-Red-Button on it but you can't see it very well due to the dim light. The whole north end of the room is cloaked in shadows that make you uneasy.",
		
		'throne_room' : "*** Throne Room ***\n\nThe room you're currently in is vast - almost cavernous. At the far end sits what must have once been a grand and glorious Throne. To the right of the Throne is a giant Stone Coffer and to the left an elegant pedestal that holds what appears to be a delicate Crystal Box. On either wall there are tall windows - now shattered and ruined but you've heard stories of the glowing stained glass that once filled them. And above the room's entrance hangs a vast (though quite dusty) Family Tree."
}

