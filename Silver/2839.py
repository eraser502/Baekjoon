# 설탕 배달
N = int(input())
fI = N // 5
tR = 1
if N == 4 or N == 7:
 print(-1)
elif N % 5 == 0:
 print(fI)
else: 
 while tR != 0:
  tR = (N - fI * 5) % 3
  fI -= 1
 print(fI + (N - fI * 5) // 3) 
 
 
