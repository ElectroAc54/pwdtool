import random

print("______      __")
print("|          /  \·")
print("|         /    \.")
print("|__      /______\.    Password tool coded by ElectroAc")
print("|       /        \.   for increase security")
print("|      /          \.")
print("|_____/            \.")
print(" ")
print(" ")
print("Select mode")
print("Mode 0 --> Create new ultrasecure password")
print("Mode 1 --> Modify password")
print("Mode 2 --> Create password dictionary")
print("Mode 3 --> Random based brute-force hacking checker for your password")
print("Mode 4 --> Dictionary based brute-force hacking checker for your password")
print("Mode 5 --> Algorithm based brute-force hacking checker for your password")
print("")
mode = int(input("Mode: "))

if mode == 0:
	print("Generating password...")
	lower = "abcdefgfijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	number = "0123456789"
	symbol = "[]{}#()*;#·_-/|@$~%&¬'¿?¡!"

	all = lower + upper + number + symbol
	large = int(input("Password length = "))
	print("Generating password...")
	password = "".join(random.sample(all,large))
	print("Generated password: " , password)

if mode == 1:
	pwd = input("Password to modify: ")
	large = int(input("Password length: "))

	password_to_modify = pwd
	lower = "abcdefgfijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	number = "0123456789"
	symbol = "[]{}#()*;#·_-/|@$~%&¬'¿?¡!"

	all = lower + upper + number + symbol + password_to_modify
	password = "".join(random.sample(all, large))
	print("New password: " , password)

if mode == 2:
	print("Generating databse...")
	password_checker1 = int(input("Symbols? (0 - No | 1 - Yes): "))
	password_checker2 = int(input("Uppers? (0 - No | 1 - Yes): "))
	password_checker3 = int(input("Numbers? (0 - No | 1 - Yes): "))
	password_checker4= int(input("Lowers (0 - No | 1 - Yes): "))

	uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowers = "abcdefghijklmnopqrstuvwxyz"
	number = "0123456789"
	symbol = "[]{}#()*;#·_-/|@$~%&¬'¿?¡!"

	all = ""

	if password_checker1 == 1:
		all = all + symbol
	if password_checker1 == 0:
		all = all
	if password_checker2 == 1:
		all = uppers
	if password_checker2 == 0:
		all = all
	if password_checker3 == 1:
		all = all + number
	if password_checker3 == 0:
		all = all
	if password_checker4 == 0:
		all = all
	if password_checker4 == 1:
		all = all + lowers

	min_large = int(input("Password min length: "))
	max_large = int(input("Password max length: "))

	database_length = int(input("Database length: "))
	database_name = input("Save as (incluide .txt): ")
	print("Generating database...")

	f = open(database_name , "w")

	checker = 0

	passwordarray = []

	while checker < database_length:
		password = "".join(random.sample(all,random.randint(min_large , max_large)))

		if password not in passwordarray:
			passwordarray.append(password)
			f.writelines(password + "\n")
			checker = checker + 1
			print("Password " + str(checker) + " is " + password)
			print(str((checker/database_length)*100) + "% Completed")
			print(" ")

		if password in passwordarray:
			print("Skipping this...")

		if checker == database_length:
			print("Finished! Saved as " + database_name)

if mode == 3:
	password = input("Password to check: ")
	password_length = int(input("Password to discover length: "))
	password_checker1 = int(input("Does your password contain symbols? (0 - No | 1 - Yes): "))
	password_checker2 = int(input("Does your password contain uppers? (0 - No | 1 - Yes): "))
	password_checker3 = int(input("Does your password contain numbers? (0 - No | 1 - Yes): "))
	password_checker4= int(input("Does your password contain lowers (0 - No | 1 - Yes): "))
	tries = int(input("How many times do you want to try? (minimum 100000000 times): "))

	uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowers = "abcdefghijklmnopqrstuvwxyz"
	number = "0123456789"
	symbol = "[]{}#()*;#·_-/|@$~%&¬'¿?¡!"

	if password_checker1 == 1:
		all = all + symbol
	if password_checker1 == 0:
		all = all
	if password_checker2 == 1:
		all = uppers
	if password_checker2 == 0:
		all = all
	if password_checker3 == 1:
		all = all + number
	if password_checker3 == 0:
		all = all
	if password_checker4 == 0:
		all = all
	if password_checker4 == 1:
		all = all + lowers

	checker = 0

	print("Checking password...")

	while checker < tries:
		print("Generating passwords...")
		print(" ")
		generated_password = "".join(random.sample(all,password_length))
		checker = checker + 1
		print("Password " + str(checker) + " of " + str(tries) + " is " + generated_password)
		print(" ")
		print("Percentage: " + str((checker/tries)*100) + "%")
		print(" ")
		print(" ")
		print(" ")

		if generated_password == password:
			print("You're not save")
			print("Tries: " + str(checker))
			break

		if tries == checker:
			print("You have a good password")
			print("Tries " + str(checker))
			break

if mode == 4:
	password = input("Password to check: ")
	file_name = input("Dictionary file name (add .txt at the end): ")
	f = open(file_name , "r")
	print("Searching in diccionary...")
	
	flag = 0
	index = 0

	for line in f:
		index = index + 1
		print("Searching in line " + str(index))

		if password in line:
			flag = 1
			print("Password found! Your password is not secure")

if mode == 5:
	password = input("Password to check: ")
	password_length = int(len(password))
	print("Your password length is " + str(password_length))

	uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowers = "abcdefghijklmnopqrstuvwxyz"
	number = "0123456789"
	symbol = "[]{}#()*;#·_-/|@$~%&¬'¿?¡!"

	all = ""

	if any(elem in password for elem in uppers) == True:
		all = all + uppers

	if any(elem in password for elem in lowers) == True:
		all = all + lowers

	if any(elem in password for elem in number) == True:
		all = all + number

	if any(elem in password for elem in symbol) == True:
		all = all + symbol

	guessarray = []
	count = 0

	guess = ""
	guessarray = []

	while guess != password:
		guess = "".join(random.sample(all, password_length))

		if guess not in guessarray:
			count = count + 1
			guessarray.append(guess)
			print("Guess " + str(count) + " is " + str(guess))

			if guess == password:
				print("Your password is " + guess)
				print("Password hacked! You're not save :(")
				break

		if password in guessarray:
			print("Skipping this...")
