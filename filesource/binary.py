arr = [2, 3, 4, 8, 9, 10, 13, 40, 100]
a = 99

def binary(arr, inp):
    mid = len(arr) // 2

    if len(arr) > 0:
        if arr[mid] < inp:
            newarr = arr[mid+1:]
            binary(newarr, inp)
        elif arr[mid] > inp:
            newarr = arr[:mid]
            binary(newarr, inp)
        else:
            print(1)
    else:
        print(0)  

binary(arr, a)
