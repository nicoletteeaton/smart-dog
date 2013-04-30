from agility_parse import *







while True:
	print "How would you like to view " + dog_name + "'s records?"
	print "Your choices are:" + '\n' + 'level' + '\n' + 'class' + '\n' + 'trial' + '\n' + 'nadacyear' + '\n' + 'lifetime'+ '\n' + 'platinum' + '\n' + 'natch' + '\n' + 'title'
	print "If you are finished, please type 'exit'"
	question = raw_input("Please sort " + dog_name + "'s records by:")

	if question.lower() == 'level':
		while True:
			level = raw_input("Please choose a level by entering:" + "\n" + "'E' for Elite" + "\n" + "'O' for Open" + "\n" + "'N' for Novice" + "\n" + "or 'B' to go back to choices" + "\n")
			input = level.upper()
			if input == "E":
				levelSort(input)
			elif input == "O":
				levelSort(input)
			elif input == "N":
				levelSort(input)
			elif input == "B":
				break
					
			else:
				print "That didn't make sense"

	elif question.lower() == 'class':
		while True:
			class_level = raw_input("Please choose a class by entering one of the following:" + "\n" + "'R' for Regular" + "\n" + "'J' for Jumpers" + "\n" + "'C' for Chances" + "\n" + "'TN' for Tunnelers" + "\n" + "'TG' for Touch 'n Go" + "\n" + "'W' for Weavers" + "\n" + "'H' for Hoopers" + "\n" "or 'B' to go back to choices" + "\n")
			input = class_level.lower()
			if input == "r":
				nadac_classSort('regular')
			elif input == "j":
				nadac_classSort('jumpers')
			elif input == "c":
				nadac_classSort('chances')
			elif input == "tn":
				nadac_classSort('tunnelers')
			elif input == "tg":
				nadac_classSort("touch 'n go")
			elif input == "w":
				nadac_classSort('weavers')
			elif input == "h":
				nadac_classSort('hoopers')
			elif input == "b":
				break
			else:
				print "That didn't make sense"

	elif question.lower() == 'trial':
		clubSort()

	elif question.lower() == 'nadacyear':
		current_year = time.gmtime()[0]
		while True:
			start_year = raw_input("NADAC years begin on August 1st," 
			" enter the year you'd like to look up in the form YYYY" + 
			"\n" + "or 'B' to go back to choices" + "\n")
			if start_year == 'b':
				break
			elif int(start_year) in range(1993, current_year + 1):
				end_year = int(start_year) + 1
				nadacYear(start_year, end_year)
			else:
				print "Please enter a valid year"

	elif question.lower() == 'lifetime':
		lifetimeSort()
		
	elif question.lower() == 'platinum':
		platinumSort()
	
	elif question.lower() == 'natch':
		natchSort()
		
	elif question.lower() == 'title':
		titleSort()


	elif question.lower() == 'exit':
		print "Good Day!"
		break
		
	else:
		print "I didn't understand that, please try again"
		





