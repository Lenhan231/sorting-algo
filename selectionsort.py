with open("dayso.txt", "r") as ds:
    x = list(map(int, ds.readline().split()))
    k = []
def selection(x,k):
    for i in range(0,len(x)):
        r = min(x)
        k.append(r)
        x.remove(min(x))
    return k
selection(x,k)
print(k)

