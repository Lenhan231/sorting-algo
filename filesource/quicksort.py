def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

with open("dayso.txt", "r") as ds:
    arr = list(map(int, ds.readline().split()))

sorted_arr = quicksort(arr)
print(sorted_arr)