import random

studentDict = {'Eric':80, 'Scott':75, 'Jessa':95, 'Mike':66}
print("Dictionary Before Shuffling")
print(studentDict)
keys =  list(studentDict.keys())
random.shuffle(keys)

ShuffledStudentDict = dict()
for key in keys:
  ShuffledStudentDict.update({key:studentDict[key]})

print("\nDictionary after Shuffling")
print(ShuffledStudentDict)