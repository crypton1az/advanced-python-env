1)
x = float(input())
y = float(input())
z = float(input())
t = float(input())

triangle = (x * y) / 2
rect = z * t

print(triangle + rect)
2)
n = int(input())
octal = ""

while n > 0:
    octal = str(n % 8) + octal
    n //= 8

while len(octal) < 10:
    octal = "0" + octal

print(octal)
