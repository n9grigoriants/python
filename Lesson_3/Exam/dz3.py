sum = 0
a = 0
n = int(input())
while n != 0:
    if n % 8 == 0:
        sum += n
        a += 1
    n = int(input())
if sum == 0:
    print("NO")
else:
    print(sum / a)
