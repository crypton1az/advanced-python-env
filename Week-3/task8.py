1)
n = int(input())

for i in range(1, n + 1):
    ok = True
    for d in str(i):
        if d == "0" or i % int(d) != 0:
            ok = False
    if ok:
        print(i, end=" ")
2)
m = int(input())
arr = []

for i in range(m):
    arr.append(int(input()))

print(arr)

arr[0], arr[-1] = arr[-1], arr[0]

print(arr)
