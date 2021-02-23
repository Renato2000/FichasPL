import re

inputFromUser = input(">> ")
while inputFromUser != "":
	y = re.search(r'(_|.)([0-9]+[A-Za-z]{3,})(\.|_)', inputFromUser)
	if y:
		print("VÁLIDO")
	else:
		print("INVÁLIDO")
	inputFromUser = input(">> ")