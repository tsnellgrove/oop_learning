# Tech with Tim

# Python Objects & Classes Tutorial 6
# Link: https://youtu.be/xY__sjI5yVU
# Title: Public & Private Classes

class _Private: # Private = only used within limited scope; is a convention but no formal restriction; initial "_" implies Private
		def __init__(self, name):
				self.name = name


class NotPrivate: # Can be accessed by everyone; 
		def __init__(self, name):
				self.name = name
				self.priv = _Private(name)
		
		def _display(self): # Private method (convention only)
				print("Hello")
				
		def display(self): # Public method
				print('Hi')


# To use a class in another file, first: 'import <file>'
# now, can use a class in file via x = <file>.<class> convention
# Alternatively, can import the class so as to avoid <file>.<class>: 'from <file> import <class>'




# Python Objects & Classes Tutorial 5
# Link: https://youtu.be/MpuOuZKWUWw
# 0:00 - 0:15 = Intro
# 0:15 - 4:00 = Class Variables


class Dog:
		dogs = [] # class variable; must be inside class to reference; better practice if will be used 'staticaly'; dogs is not specific to instance - is the same for all objects in class; is class-wide
		
		def __init__ (self, name):
				self.name = name
				self.dogs.append(self)

		# decorators denote a special method - static and class methods can be very useful

		@classmethod # decorator - can call it on name of class
		def num_dogs(cls):
				return len(cls.dogs)
												
		@staticmethod # decorator - doesn't require class to be called - don't have to pass in class - just using as function but want to organize in class
		def bark(n):
				"""barks n times"""
				for _ in range(n):
						print("Bark!")

# tim = Dog("Tim")
# jim = Dog("Jim")
# print(Dog.dogs) # can reference class variable as a class - not neccessarily by a specific instance
# print(tim.dogs) # But can also reference class variable by instance if desired - same output as for class
# print(Dog.num_dogs()) # class method can be run against the class itself!
# print(tim.num_dogs()) # class method can be run on object instance but still gives class answer
# Dog.bark(5) # static method does not require any reference to class or instance



# Python Objects & Classes Tutorial 4
# Link: https://youtu.be/39m3rstTN8w
# 0:00 - 6:20 = create point math
# 6:20 - end = override methods

# How would I use this for Dark Castle? Would I use it? Possibly for triggers???



class Point():
		def __init__(self, x=0, y=0):
				self.x = x
				self.y = y
				self.coords = (self.x, self.y)
				
		def move(self, x, y):
				self.x += x
				self.y += y

		def __add__(self, p): # We are "overloading" Python's built in "+" method and defining a specific method for "+" in the context of our Point class
				return Point(self.x + p.x, self.y + p.y)

		def __sub__(self, p):
				return Point(self.x - p.x, self.y - p.y)

		def __mul__(self, p):
				return self.x * p.x + self.y * p.y

		def length(self):
				import math
				return math.sqrt(self.x**2 + self.y**2)

		def __gt__(self, p):
				return self.length() > p.length()
		
		def __ge__(self, p):
				return self.length() >= p.length()			
			
		def __lt__(self, p):
				return self.length() < p.length()			
		
		def __le__(self, p):
				return self.length() <= p.length()			
			
		def __eq__(self, p):
				return self.x == p.x and self.y == p.y		

		def __str__(self):
				return "(" + str(self.x) + ", " + str(self.y) + ")"

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

p5 = p1 + p2 
p6 = p4 - p1
p7 = p2 * p3

# print(p5, p6, p7)
# print(p1 == p2)
# print(p1 > p2)
# print(p4 <= p3)


# Python Objects & Classes Tutorial 3
# Link: https://youtu.be/H2SQrZK2nvM
# 0:00 - 5:15 = simple inheritance
# 5:15 - 7:45 = overriding parent methodes / attributes


# Goal: One really general class that is "smaller" that applies to a bunch of sub-classes


class Vehicle():
		def __init__(self, price, gas, color):
				self.price = price
				self.gas = gas
				self.color = color
				
		def fillUpTank(self):
				self.gas = 100
				
		def emptyTank(self):
				self.gas = 0
				
		def gasLeft(self):
				return self.gas
				
class Car(Vehicle):
		def __init__(self, price, gas, speed, color):
				super().__init__(price, gas, color)
				self.speed = speed
		
		def beep(self):
				print('beep beep')

class Truck(Vehicle):
		def __init__(self, price, gas, tires, color):
				super().__init__(price, gas, color)
				self.tires = tires
		
		def beep(self):
				print('honk honk')

supe = Car(100, 50, 'fast', 'white')
bigred = Truck(150, 75, 'slow', 'red')
# supe.beep()
# bigred.beep()


# NEXT: Tom Example
# inheritance
# Create Door as child of Item [DONE]
# Create ViewOnly as parent to Item [DONE]
# Create Container as child to door [DONE]
# Create take & drop methods for Item [DONE]
# Create unlock method for Door & Container [DONE]
# Create open method for Door [DONE]
# Create a Room child class of view_only... focus on inventory only - not movement [DONE]
# Exercise inventory management using Room.room_objects and hand and take and drop [IN-PROC]
	# Update Room examine, take, and drop [DONE]
	# Test implementation [TBD]
# More classes before this gets out of hand! [TBD]
# Not: I think I'm doing something wrong... inventory management with objects is not as elegant as I was expecting


# Think through writing attribute for ViewOnly [TBD]
# Too many calsses already... think about consolidation [TBD]



hand = []
backpack = []
room = 'entrance'


class ViewOnly(object):
		def __init__(self, name, desc):
				self.name = name
				self.desc = desc

		def examine(self):
				print(self.desc)
		
		def change_desc(self, new_desc):
				self.desc = new_desc

		def add_writing(self, text_desc, text):
				self.desc = self.desc + " On the " + self.name + " there is " + text_desc + "."
				self.text = text

		def read_writing(self):
				try:
						print(self.text)
				except:
						print("There's nothing to read!")

class Room(ViewOnly):
		def __init__(self, name, desc, room_objects):
				super().__init__(name, desc)
				self.room_objects = room_objects
				
		def examine(self):
				print(self.desc)
				print("The room contains: " + ', '.join(self.room_objects))

class Item(ViewOnly):
		def __init__(self, name, desc, takeable):
				super().__init__(name, desc)
				self.takeable = takeable
				
		def take(self):
				if self.name in eval(room).room_objects:
						if len(hand) == 0:
								hand.append(self.name)
								eval(room).room_objects.remove(self.name)
								print('taken')
						else:
								print('Your hand is full.')
				else:
						print("There's no " + self.name + " to take here!")

		def drop(self):
				if self.name in hand:
						hand.remove(self.name)
						eval(room).room_objects.append(self.name)
						print("Dropped")
				else:
						print("You're not holding the " + self.name + " in your hand.")	

																
class Door(ViewOnly):
		def __init__(self, name, desc, open_state, unlock_state, key):
				super().__init__(name, desc)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key
				
		def unlock(self):
				if self.unlock_state == False:
						if self.key in hand:
								print("Unlocked")
								self.unlock_state = True
						else:
								print("You aren't holding the key.")
				else:
						print("The " + name + " is already unlocked.")

		def open(self):
				if self.open_state == False:
						if self.unlock_state == True:
								self.open_state = True
								print("Openned.")
						else:
								print("The " + self.name + " is locked.")
				else:
						print("The " + self.name + " is already open.")			


class Container(Door, Item):
		def __init__(self, name, desc, open_state, unlock_state, key, takeable, contains): # in this impplementation, containers cannot be taken
				super().__init__(name, desc, open_state, unlock_state, key, takeable)
#				super().__init__(takeable)
				self.contains = contains


dark_castle = ViewOnly('Dark Castle', 'The evil Dark Castle looms above you')
entrance = Room('Entrance', 'You stand before the daunting gate of Dark Castle. In front of you is the gate', ['sword', 'rusty_key', 'gate'])
rusty_key = Item('rusty_key', 'The key is rusty', True)
sword = Item('sword','The sword is shiny.', True)
gate = Door('Front Gate', 'The front gate is massive and imposing', False, False, 'rusty_key')
gate.add_writing('rusty letters', "The Rusty Letters read: 'Abandon Hope All Ye Who Even Thank About It'")
sword.change_desc(sword.desc +' On the sword blad you see Dwarven Runes.')
sword.add_writing('Dwarven Runes', "Goblin Wallopper")
chest = Container('chest', 'An old wooden chest', False, True, 'brass_key', False, 'potion')
giftbox = Container('giftbox', 'A pretty gift box', False, True, 'none', True, 'necklace')

# entrance.examine()
# dark_castle.examine()
# gate.examine()
# gate.read_writing()
# sword.examine()
# sword.take()
# print(hand)
# sword.take()
# sword.drop()
# gate.open()
# gate.unlock()
# rusty_key.examine()
# rusty_key.take()
# print(hand)
# gate.unlock()
# gate.open()
# gate.open()
# print(eval(room).room_objects)


# sword = Item('sword','The sword is shiny.', True, 5)
# sword.examine()
# sword.change_desc('The sword is rusty.')
# sword.examine()
# print(sword.takeable)
# print(sword.weight)
# sword.add_writing('dwarven runes', 'Goblin Wallaper')
# sword.examine()
# sword.read_writing()
# gate = Door('front gate', 'The front gate is daunting', False, False)
# gate.examine()
# gate.change_desc('The front gate is HUGE!')
# gate.examine()
# gate.read_writing()
# gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
# gate.read_writing()



class Dog(object): # parent or super class
		def __init__(self, name, age): 
				self.name = name
				self.age = age

		def speak(self):
				print("Hi, I am ", self.name, "and I am ", self.age, " years old")

		def talk(self):
				print("Bark!")

class Cat(Dog): # Class inherets the Dog Class; this is the child or derrived class
		def __init__(self, name, age, color):
				super().__init__(name, age) # calls the initialization of Dog (the super class)
				self.color = color
				self.name = "tech"

		def talk(self): # local child method over-rides parent method of same name
				print("Meow!")

tim = Cat('tim', 5, 'blue')
jim = Dog('jim', 70)
# tim.speak()
# tim.talk()
# jim.talk()


# Python Classes & Objects Tutorial 2
# Link: https://youtu.be/jQiUOV15IRI
# Topic: Creating your own ojbects & classes
# 0:00 Classes & Objects
# 9:45 Create new Attributes

# Tom Example
# objects are nouns, methods are verbs

class Item(object):
		def __init__(self, name, desc, takeable, weight):
				self.name = name
				self.desc = desc
				self.takeable = takeable
				self.weight = weight
	
		def examine(self):
				print(self.desc)
		
		def change_desc(self, new_desc):
				self.desc = new_desc

		def add_writing(self, text_desc, text):
				self.desc = self.desc + " On the " + self.name + " there is " + text_desc + "."
				self.text = text

		def read_writing(self):
				print(self.text)

sword = Item('sword','The sword is shiny.', True, 5)
#sword.examine()
sword.change_desc('The sword is rusty.')
# sword.examine()
#print(sword.takeable)
#print(sword.weight)
sword.add_writing('dwarven runes', 'Goblin Wallaper')
#sword.examine()
#sword.read_writing()




# Tim Example

class Dog(object):
		def __init__(self, name, age): # auto occurs upon class object instantiation
				# print("Nice, you made a dog!")
				self.name = name # name is an attribute of class Dog
				self.age = age
				self.li = [1,3,4] # note that attributes do not have to be passed into an object - they can be defined within the init

# notice the idiomatic use of 'self' as a default attribute - this is referencing the specific instance of the object

		def speak(self): # this is a method - it looks just like a function but has to be called using the class object
				print("Hi, I am ", self.name, "and I am ", self.age, " years old")

		def change_age(self, age):
				self.age = age

		def add_weight(self, weight):
				self.weight = weight

# classes allow you to create an infinite number of objects with each having all the attributes of the class


tim = Dog('Tim', 55) # tim is an instance of type / class Dog
fred = Dog('Fred', 3) # fred is another instance of type dog
tim.change_age(5)
# tim.speak()
# fred.speak()
# print(tim.age) # note that we can access object attributes directly
# print(tim.name)
# print(tim.li)
# print(fred.li)
tim.add_weight(70)
# print(tim.weight)


# Python Classes & Objects Tutorial 1
# Link: https://youtu.be/v_Jp11xqCzg
# Topic: Objects!


import turtle


x = 5
y = 'string'
f = 5.5

# print(type(x))
# print(type(y))

# help(str)

tim = turtle.Turtle()

def	func(x): # function
	return x + 1
	
# print(func(5))

# print(y.upper()) # method

# print(y.replace('s', ''))


