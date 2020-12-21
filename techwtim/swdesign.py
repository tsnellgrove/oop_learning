# Tech with Tim - Software Design
# Link: https://youtu.be/-njsRb8Tn70
# A) 0:00 - Example 1 - Common Design Mistakes
# B) 8:20 - Example 2 - 


# Example 1 - Common Design Mistakes

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
print(DELIMETER.join(list_of_words))

