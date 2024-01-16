h = open("dayso.txt")
a = h.read().split()

for i in range(0, len(a)):
    if int(a[0]) < int(a[i]):
        a[0], a[i] = int(a[i]), int(a[0])

print(a[0])

h.close()  # Don't forget to close the file
