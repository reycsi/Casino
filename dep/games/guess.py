from random import randint
from os import system
from time import sleep
def leave():
	system("cls")
	system("cd .. & py main.py")
	exit()
money = float(open("..//save//money.txt").readlines()[0].split()[0])
while True:
	print("Ваш баланс: " + str(int(money)))
	q = input("введите коэффициент (целое число > 1 или -1, если хотите выйти.): ")
	q = int(q)
	if q == -1:
		leave()
	rand = randint(1, q)
	bal = input("Введите ставку (целое число > 1): ")
	bal = int(bal)
	if bal > money:
		print("Мало денег")
		continue
	money -= bal
	print("Загадано целое число от 1 до " + str(q))
	userNum = int(input("Отгадайте его: "))
	if userNum == rand:
		money += bal * q
		print("Победа")
	else:
		print("Вы проиграли, правильный ответ - " + str(rand))
	sleep(2)
	system("cls")
	system("cd ..//save & echo " + str(money) + " > money.txt")