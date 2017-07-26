#~ x = 0
#~ while x < 100:
	#~ x+= 1
	#~ print ("{} Doodle").format(x)
	
class Sublime():
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def format_title(self):
		return (self.name.title(), self.age)

name = input("Please enter your first name: ")
age = input ("Please enter you age: ")

person = Sublime(name, age)

print ("\nYou are %s and you are %s years old." % person.format_title() ) 	
	

