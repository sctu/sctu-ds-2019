str = 'abcdcba'
l = []
s = []
for i in str:
    l.append(i)

while len(l) != 0:
    s.append(l.pop())

for i in str:
    l.append(i)

if l == s:
    print("True")
else:
    print("False")