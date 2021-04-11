from instaclient import InstaClient
from instaclient.errors import *
from database import DataBase

client = InstaClient(driver_path='./chromedriver')

# Login
try:
    client.login(username='themain.end', password='L!iykMt!buJd229V15IC68EMU5CsU$vEzKsLOzxu@BUCiEqI4b7')
except VerificationCodeNecessary:
    code = input('Enter the 2FA security code generated by your Authenticator App or sent to you by SMS')
    client.input_verification_code(code)
except SuspisciousLoginAttemptError as error:
    if error.mode == SuspisciousLoginAttemptError.EMAIL:
        code = input('Enter the security code that was sent to you via email: ')
    else:
        code = input('Enter the security code that was sent to you via SMS: ')
    client.input_security_code(code)

# Menu
print(f"{DataBase.sentCount()}/{DataBase.Count()} Users\n")
print("1- Send")
print("2- Fetch")
choice = int(input('Choose by number: '))

if choice == 1:
	for user in DataBase.GetFromDB():

		if not int(user[3]):
			try:
				DataBase.SendUpdate(user[1], 2)
				client.send_dm(user[1], '')
				client.send_dm(user[1], '')
				print(f"Sending to {user[1]} "+"\033[32m"+"Success"+"\033[0m")
			except:
				DataBase.SendUpdate(user[1], 1)
				print(f"Sending to {user[1]} "+"\033[31m"+"Failed"+"\033[0m")
elif choice == 2:
	client.get_followers(user=input("Username: "), count=None)