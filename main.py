import random
from table import Table
print("                      ___       ___  ___    _    ___  ")
print("    /\    /\         / _ \     / _ \/ _ \  |_|  / _ \ ")
print("   /  \  /  \       / /_\ \   | |_|  |_| |  _  | |_| |")
print("  / /\ \/ /\ \     / _____ \   \___/\___/  | |  \___/|")
print(" / /  \__/  \ \   / /     \ \     |  |     | |  / /| |")
print("/ /          \ \ / /       \ \    |  |     | | / / | |")
print("                    Автор MrCronix\nДля завершення гри напишіть quit")
class Game():
	@classmethod
	def start(self):
		while True:
			temporage_list = []
			total_players_role = []
			print("\nВведіть кількість гравців")
			command = input()
			print("")
			if command == "quit":
				print("Гра завершена")
				break
			roles = Table.calculate(int(command))
			for i in range(roles[0]):
				temporage_list.append("Мирний житель")
			for i in range(roles[1]):
				temporage_list.append("Мафія")
			for i in range(roles[2]):
				temporage_list.append("Доктор")
			for i in range(roles[3]):
				temporage_list.append("Шериф")
			for i in range(roles[4]):
				temporage_list.append("Маніяк")
			for i in range(roles[5]):
				temporage_list.append("Коханка")
			for i in range(int(command)):
				total_players_role.append(temporage_list.pop(random.randint(0, len(temporage_list)-1)))
			for i in range(1,int(command)+1):
				print(str(i)+".", total_players_role[i-1])
if __name__ == '__main__':
	Game.start()