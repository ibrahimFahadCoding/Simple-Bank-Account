
oldpassword = ""
password1 = "iamfahad"
password2 = "secret123"
money = 0
money2 = 0

usernames = {"iMibbiFahad": password1, "alexvexab123": password2}
moneys = {"iMibbiFahad": money, "alexvexab123": money2}


choice = "4"
while True: 
		def login():
			global username
			global password
			username = ""
			password = ""
			print("EB Bank ☵")
			while username not in usernames:
					username = input("Enter your username: ")
					if username not in usernames: 
						print("Error: Incorrect username/password!")
					else:
						while password != usernames[username]:
								password = input("Enter your password: ")
								if password != usernames[username]:
									print("Error: Incorrect username/password!")
				
						
			choice = ""				
		if choice == "4":
			login()
			

		print("Hello " + username + "! You currently have $" + str(moneys[username]) + " in your account.")
		print("1: Make a deposit")
		print("2: Make a withdrawal")
		print("3: Change your password")
		print("4: Log Out")
		choice = input("Type 1,2,3,or 4: ")
		if choice != "1" and choice != "2" and choice != "3" and choice != "4":
			print("Error: Type 1,2,3,or 4.")
		if choice == "1":
			deposit = int(input("How much would you like to deposit: "))
			moneys[username] += deposit
		if choice == "2":
			withdraw = moneys[username] + 1
			while withdraw > moneys[username]:
				withdraw = int(input("How much would you like to withdraw: "))
				if withdraw > moneys[username]:
					print("Error: You are asking to withdraw more money than you have.")
			moneys[username] -= withdraw
		if choice == "3":
			while oldpassword != usernames[username]:
				oldpassword = input("Type in your old password: ")
				if oldpassword != usernames[username]:
					print("Error: Your old password is incorrect. ")
			newpassword = input("Type in your new password: ")
			usernames[username] = newpassword  
		
			
