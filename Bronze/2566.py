A = []
for row in range(9):
    row = list(map(int, input().split()))
    A.append(row)
max_v = max(map(max, A))
for row in range(9):
    for col in range(9):
        if A[row][col] == max_v:
            print(max_v)
            print(row+1, col+1)
            break