str = input("请输入一个回文数:")
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