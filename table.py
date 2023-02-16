class Table():
	@classmethod
	def calculate(self, count : int):
		peaceful = 0
		mafia = 0
		doctor = 0
		sheriff = 0
		maniac = 0
		mistress = 0
		if count < 6:
			print("Гра неможлива при кількості гравців:",count)
		elif count >= 6:
			sheriff = 1
			if count >= 9:
				maniac = 1
				if count >= 11:
					doctor = 1
					if count >= 15:
						mistress = 1
			if count == 6:
				mafia = 1
			elif 6 < count < 12:
				mafia = 2
			elif 11 < count < 20:
				mafia = 3
			elif 19 < count < 25:
				mafia = 4
			else:
				mafia = 5
			peaceful = count - mafia - doctor - sheriff - maniac - mistress
			return [peaceful, mafia, doctor, sheriff, maniac, mistress]
		else:
			print("Неправильні дані")