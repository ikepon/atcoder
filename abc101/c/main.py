n, k = list(map(int, input().split()))

num = 1
n -= k
while True:
    if n <= 0:
        break

    n -= k - 1
    num += 1

print(num)
