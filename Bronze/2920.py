asd = [1,2,3,4,5,6,7,8]
dsd = [8,7,6,5,4,3,2,1]
ip = list(map(int, input().split(" ")))
if ip == asd:
    print("ascending")
elif ip == dsd:
    print("descending")
else:
    print("mixed")

