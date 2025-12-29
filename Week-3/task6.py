1)
a = int(input())
b = int(input())

x, y = a, b
while y:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print(gcd, lcm)
2)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
diag = float(input())

s1 = (a*b) / 2
s2 = (c*d) / 2

print(s1 + s2)
