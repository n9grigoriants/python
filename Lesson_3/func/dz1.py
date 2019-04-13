def find_min(a, b, c, d):
    if a < b and a < c and a < d:
        return a
    if b < a and b < c and b < d:
        return b
    if c < a and c < b and c < d:
        return c
    if d < a and d < b and d < c:
        return d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
result = find_min(a, b, c, d)
print(result)