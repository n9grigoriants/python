n = int(input("Input amount:"))
a = []
max = 0
for i in range(n):
    a.append(int(input("Input value:")))
for i in range(n):
    if a[i]%5 == 0:
        if a[i] > max:
            max = a[i]
print(max)
        