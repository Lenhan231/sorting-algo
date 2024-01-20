arr = [5,13,29,101,42,73,99,1012]
def insertion(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            while i != 0:
                if arr[i]<arr[i-1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    i-=1
                else:
                    i-=1
insertion(arr)  
print(arr)

