from random import randint, choices
from time import sleep
from os import system
def leave():
	system("cls")
	system("py slot_manager.py")
	exit()
def game(cnt, real_game):
	char = ['🍓', '🍌', '💎', '🍉', '🎁', '💵']
	wei = [1000, 400, 200, 100, 50, 3]
	won = 0
	for _ in range(cnt):
		first = choices(char, weights = wei, k = 1)[0]
		second = choices(char, weights = wei, k = 1)[0]
		third = choices(char, weights = wei, k = 1)[0]
		for i in range(100):
			print(choices(char)[0], end = '', flush = True)
			print('\b\b', end = '', flush = True)
			if real_game:
				sleep(0.01 / (cnt ** 2))
		print(first, end = '', flush = True)
		for i in range(100):
			print(choices(char)[0], end = '', flush = True)
			print('\b\b', end = '', flush = True)
			if real_game:
				sleep(0.01 / (cnt ** 2))
		print(second, end = '', flush = True)
		for i in range(100):
			print(choices(char)[0], end = '', flush = True)
			print('\b\b', end = '', flush = True)
			if real_game:
				sleep(0.01 / (cnt ** 2))
		print(third)
		if first == '💎':
			won += 100
		if second == '💎':
			won += 200
		if third == '💎':
			won += 100
		if first == '💵':
			won += 100000
		if second == '💵':
			won += 100000
		if third == '💵':
			won += 100000
		if first == second == third:
			if first == '🍓':
				won += 400
			elif first == '🍌':
				won += 1000
			elif first == '💎':
				won += 8000
			elif fist == '🎁':
				won += game(15, 0) + 20000
			else:
				won += 1000000
		else:
			kol = 0
			if first == '🎁':
				kol += 5
			if second == '🎁':
				kol += 5
			if third == '🎁':
				kol += 5
			if kol != 0:
				won += game(kol, 0)
	if real_game:
		print("Итог")
		if cnt * 250 <= won:
			print("Вы выиграли " + str(won - cnt * 250) + "!")
		else:
			print("Вы проиграли " + str(cnt * 250 - won) + ".")
	return won
money = float(open("..//../save//money.txt").readlines()[0].split()[0])
while True:
	print("Ваш баланс: " + str(int(money)))
	kol = int(input("Сколько раз сыграть (каждая игра за 250)? (-1 - выход): "))
	if kol == -1:
		leave()
	if money < 250 * kol:
		print("Мало денег")
		continue
	money -= 250 * kol
	system("cls")
	money += game(kol, 1)
	sleep(2)
	system("cls")
	system("cd ..//..//save & echo " + str(money) + " > money.txt")