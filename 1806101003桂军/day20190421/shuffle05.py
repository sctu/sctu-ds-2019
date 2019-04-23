import random
empName = ['Jhon', 'Emma', 'Kelly', 'Jason']
empAchievement = [90, 85, 87, 100]
print("Print Lists Before Shuffling")
print("List Employee Names: ", empName)
print("List Employee Achievement: ", empAchievement)
mapIndexPosition = list(zip(empName, empAchievement))
random.shuffle(mapIndexPosition)
empName, empAchievement = zip(*mapIndexPosition)
print("\nPrint Lists after Shuffling")
print("List Employee Names: ", empName)
print("List Employee Achievement: ", empAchievement)