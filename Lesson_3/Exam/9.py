n = int(input("Input amount:"))
sum = 0
for j in range(n):
    i = int(input())
    if i % 10 == 3:
        sum += 1
print(sum)