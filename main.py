x = 3
a = []
i = 0
z = 0
while z < 1000:
    i += 1
    z = i * x
    a.append(z)
a.pop()
print(a)

y = 5
b = []
c = 0
d = 0

while d < 1000:
    c += 1
    d = c * y
    b.append(d)
b.pop()
print(b)

finaltest = set(a + b)
print(finaltest)
finalvalue = 0
copylist = list(finaltest)
for i in range(len(finaltest)):
    finalvalue += (copylist[i])

print(finalvalue)
print("New")