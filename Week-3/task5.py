1)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

num = a*d - c*b
den = b*d

g = gcd(abs(num), den)
print(num//g, "/", den//g)
2)
n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
