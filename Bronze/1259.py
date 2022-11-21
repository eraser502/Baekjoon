# 팰린드롬수
N = input()
while N != "0":
    revN = N[::-1]
    if N == revN:
        print("yes")
    else:
        print("no")
    N = input()