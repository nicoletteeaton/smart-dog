from agility import *



while True:
	print "How would you like to view " + dog_name + "'s records?"
	print "Your choices are: 'level', 'class', 'trial', 'nadacyear', 'lifetime'"
	print "If you are finished, please type 'exit'"
	question = raw_input("Please sort " + dog_name + "'s records by:")

	if question.lower() == 'level':
		while True:
			level = raw_input("Please choose a level by entering:" + "\n" + "'E' for Elite" + "\n" + "'O' for Open" + "\n" + "'N' for Novice" + "\n" + "or 'B' to go back to choices" + "\n")
			input = level.upper()
			if input == "E":
				levelSort(filename, input)
			elif input == "O":
				levelSort(filename, input)
			elif input == "N":
				levelSort(filename, input)
			elif input == "B":
				break
					
			else:
				print "That didn't make sense"

	elif question.lower() == 'class':
		while True:
			class_level = raw_input("Please choose a class by entering one of the following:" + "\n" + "'R' for Regular" + "\n" + "'J' for Jumpers" + "\n" + "'C' for Chances" + "\n" + "'TN' for Tunnelers" + "\n" + "'TG' for Touch 'n Go" + "\n" + "'W' for Weavers" + "\n" + "'H' for Hoopers" + "\n" "or 'B' to go back to choices" + "\n")
			input = class_level.lower()
			if input == "r":
				classSort(filename, 'regular')
			elif input == "j":
				classSort(filename, 'jumpers')
			elif input == "c":
				classSort(filename, 'chances')
			elif input == "tn":
				classSort(filename, 'tunnelers')
			elif input == "tg":
				classSort(filename, "touch 'n go")
			elif input == "w":
				classSort(filename, 'weavers')
			elif input == "h":
				classSort(filename, 'hoopers')
			elif input == "b":
				break
			else:
				print "That didn't make sense"

	elif question.lower() == 'trial':
		clubSort(filename)

	elif question.lower() == 'nadacyear':
		current_year = time.gmtime()[0]
		while True:
			s_year = raw_input("NADAC years begin on August 1st, enter the year you'd like to look up in the form YYYY" + "\n" + "or 'B' to go back to choices" + "\n")
			if s_year == 'b':
				break
			elif int(s_year) in range(1993, current_year + 1):
				e_year = int(s_year) + 1
				nadacYear(filename, s_year, e_year)
			else:
				print "Please enter a valid year"

	elif question.lower() == 'lifetime':
		lifetimeSort(filename)
	


	elif question.lower() == 'exit':
		print "Good Day!"
		break
		





