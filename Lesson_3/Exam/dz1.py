sum = 0
i = int(input())
while i != 0:
    if i % 8 == 0 and i / 10 > 1:
        sum += i
    i = int(input())
print(sum)