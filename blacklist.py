import requests as r
import string as s
import random as rand
import time as t

loginUrl = "http://10.10.10.151/user/login.php"
registerUrl = "http://10.10.10.151/user/registration.php"
email = "test@test.com"
letters = s.ascii_letters
username = ''.join(rand.choices(letters, k=5))
password = "test"
badChars = s.punctuation
blacklisted = ""

for bc in badChars:
	newUsername = username+bc

	print(f"Testing : {newUsername}")

	data = {
		"email"		: email,
		"username"	: newUsername,
		"password"	: password,
		"submit"	: " "
	}

	response = r.post(registerUrl, data=data)
	
	if response.status_code == 200:
		data = {
			"username"	: newUsername,
			"password"	: password,
			"submit"	: " "
		}
		
		resp = r.post(loginUrl, data=data)
		
		if "Username/password is incorrect." in resp.text:
			print(f"[-] {bc} filtered")
			print("")
			blacklisted += bc
		else:
			print(f"[+] {bc} passed")
			print("")

print(f"Blacklist Char : {blacklisted}")
