ds = open("dayso.txt")
arr = ds.read().split()
arr = list(map(int, arr))
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]#arr trong vong lap de quy
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
mergeSort(arr)
print(arr)

 