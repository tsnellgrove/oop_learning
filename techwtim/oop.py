# Object Orientd Programming in Python
# Tech With Tim - Python Object Oriented Programming - For Beginners
# 1) 00:00 
# 2) 05:47
# 3) 16:45
# 4) 27:50
# 5) 41:00
# 6) 45:40

# ### 5) Class Methods ***



# *** 4) Class Atributes - can be useful as constants ***

class Person: # does NOT reference self; same for ALL instances
	number_of_people = 0
	GRAVITY = -9.8
	
	def __init__(self, name):
		self.name = name
		Person.number_of_people += 1

# Person.number_of_people = 8 # changes value for ALL instances!		
		
p1 = Person("tim")
#print(Person.number_of_people)
p2 = Person("jill")
#print(Person.number_of_people)




# *** 3.2) Pet, Dog, Cat, Fish - Objects with Inheritance ***

# parent / instantiated / super / upper / general class
class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I don't know what I say")

# parent / derived / lower classes
class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age) # ref super class for name & age
		self.color = color
		
	def speak(self): # supercedes default in Pet
		print("Meow")

	def show(self): # supercedes default in Pet
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
	def speak(self): # supercedes default in Pet
		print("Bark")	

class Fish(Pet):
	pass	

p = Pet("Tim", 19)
#p.show()
#p.speak()
c = Cat("Bill", 34, "Black")
#c.show()
#c.speak()
d = Dog("Jill", 25)
#d.show()
#d.speak()
f = Fish("Bubbles", 10)
#f.show()
#f.speak()


# *** 3.1) Dog & Cat - Objects without Inheritance ***

class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def speak(self):
		print("Meow")
		
class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def speak(self):
		print("Bark")


# *** 2) Student Roster Example - Classes Working Together ***

class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade # 0 - 100
		
	def get_grade(self):
		return self.grade
		
class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False
	
	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()
		return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
# print(course.add_student(s3))
# print(course.get_average_grade())

# print(course.students[0].name)


# *** 1) Dog Functionality Example - Basics of Objects ***

class Dog:

	def __init__(self, name, age): # defining a class
		self.name = name # nomenclature is "object.method"
		self.age = age

	def get_name(self): # defining a function
			return self.name
			
	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age

	def add_one(self, x):
		return x + 1
		
	def bark(self):
		print("bark")

d = Dog("Tim", 34)
d.set_age(23)
# print(d.get_age())
d2 = Dog("Bill", 12)
# print(d2.get_age())

# d.bark()
# print(d.add_one(5))
# print(type(d))


