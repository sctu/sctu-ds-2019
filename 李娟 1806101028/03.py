#回文检测
str = input("please input something:")
original = []
inverted = []
for i in str:
    original.append(i)

while len(original) != 0:
    inverted.append(original.pop())

for i in str:
    original.append(i)

if original == inverted:
    print("True")
else:
    print("False")
