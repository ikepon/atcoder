d, g = list(map(int, input().split()))

sum = 0
for n in range(0, d):
    p, c = list(map(int, input().split()))
    sum += n * 100 + c
    if sum >= g:
        print(n + 1)
