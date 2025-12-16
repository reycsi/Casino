from random import randint, choices
from time import sleep
from os import system
def leave():
	system("cls")
	system("py slot_manager.py")
	exit()
def game(cnt):
	char = ['🪙', '💍', '💵', '💰', '✨']
	wei = [5000, 3000, 1000, 500, 100]
	won = 0
	for _ in range(cnt):
		first = choices(char, weights = wei, k = 1)[0]
		second = choices(char, weights = wei, k = 1)[0]
		third = choices(char, weights = wei, k = 1)[0]
		for i in range(100):
			print(choices(char)[0], end = '', flush = True)
			print('\b\b', end = '', flush = True)
			sleep(0.01 / (cnt ** 2))
		print(first, end = '', flush = True)
		for i in range(100):
			print(choices(char)[0], end = '', flush = True)
			print('\b\b', end = '', flush = True)
			sleep(0.01 / (cnt ** 2))
		print(second, end = '', flush = True)
		for i in range(100):
			print(choices(char)[0], end = '', flush = True)
			print('\b\b', end = '', flush = True)
			sleep(0.01 / (cnt ** 2))
		print(third)
		if first == second == third:
			if first == '🪙':
				won += 500000
			elif first == '💍':
				won += 1000000
			elif first == '💵':
				won += 5000000
			elif first == '💰':
				won += 10000000
			elif first == '✨':
				won += 100000000
	print("Итог")
	if cnt * 100000 <= won:
		print("Вы выиграли " + str(won - cnt * 100000) + "!")
	else:
		print("Вы проиграли " + str(cnt * 100000 - won) + ".")
	return won
money = float(open("..//../save//money.txt").readlines()[0].split()[0])
while True:
	print("Ваш баланс: " + str(int(money)))
	kol = int(input("Сколько раз сыграть (каждая игра за 100000)? (-1 - выход): "))
	if kol == -1:
		leave()
	if money < 100000 * kol:
		print("Мало денег")
		continue
	money -= 100000 * kol
	system("cls")
	money += game(kol)
	sleep(2)
	system("cls")
	system("cd ..//..//save & echo " + str(money) + " > money.txt")