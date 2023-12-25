with open("dayso.txt", "r") as ds:
    x = list(map(int, ds.readline().split()))
    xcopy = x.copy()

def quicksort(a, b):
    for i in range(len(a)):
        if b < a[i]:
            a.append(a[i])
            a.pop(i)

def pc(c):
    for i in range(len(c)):
        quicksort(x, c[i])

pc(xcopy)
print(x)
