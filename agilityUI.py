from agility import *

dog_name = "Canon"

while True:
	print "How would you like to view " + dog_name + "'s records?"
	print "Your choices are: 'level', 'class', 'trial', 'nadacyear', 'lifetime'"
	print "If you are finished, please type 'exit'"
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
	elif question.lower() == 'class':
		class_level = raw_input("Please choose a class by entering one of the following:" + "\n" + "'Regular'" + "\n" + "'Jumpers'" + "\n" + "'Chances'" + "\n" + "'Tunnelers'" + "\n" + "'Touch 'n Go'" + "\n" + "'Weavers'" + "\n" + "'Hoopers'" + "\n")
		input = class_level.lower()
		if input == "regular":
			classSort(filename, input)
		elif input == "jumpers":
			classSort(filename, input)
		elif input == "chances":
			classSort(filename, input)
		elif input == "tunnelers":
			classSort(filename, input)
		elif input == "touch 'n go":
			classSort(filename, input)
		elif input == "weavers":
			classSort(filename, input)
		elif input == "hoopers":
			classSort(filename, input)
		else:
			print "try again"


	elif question.lower() == 'exit':
		print "Good Day!"
		break
		





