from time import sleep
from sys import exit
class BANK:
	pass
class AccountManager(BANK):
	def show_accounts(self):
		with open('accounts.txt',"r") as f:
			al = f.read()
			al = al.split("\n")
			output = []
			for i in range(len(al)):
				output.append(str(i + 1) + '.' + al[i] + '\n')
			return "".join(output)
	def	add_account(self,new_account_name):
		with open('accounts.txt','a') as f:
			f.write(new_account_name)
	
print()
o = AccountManager()
print("Welcome to OOP Bank.")
sleep(0.5)
print(o.show_accounts())

ACCOUNT = input('''Please enter the NUMBER of your account.
If you don\'t have account , enter \\
Your choice:''')
c = None
try:
	c = ACCOUNT
	ACCOUNT = int(ACCOUNT)
except ValueError:
	if c == "\\":
		o.add_account("A")
	else:	
		print("Please enter Valid input.")
		exit()
		


