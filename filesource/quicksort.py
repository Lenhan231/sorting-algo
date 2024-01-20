def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        l = 1
        r = len(arr) - 1

        while l <= r:
            while l <= r and arr[l] < pivot:
                l += 1
            while l <= r and arr[r] > pivot:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        leftarr = arr[1:l]
        rightarr = arr[l:]
        mid = [pivot]
        return quickSort(leftarr) + mid + quickSort(rightarr)


arr = [2, 3, 105, 300, 4, 8, 9, 10, 75, 99, 13, 40, 100]    
print(quickSort(arr))
