arr = [2, 3, 105, 300, 4, 8, 9, 10, 75, 99, 13, 40, 100]

for i in range(0, len(arr)):
    if int(arr[0]) < int(arr[i]):
        arr[0], arr[i] = int(arr[i]), int(arr[0])

print(arr[0])


