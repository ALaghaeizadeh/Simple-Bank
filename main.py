########START#########
import colorama
from time import sleep
from sys import exit
from colorama import Fore as F

br = open('balance.txt' , "r")
newpart = "\n\n\n\n\n\n\n"

colorama.init(autoreset=True)

class AccountManager:
	def show_accounts(self) -> str:
		with open('accounts.txt',"r") as f:
			al = f.read()
			al = al.split("\n")
			output = []
			for i in range(len(al) - 1):
				output.append(str(i + 1) + '.' + al[i] + '\n')
			return "".join(output)

	def	add_account(self,new_account_name,new_account_password):
		with open('accounts.txt','a') as f:
			f.write(new_account_name + '\n')
		with open('password.txt' , 'a') as f:
			f.write(new_account_password + "\n")
		with open('balance.txt', 'a+') as fa:
			fa.write('200')
	def check_password(self,un,pass_to_check) -> bool:
		with open('password.txt' , "r") as f:
			__p = f.read()
			__p = __p.split("\n")
			p2 = __p[un - 1]
			if p2 == pass_to_check:
				return True
			else:
				return False
	def length(self ,ufd = False) -> int:
		with open('accounts.txt',"r") as f:
			l = f.read()
			l = l.split("\n")
		if ufd == True:
			return len(l)-2
		else:
			return len(l)-1
class BANK:
	def __init__(self,aid):
		self.aid = aid - 1
	def balance(self):
		b = br.read()
		b = b.split("\n")
		return b[self.aid]
	def change_pass(self,new_pass):
		with open("password.txt", "r+") as f:
			__pass = f.read()
			__pass = __pass.split('\n')
		with open("password.txt" , "w") as f:
			__pass[self.aid] = new_pass
			f.write('\n'.join(__pass))
	def deposit(self,balance,to):
		__b2 = br.read()
		__b2 = __b2.split("\n")
		__b = []
		for v in __b2[:-1]:
			__b.append(int(v))
		__b[to] += balance
		__b[self.aid] -= balance
		for v in __b:
			__b2.append(str(v))
		with open("balance.txt" , "w") as f:
			f.write(__b2)
		
	
o = AccountManager()
print("Welcome to OOP Bank.")
sleep(1)
print(o.show_accounts())

ACCOUNT = input('''Please enter the NUMBER of your account.
If you don\'t have account , enter \\
You can exit with 0.
Your choice:''')
c = 0 
aid = 0
try:
	c = ACCOUNT
	try:
		ACCOUNT = int(ACCOUNT)
	except:
		raise TypeError
	del c
	if ACCOUNT > o.length() or ACCOUNT < 0:
		raise ValueError
	elif ACCOUNT == 0:
		print("Goodbye")
		exit()
	aid = ACCOUNT
	p = input("Enter your password:")
	if o.check_password(ACCOUNT,p) :
		pass
	else:
		print(F.RED + "Your password is incorrect")
		exit()
except TypeError:
	if c == "\\":
		n = input("Enter your name:")
		p = input("Enter your password:")
		cp = input("Confirm your password:")
		if p == cp: 					#Create User
			o.add_account(n,p)
			print(F.GREEN + "User created successfully")
		elif p != cp :
			print(F.RED + "Please enter the correct password.\n\rThe operation failed.")
			exit()
	else:	
		print(F.RED + "Please enter Valid input.")
		exit()
except ValueError:
	print(F.RED + "Please enter the number in the correct range.")
	exit()
finally:
	print(newpart)
#################################################################
bc = BANK(aid)
print("You have successfully logged in.")
while True:
	t = input("""Please enter the number of the option you want.
1. Account Balance
2. Deposit
3. View History
4. Change Password
5. Log Out
Your choice:""")
	try:
		t = int(t)
	except:
		print(F.RED + "Please enter Valid input.")
		continue

	if t == 1:
		print("Please Wait\n")
		sleep(1)
		print("Your account balance is:" , bc.balance() + '$')
		sleep(0.75)
		print(newpart)
	if t == 2:
		with open('accounts.txt' , 'r') as f:
			a2 = f.read()
			a2 = a2.split("\n")
			A = []
		for j in range(len(a2)-1):
			if j == aid-1:
				continue
			A.append(a2[j])
		A.append("Others")
		ou = []
		for k in range(len(A)):
			ou.append(str(k + 1) + '.' + A[k] + '\n')
		ou = ''.join(ou)
		i = input("Please enter your destination account number.\n" + ou + "\nYour choice:")
		try:
			i = int(i)
		except:
			print(F.RED + "Please enter Valid input.")
			continue
		if i > o.length():
			print(F.RED + "Please enter the number in the correct range.")
			continue
		balance_for_disposit = input("Please enter your desired amount:")
		try:
			balance_for_disposit = int(balance_for_disposit)
		except:
			print(F.RED + "Please enter Valid input.")
			continue
		if int(bc.balance()) < balance_for_disposit:
			print(F.RED + "Insufficient account balance")
			continue
		bc.deposit(balance_for_disposit,i-1)
	if t == 3:
		pass
	if t == 4:
		op = input("Enter your old password:")
		if o.check_password(aid,op):
			print("Your password is correct\n")
			np = input("Enter your new password:")
			cp = input("Confirm your new password:") 
			if np == cp:
				bc.change_pass(np)
				print("Changing password...")
				sleep(1)
				print(F.GREEN + "\nPassword changed successfully.")
				sleep(0.75)
				print(newpart)
			else:
				print(F.RED + "Please enter the correct password.\n\rThe operation failed.")
		else:
			print(F.RED + "Please enter the correct password.\n")
	if t == 5 or t == "\n":
		break
print("Goodbye")
exit()
br.close()

#########END##########
