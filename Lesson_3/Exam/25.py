n = int(input("Input amount:"))
sum = 0
a = 0
i = int(input())
while i != 0:
    sum += i
    if i % 2 == 0 and i % 5 == 0:
        a += 1
    i = int(input())
print(sum)
print(a)
