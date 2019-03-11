sum = 0
a = 0
b = 0
diff = 0
i = int(input())
while i != 0:
    sum += i
    if i < 0:
        a += 1
    if i > 0:
        b += 1
    i = int(input())
diff = b - a
print(sum)
print(diff)