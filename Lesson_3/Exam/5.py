n = int(input("Input amount:"))
sum = 0
for j in range(n):
    i = int(input())
    if i % 3 == 0:
        sum = sum + i
print(sum)