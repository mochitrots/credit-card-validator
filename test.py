# class Number:
#     integers = [5, 6, 7]
#     for i in integers:
#         i * 2

# print(Number.i)

# from abc import ABC, abstractmethod
# class Animal(ABC):
# 	def oink(self):
# 		print("It's gonna oink")
    
# 	@abstractmethod
# 	def jump(self):
# 		pass

# class Kitten(Animal):
# 	def meow(self):
# 		print("smsm")

# class Doggo(Animal):
# 	def jump(self):
# 		print("The doggo jumps at the frisbee.")
		

# mouchi = Kitten()
# bruno = Doggo()



# bruno.jump()
# mouchi.oink()

# class Kitchen:
# 	color = None

# class Bedroom:
# 	color = None

# def change_color(room, color):
# 	room.color = color

# lower_kitchen = Kitchen()
# upper_kitchen = Kitchen()
# small_bedroom = Bedroom()
# master_bedroom = Bedroom()

# change_color(lower_kitchen, "white")
# change_color(upper_kitchen, "yellow")
# change_color(small_bedroom, "pink")
# change_color(master_bedroom, "burgandy")

# print(lower_kitchen.color)
# print(upper_kitchen.color)
# print(small_bedroom.color)
# print(master_bedroom.color)

# class Duck:
# 	def walk(self):
# 		print("This duck be walking")
# 	def talk(self):
# 		print("This duck be quacking")
		
# class Sheep:
# 	def walk(self):
# 		print("This sheep be walking")
# 	def talk(self):
# 		print("This sheep be baaa-ing")

# class Kitten():
# 	def __init__(self, name):
# 		self.name = name
	
# 	def catch(self, duck):
# 		duck.walk()
# 		duck.talk()
# 		print("De "+self.name+" caught de critter") ; print("De "+self.name+" steps on de critter & meows")

# duck = Duck()
# sheep = Sheep()
# mouchii = Kitten("Mouchii")

# mouchii.catch(duck)

# mouchii.catch(sheep)


# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4, 5]
# import numpy as np
# a = np.array(a)
# b = np.array(b)

# IF LENGTHS OF EACH NOT KNOWN

# if len(a) < len(b):
#     c = b.copy()
#     c = c[:len(a)] / a
# else:
#     c = a.copy()
#     c = c[:len(b)] / b
# print(c)

# IF WE KNOW THAT B IS BIGGER

# a.resize(b.shape)
# c = a * b
# print(c)

# a.resize(b.shape)
# print(a)

# c = a[1:2]
# print(c)

# import numpy as np
# a = [99, False, True]
# b = np.array(a)
# print(b)
# nums = [[11, 22, 55.7, 23],
# [22, 55, 6, 5]]

# np_num = np.array(nums)
# print(np_num)

# import matplotlib.pyplot as plt
# frauts = ["Apples", "Oranges", "Kiwis"]
# qty = [9, 11, 77]

# pop = [1.11, 7.19, 11.5, 22.9]
# gdp_pc = [5000, 11000, 99100, 58090]
# plt.plot(frauts, qty)
# plt.show()
# plt.clf()
# plt.scatter(pop, gdp_pc)
# plt.show()
# plt.clf()
