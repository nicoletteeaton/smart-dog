from agility import *

dog_name = "Canon"

while True:
	print "How would you like to view " + dog_name + "'s records?"
	print "Your choices are: 'level', 'class', 'trial', 'nadacyear', 'lifetime'"
	question = raw_input("Please sort " + dog_name + "'s records by:")

	if question.lower() == 'level':
		level = raw_input("Please choose a level by entereing: 'E', 'O', or 'N'")
		input = level.upper()
		if input == "E":
			levelSort(filename, input)
		elif input == "O":
			levelSort(filename, input)
		elif input == "N":
			levelSort(filename, input)
		else:
			print "try again"
		





