1)
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

h1 = (a1*a1 + b1*b1) ** 0.5
h2 = (a2*a2 + b2*b2) ** 0.5

if h1 > h2:
    print("First is bigger")
elif h1 < h2:
    print("Second is bigger")
else:
    print("Equal")
2)
text = input()
words = text.split()

for w in words:
    letters = list(w)

    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[i] > letters[j]:
                letters[i], letters[j] = letters[j], letters[i]

    print("".join(letters), end=" ")

