# Tech with Tim - Software Design
# Link: https://youtu.be/-njsRb8Tn70
# A) 0:00 - Example 1 - Common Design Mistakes
# B) 8:20 - Example 2 - Separate methods or functions that do just one thing
# C) 18:30 - Example 3 -
# D) 23:50 - splitting functions into cohesive modules


# *** Example 3 - 
# Problems: 1) Not cohesive - both list functins and hash functions

# Better would be two functins - one for lists and one for HT
# Now we have 2 cohesive functions




"""
LIST FUNCTIONS
"""

def	get_max(lst):
		mx = float("-inf")
	
		for num in lst:
				if num > mx:
						mx = num
						
		return mx
		
def get_min(lst):
		mn = float("inf")
		
		for num in lst:
				if num < mn:
						mn = num
						
		return num
		
def get_average(lst):
		return sum(lst) / len(lst)
		
def get_median(lst):
		lst = sorted(lst)
		
		if len(lst) % 2 == 0:
				return (lst[ (len(lst)/2)-1] + lst[(len(lst))]) / 2
		else:
				return lst[(len(lst)-1)]/2

list = [1,2,3,4,5]
length = len(list)
mod2 = length % 2
median = get_median(list)
print(length, mod2, median)				
# Plus more has tabel examples. All saved in mathfunctions module to be imported and called



# *** Example 2 - Solution 2

# Want small cohesive methods in same class; break into atomic pieces
# good input validation
# range easily changable
# number easily changeable
# game is easily callable externally
# method does one thing and does it well; avoids monolithic mega function!
# separate things into functions or methods that do ONE THING and do that one thing very well
# Want to ensure functions & methods don't have "side effects"

class GuessNumber:
		def __init__(self, number, mn=0, mx=100):
				self.number = number
				self.guesses = 0
				self.min = mn
				self.max = mx
				
		def get_guess(self): # just gest guess from user
				guess = input(f"Please guess a number ({self.min} - {self.max})") # range is not hard coded
				
				if self.valid_number(guess):
						return int(guess)
				else:
						print("Please enter a valid number.")
						return self.get_guess() # recursively calls get_guess in order to get a valid guess
						
		def valid_number(self, str_number):
				try:
						number = int(str_number)
				except:
						return False
						
				return self.min <= number <= self.max
				
		def	play(self):
				while True:
						self.guesses += 1
						
						guess = self.get_guess()
						
						if guess < self.number:
								print("Your guess was under.")
						elif guess > self.number:
								print("Your guess was over.")
						else: # they guessed it
								break
					
				print(f"You guessed it in {self.guesses} guesses")
					
game = GuessNumber(56, 0, 100)
#game.play()


# *** Example 2 - Solution 1

# Problems:
# 1) Number is hard coded; hard to change
# 2) range is not enforced and is hard coded
# 3) Can't easily add random number


# guess = 1

# while True:
#		num = input("Please guess the number (between 0-100): ")
#		try:
#				num = int(num)
#		except:
#				print("Invalid number, please guess again.")
				
#		if num < 45:
#				print("Your guess was under.")
#		elif num > 45:
#				print("Your guess was over.")
#		else:
#				break
		
#		guess += 1
		
# print(f"You guessed it in {guess} guesses")


# **************************************


# *** Example 1 - Common Design Mistakes ***

# Program Goal: print a list of words delimited by commas

# Solution 1: What's wrong?
# Problem 1: Not flexible - hard to add another word
# Problem 2: Can't change delimeter easily (requirements locked in)

list_of_words = ["hello", "yes", "goodbye", "last", "hello"]
# print(list_of_words[0] + ", " + list_of_words[1] + ", " + list_of_words[2] + ", " + list_of_words[3])



# Example 1 - Common Design Mistakes

# Program Goal: print a list of words delimited by commas

# Solution 2: What's wrong?
# Now a little easier to change delimeter but "4" is still hard coded
# should link to len of list


list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(4):
		to_print += list_of_words[i]
		if i != 3:
					to_print += ", "
					
# print(to_print)

# Solution 2.5
# A bit better: 
	
list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(len(list_of_words)):
		to_print += list_of_words[i]
		if i != len(list_of_words) - 1:
					to_print += ", "
					
# print(to_print)



# Solution 3:
# Getting there

list_of_words = ["hello", "yes", "goodbye", "last"]

# print(", ".join(list_of_words))


# Solution 4:
# Best solution

DELIMETER = ","
list_of_words = ["hello", "yes", "goodbye", "last"]
# print(DELIMETER.join(list_of_words))

