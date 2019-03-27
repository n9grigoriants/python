sum = 0
b = 0
n = int(input())
for i in range(n):
    sum += i
    if i > 0:
        b += 1
print(sum / n)
if b >= 5:
    print("YES")
else:
    print("NO")