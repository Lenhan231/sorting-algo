arr = [2, 3, 4, 8, 9, 10, 13, 40, 100]
def linear(arr,index):
    for i in range(0, len(arr)):
        if arr[i] == index:
            return i
    return -1

a = int(input())
if linear(arr,a) == -1:
    print("Not found")
else:
    print(linear(arr,a))        