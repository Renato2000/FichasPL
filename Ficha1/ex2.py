import re

inputFromUser = input(">> ")
while inputFromUser != "":
	if re.search(r'^\d{1,3}(.\d{1,3}){3}$', inputFromUser):
		print("IPV4")
	elif re.search(r'^[\d\w]{1,4}(:[\d\w]{1,4}){7}$', inputFromUser):
		print("IPV6")
	else:
		print("Erro")
	inputFromUser = input(">> ")