import statistics

n = int(input())
arr = list(map(int, input().split()))

median = statistics.median(arr)
ans = 0

for i in range(0, n):
    ans += abs(arr[i] - (median + i + 1))

print(ans)
