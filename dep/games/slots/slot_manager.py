from os import system
print("Какой слот выбрать? (-1 для выхода)")
print("1. Слот купюры (250)")
print("2. Классика (100)")
print("3. Мажор (100000)")
a = int(input())
if a == 1:
	system("cls")
	system("py slot1.py")
elif a == 2:
	system("cls")
	system("py slot2.py")
elif a == 3:
	system("cls")
	system("py slot3.py")
else:
	system("cls")
	system("cd ../.. & py main.py")