n = int(input())

ans = 0

for j in range(8, n + 1):
    if j % 2 == 0:
        continue

    divisor = []
    i = 1

    while True:
        if i > j:
            break

        if j % i == 0:
            divisor.append(i)

        i += 1

    if len(divisor) == 8:
        ans += 1

print(ans)
