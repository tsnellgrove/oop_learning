# Tech with Tim

# Python Objects & Classes Tutorial 3
# Link: https://youtu.be/H2SQrZK2nvM
# 0:00 - 5:15 = simple inheritance


# NEXT: Tom Example
# inheritance
# Create Door as child of Item [DONE]
# Create ViewOnly as parent to Item [TBD]


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
				try:
						print(self.text)
				except:
						print("There's nothing to read!")
			
class Door(Item):
		def __init__(self, name, desc, takeable, weight, open_state, unlock_state):
				super().__init__(name, desc, takeable, weight)
				self.open_state = open_state


sword = Item('sword','The sword is shiny.', True, 5)
sword.examine()
sword.change_desc('The sword is rusty.')
sword.examine()
print(sword.takeable)
print(sword.weight)
sword.add_writing('dwarven runes', 'Goblin Wallaper')
sword.examine()
sword.read_writing()
gate = Door('front gate', 'The front gate is daunting', False, 0, False, False)
gate.examine()
gate.change_desc('The front gate is HUGE!')
gate.examine()
print(gate.takeable)
gate.read_writing()
gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
gate.read_writing()



class Dog(object): # parent or super class
		def __init__(self, name, age): 
				self.name = name
				self.age = age

		def speak(self):
				print("Hi, I am ", self.name, "and I am ", self.age, " years old")


class Cat(Dog): # Class inherets the Dog Class; this is the child or derrived class
		def __init__(self, name, age, color):
				super().__init__(name, age) # calls the initialization of Dog (the super class)
				self.color = color

tim = Cat('tim', 5, 'blue')
# tim.speak()



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


