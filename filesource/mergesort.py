with open("dayso.txt", "r") as ds:
    x = list(map(int, ds.readline().split()))
    xcopy = x.copy()
k= len(x)
for i in x:
    print(i,end=" ")
print(k)