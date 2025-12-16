import keyboard
from random import choices
from time import sleep
from os import system
def leave():
	system("cls")	
	system("cd .. & py main.py")
	exit()
money = float(open("..//save//money.txt").readlines()[0].split()[0])
while True:
	print("Ваш баланс: " + str(int(money)))
	q = int(input("Введите ставку (целое число > 1 или -1, чтобы выйти): "))
	if q == -1:
		leave()
	if (q < 1):
		continue
	if q > money:
		print("Слишком мало денег.")
		continue
	print("Нажмите пробел, чтобы закончить.")
	money -= q
	a = []
	chance = []
	st = 1.1
	while st < 1000:
		a.append(st)
		chance.append((1 / st) ** 3)
		st += 0.1
	rand = choices(a, weights = chance, k = 1)[0]
	win = 1
	flag = False
	moment = 0
	while win <= rand:
		if moment % 100 == 0:
			print(round(win, 2))
		if keyboard.is_pressed('space'):
			flag = True
			break
		win += 0.001
		sleep(0.001)
		moment += 1
	if flag:
		print("Победа!")
		money += q * win
	else:
		print("Краш (поражение)")
	sleep(2)
	system("cls")
	system("cd ..//save & echo " + str(money) + " > money.txt")