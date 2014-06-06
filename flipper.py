import random
import math

def wait():
	raw_input("\nPress 'Return' to continue.")

def roll(num,d,mod):
	i = 0
	result = 0
	while(i<num):
		result += random.randint(1,d)
		i += 1
	result += mod
	return result

def coin():
	num = roll(2)
	if num == 1:
		print '\nHeads'
		wait()
	else:
		print '\nTails'
		wait()

def check_choice(Choice):
	try:
		Choice = int(Choice)
	except:
		print "\nPlease input integer values for that operation"
		Choice = float('nan')
		wait()
	return Choice

def check_silent(Choice):
	try:
		Choice = int(Choice)
	except:
		Choice = float('nan')
		wait()
	return Choice

def main():
	Loop = 1
	while(Loop > 0):
		print "\nChoose desired operation: \n 0: Quit \n 1: Coin flip \n 2: Die roll"
		Choice = check_choice(raw_input('>>'))
		if(Choice == 0):
			Loop = 0
			print "\nGood bye."
			break
		elif(Choice == 1):
			coin()
		elif(Choice == 2):
			dice()
		elif(math.isnan(Choice)):
			continue
		else:
			print "\nInvalid input. Please try again."
			wait()

def unimplemented():
	print "\nUnimplemented option."
	wait()


def dice():
	Rolling = 1
	while(Rolling > 0):
		print "\nChoose input method: \n 0: Cancel \n 1: Standard Roll Notation \n 2: Prompted Entry"
		Method = check_choice(raw_input('>>'))
		if(Method == 0):
			print "\nReturning to Main Menu."
			wait()
			break
		elif(Method == 1):
			roll_std()
		elif(Method == 2):
			roll_prompted()
		elif(math.isnan(Method)):
			continue
		else:
			print "\nInvalid input. Please try again."
			wait()

def roll_std():
	unimplemented()
	# print "/nPlease input required roll in Standard Roll Notation."
	# RawNote = raw_input('>>')
	# Note = RawNote.replace(' ','')
	# Note = Note.replace('d',',')
	# Note = Note.replace('-','+-')
	# Note = Note.replace('+',',')
	# Args = Note.split(',')
	# try:
		# NumDice,NumSides,Mod = Args
	# except:
		# try:
			# NumDice,NumSides = Args
			# Mod = 0
		# except:
			# try:
				# NumSides = Args
				# NumDice = 1
				# Mod = 0
			# except:
				# print "Can't roll dice with input", RawNote
				# return
	# NumDice = check_silent(NumDice)
	# NumSides = check_silent(NumSides)
	# Mod = check_silent(Mod)
	# if(Num
	# print ""
	# print "%rd%r+%r= %r" % (NumDice,NumSides,Mod,roll(NumDice,NumSides,Mod))

def roll_prompted():
	Prompting = 1
	while(Prompting == 1):
		print "\nHow many dice?"
		NumDice = check_choice(raw_input('>>'))
		if(NumDice < 1):
			print "\nInvalid input, please input an integer greater than zero."
			wait()
		elif(math.isnan(NumDice)):
			Purple = 'pink'
		else:
			Prompting = 2
	while(Prompting == 2):
		print "\nHow many sides?"
		NumSides = check_choice(raw_input('>>'))
		if(NumSides < 2):
			print "\nInvalid input, please input an integer greater than one."
			wait()
		elif(math.isnan(NumSides)):
			Purple = 'pink'
		else:
			Prompting = 3
	while(Prompting == 3):
		print "\nWhat is the modifier?"
		Mod = check_choice(raw_input('>>'))
		if(math.isnan(Mod)):
			Purple = 'pink'
		else:
			Prompting = 4
	print ""
	print "%rd%r+%r= %r" % (NumDice,NumSides,Mod,roll(NumDice,NumSides,Mod))



'''Operation starts here'''
main()