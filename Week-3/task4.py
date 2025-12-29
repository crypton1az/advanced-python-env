1)
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a = int(input())
b = int(input())
c = int(input())
d = int(input())

num = a * d
den = b * c

g = gcd(num, den)
print(num // g, "/", den // g)
2)
def inside(x, y, r):
    return x*x + y*y <= r*r

r = float(input())
count = 0

for i in range(3):
    x = float(input())
    y = float(input())
    if inside(x, y, r):
        count += 1

print(count)
