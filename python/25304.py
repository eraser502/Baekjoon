cost = int(input())
tc = int(input())
rctp = 0
for i in range(tc):
 rct = list(map(int, input().split()))
 rctp += rct[0] * rct[1]
if cost == rctp:
 print("Yes")
else: 
 print("No")

