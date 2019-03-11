n = int(input("Input amount:"))
max = 0
for j in range(n):
    i = int(input())
    if i % 5 == 0:
        if i > max:
            max = i
print(max)