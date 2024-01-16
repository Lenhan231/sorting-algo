ds = open("dayso.txt")
arr = ds.read().split()
a = int(input())
for i in range(0,len(arr)):
    if int(arr[i]) == a:
        print(i+1)