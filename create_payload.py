import requests as r
import string as s
import random as rand
import time as t
import sys

loginUrl = "http://10.10.10.151/user/login.php"
registerUrl = "http://10.10.10.151/user/registration.php"
email = "test@test.com"
letters = s.ascii_letters
password = "test"

if len(sys.argv) == 2:
	username = str(sys.argv[1])
else:
	sys.exit("[-] Error Argument")

data = {
	"email"		: email,
	"username"	: username,
	"password"	: password,
	"submit"	: " "
}

response = r.post(registerUrl, data=data)

if "Login V2" in response.text:
	print("[+] Register Success")
	data = {
		"username" 	: username,
		"password" 	: password,
		"submit"	: " "
	}
	response = r.post(loginUrl, data=data)
	
	if "User Portal Under Construction" in response.text:
		print("[+] Login Success")
else:
	sys.exit("[-] Register Error too much string")
