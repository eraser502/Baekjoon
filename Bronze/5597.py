a = []
b = []   
for i in range(28):
 a.append(int(input()))
a.sort()
for i in range(1, 31):
 if (i in a) == False:
  b.append(i)
print(b[0])
print(b[1]) 

