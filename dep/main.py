from os import system
while True:
	next_station = input("Во что сыграть? (1. Слоты, 2. Угадайка, 3. Ракета или -1 для выхода): ")
	if next_station == "1":
		system("cls")
		system("cd games/slots & py slot_manager.py")
		exit()
	elif next_station == '2':
		system("cls")
		system("cd games & py guess.py")
		exit()
	elif next_station == '3':
		system("cls")
		system("cd games & py crash.py")
		exit()
	elif next_station == '-1':
		exit()