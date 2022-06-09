n = int(input())
arr = list(map(int, input().split()))

maximum = max(*arr)
minimum = min(*arr)

print(maximum - minimum)
