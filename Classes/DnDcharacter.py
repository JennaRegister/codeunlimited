from numpy import random
class Character:
	def __init__(self,name,race,class_):
		if race=="random":
			self.race = random.choice(['orc','elf','human','dwarf','gnome'])
		if class_=="random":
			self.class_ = random.choice(['sorcerer','barbarian','bard','paladin','monk','druid'])
		else:
			self.race = race
		self.name = name





char = Character("jenn","random","random")
print char.class_

