with open("dayso.txt", "r") as ds:
    x = list(map(int, ds.readline().split()))

def swap(a, b):
    return b, a

def bubble(x, k):
    if k == 0:
        return x
    else:
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = swap(x[i], x[i + 1])
        return bubble(x, k - 1)

sorted_list = bubble(x, len(x))
print(sorted_list)