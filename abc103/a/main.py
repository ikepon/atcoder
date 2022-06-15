import statistics

a1, a2, a3 = list(map(int, input().split()))

b1 = abs(a1 - a2) + abs(a2 - a3)
b2 = abs(a1 - a3) + abs(a2 - a3)
b3 = abs(a2 - a1) + abs(a1 - a3)
b4 = abs(a2 - a3) + abs(a1 - a3)
b5 = abs(a3 - a2) + abs(a2 - a1)
b6 = abs(a3 - a1) + abs(a2 - a1)

print(min(b1, b2, b3, b4, b5, b6))
