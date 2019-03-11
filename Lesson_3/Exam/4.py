n = int(input("Input amount:"))
min = 30000
for j in range(n):
    i = int(input())
    if i % 3 == 0:
        if i < min:
            min = i
print(min)