with open("dayso.txt", "r") as ds:
    x = list(map(int, ds.readline().split()))
    xcopy = x.copy()
for i in x:
    print(i,end=" ")
    