ticket = input()

first_sum = sum(map(int, ticket[:3]))
last_sum = sum(map(int, ticket[3:]))

print("YES" if first_sum == last_sum else "NO")
